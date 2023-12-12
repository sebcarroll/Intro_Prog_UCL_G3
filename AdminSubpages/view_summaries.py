import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox


class AdminViewSummaries:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main

    def create_gui_view_summaries(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        end_plan_frame = tk.Frame(self.window)
        end_plan_frame.grid(sticky="nsew", padx=5, pady=5)
        end_plan_frame.grid_columnconfigure(0, weight=1)
        end_plan_frame.grid_rowconfigure(3, weight=1)

        # Labels
        end_plan_title = tk.Label(end_plan_frame, text="View Plan Summaries", font=('Helvetica', 16))
        end_plan_title.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew", pady=5, padx=5)

        self.end_plan_tree = ttk.Treeview(end_plan_frame)
        self.end_plan_tree.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        # CSV data
        csv_file = "crisis_events.csv"
        #csv_data = self.load_csv_data(csv_file)
        self.upload_csv_data(self.end_plan_tree, csv_file)

        # Buttons
        # Edit event
        edit_event_btn = tk.Button(self.window, text="Edit Event", command=lambda: self.edit_csv_data_entry())
        edit_event_btn.grid(row=4, column=0, padx=5, pady=10)

        # Delete button
        delete_btn = tk.Button(self.window, text="Delete Event", command=lambda: self.delete_csv_data_entry(self.end_plan_tree, csv_file))
        delete_btn.grid(row=5, column=0, padx=5, pady=10)

        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=8, column=0, padx=5, pady=10)


    def upload_csv_data(self, tree, filename):
        data = pd.read_csv(filename)

        # The following block will convert floats to integers for the GUI to remove the ".0"
        # columns with float numbers
        float_columns = data.select_dtypes(include=['float']).columns
        # Convert floats to integers for display in treeview
        for col in float_columns:
            data[col] = data[col].fillna(0).astype(int)

        tree.delete(*tree.get_children())
        tree['columns'] = list(data.columns)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        for col in data.columns:
            tree.column(col, anchor=tk.CENTER, width=80)
            tree.heading(col, text=col, anchor=tk.CENTER)

        for index, row in data.iterrows():
            tree.insert("", tk.END, values=list(row), iid=str(index))


    def delete_csv_data_entry(self, tree, filename):
        selected_item = self.end_plan_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a plan to delete")
            return
        if messagebox.askokcancel("Delete Entry?", "Are you sure you want to delete this plan?\nYou will not be able to recover this plan"):
            selected_item = tree.selection()
            if selected_item:
                # Get the row index of the selected row
                index = int(selected_item[0])

                # Load current CSV data, delete the entry, save the deletion to the csv file
                data = pd.read_csv(filename)
                data = data.drop(index)
                data.to_csv(filename, index=False)

                # Refresh treeview to reflect change
                self.upload_csv_data(tree, filename)

    def edit_csv_data_entry(self):
        selected_item = self.end_plan_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a plan to edit")
            return

        selected_row = self.end_plan_tree.selection()
        if selected_row:
            row_content = self.end_plan_tree.item(selected_row[0], 'values')
            if row_content and row_content[7] == 'Inactive':
                messagebox.showwarning("Past Event", "You selected a deactivated plan\n\nYou cannot edit an inactive plan")
            else:
                plan_details = self.end_plan_tree.item(selected_item, 'values')

                # Attributes from the treeview
                column_attributes = self.end_plan_tree['columns']
                treeview_width = len(column_attributes)

                # Open pop up edit window
                edit_plan_window = tk.Toplevel(self.window)
                edit_plan_window.title("Edit Plan")

                # Create empty dictionary to store new edited info with key as attribute, value as new edited entry
                self.edited_entry_dictionary = {}

                # Create a label and entry for each plan attribute using column attributes
                for i in range(treeview_width):

                    att = column_attributes[i]
                    value = plan_details[i]

                    label = tk.Label(edit_plan_window, text=f"{att}:")
                    label.grid(row=i, column=0)

                    edit_entry = tk.Entry(edit_plan_window, textvariable=tk.StringVar(edit_plan_window, value=value))
                    edit_entry.grid(row=i, column=1)
                    self.edited_entry_dictionary[att] = edit_entry

                # Save button
                save_button = tk.Button(edit_plan_window, text="Save", command=lambda: self.save_plan(edit_plan_window, selected_item))
                save_button.grid(row=len(plan_details), column=1)

                # Cancel button
                save_button = tk.Button(edit_plan_window, text="Cancel", command=lambda: self.cancel_btn(edit_plan_window, selected_item))
                save_button.grid(row=len(plan_details)+1, column=1)


    def save_plan(self, edit_plan_window, selected_item):

        try:
            # list comprehension for new edited values
            updated_values = [entry.get() for entry in self.edited_entry_dictionary.values()]

            data = pd.read_csv("crisis_events.csv")

            selected_id = int(self.end_plan_tree.item(selected_item, 'values')[0])

            if selected_id in data[data.columns[0]].values:
                row_index = data[data[data.columns[0]] == selected_id].index[0]

                # Iterate over each column and convert updated values to the correct type
                for i, col_name in enumerate(data.columns):
                    col_type = data[col_name].dtype

                    # Convert the value to the column's type
                    if pd.api.types.is_numeric_dtype(col_type):
                        if updated_values[i] != '':
                            updated_values[i] = col_type.type(updated_values[i])
                        else:
                            updated_values[i] = pd.NA

                data.loc[row_index] = updated_values
                data.to_csv("crisis_events.csv", index=False)
                self.end_plan_tree.item(selected_item, values=updated_values)

            edit_plan_window.destroy()
            # CSV data
            csv_file = "crisis_events.csv"
            # csv_data = self.load_csv_data(csv_file)
            self.upload_csv_data(self.end_plan_tree, csv_file)

        except:

            messagebox.showinfo("Data Types", "Please select valid data types to save your edit")

    def cancel_btn(self, edit_plan_window, selected_item):
        edit_plan_window.destroy()
