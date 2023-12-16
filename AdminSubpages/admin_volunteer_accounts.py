import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox


class AdminVolunteerDisplay:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main

    def create_gui_volunteer_display(self, window):
        for i in self.window.winfo_children():
            i.grid_forget()
        for i in range(9):
            self.window.grid_columnconfigure(i, weight=1)
        display_volunteer_frame = tk.Frame(self.window)
        display_volunteer_frame.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
        for i in range(9):
            display_volunteer_frame.grid_columnconfigure(i, weight=1)
        for i in range(9):
            display_volunteer_frame.grid_rowconfigure(i, weight=1)


        # Labels
        display_volunteer_title = tk.Label(display_volunteer_frame, text="Display Volunteer Accounts", font=('TKDefault', 25), fg='white')
        display_volunteer_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
        display_volunteer_title.configure(background="grey")

        self.display_volunteer_tree = ttk.Treeview(display_volunteer_frame, height=10)
        self.display_volunteer_tree.grid(row=1, column=0, columnspan=9, sticky="nsew", padx=10, pady=5, rowspan=4)

        # Button Frame:
        btn_frame = tk.Frame(display_volunteer_frame)
        btn_frame.grid(row=6, column=4, pady=10, sticky="sew", rowspan=4)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # Buttons
        # View event
        view_btn = tk.Button(btn_frame, text="View Volunteer Profile", command=lambda: self.view_csv_data_entry())
        view_btn.grid(row=0, column=0, padx=20, pady=(50,10))

        # Edit event
        edit_btn = tk.Button(btn_frame, text="Edit Volunteer Profile", command=lambda: self.edit_csv_data_entry())
        edit_btn.grid(row=0, column=1, padx=20, pady=(50,10))

        # Delete button
        delete_btn = tk.Button(btn_frame, text="Delete Volunteer Profile", command=lambda: self.delete_csv_data_entry(self.display_volunteer_tree, csv_file))
        delete_btn.grid(row=0, column=2, padx=20, pady=(50,10))

        # Back button
        back_button = tk.Button(btn_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=2, column=1, padx=5, pady=40)



        # CSV data
        csv_file = "volunteer_info.csv"
        # csv_data = self.load_csv_data(csv_file)
        try:
            self.upload_csv_data(self.display_volunteer_tree, csv_file)
        except:
            messagebox.showwarning("No data found",
                                   "There is a problem accessing the database\n\nThe file may be missing or corrupted")
            self.back_button_to_admin_main()


    def upload_csv_data(self, tree, filename):
        data = pd.read_csv(filename, dtype={'Phone Number': str})
        data['Phone Number'] = data['Phone Number'].astype(str)
        # The following block will convert floats to integers for the GUI to remove the ".0"
        # columns with float numbers
        float_columns = data.select_dtypes(include=['float']).columns
        # Convert floats to integers for display in treeview
        for col in float_columns:
            data[col] = data[col].fillna(0).astype(int)
        columns_to_display = [col for col in data.columns if (col != "Deleted" and col != "Phone Number")]
        tree.delete(*tree.get_children())
        tree['columns'] = columns_to_display
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        for col in columns_to_display:
            tree.column(col, anchor=tk.CENTER, width=80)
            tree.heading(col, text=col, anchor=tk.CENTER)

        for index, row in data.iterrows():
            tree.insert("", tk.END, values=[row[col] for col in columns_to_display], iid=str(index))


    def delete_csv_data_entry(self, tree, filename):
        selected_item = self.display_volunteer_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a volunteer profile to delete")
            return
        if messagebox.askokcancel("Delete Volunteer Profile?", "Are you sure you want to delete this volunteer profile?\nYou will not be able to recover this volunteer profile"):
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

    def view_csv_data_entry(self):
        selected_item = self.display_volunteer_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a volunteer profile to view")
            return

        refugee_details = self.display_volunteer_tree.item(selected_item, 'values')

        # Attributes from the treeview
        column_attributes = self.display_volunteer_tree['columns']
        treeview_width = len(column_attributes)

        # Open pop up edit window
        refugee_profile_window = tk.Toplevel(self.window)
        refugee_profile_window.title("View Volunteer Details")
        refugee_profile_window.grab_set()

        # Create a label and entry for each plan attribute using column attributes
        for i in range(treeview_width):
            att = column_attributes[i]
            value = refugee_details[i]

            label = tk.Label(refugee_profile_window, text=f"{att}:")
            label.grid(row=i, column=0)

            current_camp_info = tk.Label(refugee_profile_window, textvariable=tk.StringVar(refugee_profile_window, value=value))
            current_camp_info.grid(row=i, column=1)

        # Close button
        save_button = tk.Button(refugee_profile_window, text="Close",command=lambda: self.cancel_btn(refugee_profile_window, selected_item))
        save_button.grid(row=len(refugee_details) + 1, column=1)


    def edit_csv_data_entry(self):
        selected_item = self.display_volunteer_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a volunteer profile to edit")
            return

        refugee_details = self.display_volunteer_tree.item(selected_item, 'values')

        # Attributes from the treeview
        column_attributes = self.display_volunteer_tree['columns']
        treeview_width = len(column_attributes)

        # Open pop up edit window
        refugee_profile_window = tk.Toplevel(self.window)
        refugee_profile_window.title("Edit Volunteer Details")
        refugee_profile_window.grab_set()

        # Create empty dictionary to store new edited info with key as attribute, value as new edited entry
        self.edited_entry_dictionary = {}

        # Create a label and entry for each plan attribute using column attributes
        for i in range(treeview_width):

            att = column_attributes[i]
            value = refugee_details[i]

            label = tk.Label(refugee_profile_window, text=f"{att}:")
            label.grid(row=i, column=0)

            edit_entry = tk.Entry(refugee_profile_window, textvariable=tk.StringVar(refugee_profile_window, value=value))
            edit_entry.grid(row=i, column=1)
            self.edited_entry_dictionary[att] = edit_entry

        # Save button
        save_button = tk.Button(refugee_profile_window, text="Save", command=lambda: self.save_details(refugee_profile_window, selected_item))
        save_button.grid(row=len(refugee_details), column=1)

        # Cancel button
        cancel_button = tk.Button(refugee_profile_window, text="Cancel", command=lambda: self.cancel_btn(refugee_profile_window, selected_item))
        cancel_button.grid(row=len(refugee_details)+1, column=1)


    def save_details(self, refugee_profile_window, selected_item):

        try:
            # list comprehension for new edited values
            updated_values = [entry.get() for entry in self.edited_entry_dictionary.values()]

            data = pd.read_csv("volunteer_info.csv")

            selected_id = self.display_volunteer_tree.item(selected_item, 'values')[0]

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
                data.to_csv("volunteer_info.csv", index=False)
                self.display_volunteer_tree.item(selected_item, values=updated_values)

            refugee_profile_window.destroy()
            # CSV data
            csv_file = "volunteer_info.csv"
            # csv_data = self.load_csv_data(csv_file)
            self.upload_csv_data(self.display_volunteer_tree, csv_file)

        except:

            messagebox.showinfo("Data Types", "Please select valid data types to save your edit")

    def cancel_btn(self, edit_plan_window, selected_item):
        edit_plan_window.destroy()
