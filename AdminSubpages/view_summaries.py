import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
from general_functions import validate_data, cast_data
import csv


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
        end_plan_frame.grid_rowconfigure(1, weight=3)
        end_plan_frame.grid_rowconfigure(2, weight=1)

        # Labels
        end_plan_title = tk.Label(end_plan_frame, text="View Plan Summaries", font=('Helvetica', 16))
        end_plan_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5)

        self.end_plan_tree = ttk.Treeview(end_plan_frame, height=20)
        self.end_plan_tree.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Button Frame:
        btn_frame = tk.Frame(end_plan_frame)
        btn_frame.grid(row=2, column=0, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # Buttons
        # View event
        edit_event_btn = tk.Button(btn_frame, text="View Event", command=lambda: self.view_csv_data_entry())
        edit_event_btn.grid(row=0, column=0, padx=20, pady=(50,10))

        # Edit event
        edit_event_btn = tk.Button(btn_frame, text="Edit Event", command=lambda: self.edit_csv_data_entry())
        edit_event_btn.grid(row=0, column=1, padx=20, pady=(50,10))

        # Delete button
        delete_btn = tk.Button(btn_frame, text="Delete Event", command=lambda: self.delete_csv_data_entry(self.end_plan_tree, csv_file))
        delete_btn.grid(row=0, column=2, padx=20, pady=(50,10))

        # Back button
        back_button = tk.Button(btn_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=2, column=1, padx=5, pady=40)



        # CSV data
        csv_file = "crisis_events.csv"
        # csv_data = self.load_csv_data(csv_file)
        self.upload_csv_data(self.end_plan_tree, csv_file)

        # pie chart
        self.create_pie_chart()
        self.create_pie_chart_crisis_type()



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

    def view_csv_data_entry(self):
        selected_item = self.end_plan_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a plan to view")
            return

        plan_details = self.end_plan_tree.item(selected_item, 'values')

        # Attributes from the treeview
        column_attributes = self.end_plan_tree['columns']
        treeview_width = len(column_attributes)

        # Open pop up edit window
        view_plan_window = tk.Toplevel(self.window)
        view_plan_window.title("View Plan")

        # Create a label and entry for each plan attribute using column attributes
        for i in range(treeview_width):
            att = column_attributes[i]
            value = plan_details[i]

            label = tk.Label(view_plan_window, text=f"{att}:")
            label.grid(row=i, column=0)

            current_camp_info = tk.Label(view_plan_window, textvariable=tk.StringVar(view_plan_window, value=value))
            current_camp_info.grid(row=i, column=1)

        # Close button
        save_button = tk.Button(view_plan_window, text="Close",command=lambda: self.cancel_btn(view_plan_window, selected_item))
        save_button.grid(row=len(plan_details) + 1, column=1)

    def create_pie_chart(self):
        # Read data from CSV file
        active_count = 0
        inactive_count = 0

        with open('crisis_events.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                status = row['Status']
                if status.lower() == 'active':
                    active_count += 1
                elif status.lower() == 'inactive':
                    inactive_count += 1

        # Calculate percentage
        total = active_count + inactive_count
        active_percentage = (active_count / total) * 360
        inactive_percentage = (inactive_count / total) * 360

        # Create a pie chart using canvas
        canvas = tk.Canvas(self.window, width=200, height=200)
        canvas.grid(row=15, column=10)

        # Draw active slice
        canvas.create_arc(50, 50, 150, 150, start=0, extent=active_percentage, fill='green', outline='white')
        # Draw inactive slice
        canvas.create_arc(50, 50, 150, 150, start=active_percentage, extent=inactive_percentage, fill='red',
                          outline='white')

        # Add legend (key)
        legend_labels = ['Active Crisis', 'Inactive Crisis']
        legend_colors = ['green', 'red']

        for i, label in enumerate(legend_labels):
            # Draw legend rectangle
            canvas.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=legend_colors[i], outline='white')
            # Draw legend label
            canvas.create_text(40, 20 + i * 20, text=label, anchor=tk.W, fill='white')

    def create_pie_chart_crisis_type(self):
        # Read data from CSV file
        war_count = 0
        environmental_count = 0
        supply_shortage_count = 0
        political_unrest_count = 0
        displacement_count = 0
        other_count = 0

        with open('crisis_events.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                status = row['Crisis Type']
                if status.lower() == 'war':
                    war_count += 1
                elif status.lower() == 'environmental':
                    environmental_count += 1
                elif status.lower() == 'political unrest':
                    political_unrest_count += 1
                elif status.lower() == 'displacement':
                    displacement_count += 1
                elif status.lower() == 'supply shortage':
                    supply_shortage_count += 1
                elif status.lower() == 'other':
                    other_count += 1

        # Calculate percentage
        total = war_count + environmental_count + supply_shortage_count + political_unrest_count + displacement_count + other_count
        war_percentage = (war_count / total) * 360
        environmental_percentage = (environmental_count/ total) * 360
        supply_shortage_percentage = (supply_shortage_count/ total) * 360
        political_unrest_percentage = (political_unrest_count/ total) * 360
        displacement_percentage = (displacement_count / total) * 360
        other_percentage = (other_count/ total) * 360

        # Create a pie chart using canvas
        canvas = tk.Canvas(self.window, width=200, height=200)
        canvas.grid(row=15, column=1)

        # Draw slices  of pie chart

        canvas.create_arc(50, 50, 150, 150, start=0, extent=war_percentage, fill='red', outline='white')
        canvas.create_arc(50, 50, 150, 150, start=war_percentage, extent=environmental_percentage, fill='blue', outline='white')
        canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage, extent=supply_shortage_percentage, fill='green', outline='white')
        canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage, extent=political_unrest_percentage, fill='yellow', outline='white')
        canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage + political_unrest_percentage, extent=displacement_percentage, fill='purple', outline='white')
        canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage + political_unrest_percentage + displacement_percentage, extent=other_percentage, fill='orange', outline='white')

        # canvas_legend = tk.Canvas(self.window, width=100, height=150)
        # canvas_legend.grid(row=, column=5)
        # Add legend (key)
        legend_labels = ['War', 'Environmental', 'Supply Shortage', 'Political Unrest', 'Displacement', 'Other']
        legend_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']


        for i, label in enumerate(legend_labels):
            # Draw legend rectangle
            canvas.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=legend_colors[i], outline='white')
            # Draw legend label
            canvas.create_text(40, 20 + i * 20, text=label, anchor=tk.W, fill='white')




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

                    label = tk.Label(edit_plan_window, text=f"{att}:    ")
                    label.grid(row=i, column=0)

                    edit_entry = tk.Entry(edit_plan_window, textvariable=tk.StringVar(edit_plan_window, value=value))
                    edit_entry.grid(row=i, column=1)
                    self.edited_entry_dictionary[att] = edit_entry

                # Save button
                save_button = tk.Button(edit_plan_window, text="Save", command=lambda: self.save_plan(edit_plan_window, selected_item))
                save_button.grid(row=len(plan_details), column=1, pady=3)

                # Cancel button
                save_button = tk.Button(edit_plan_window, text="Cancel", command=lambda: self.cancel_btn(edit_plan_window, selected_item))
                save_button.grid(row=len(plan_details)+1, column=1, pady=3)


    def save_plan(self, edit_plan_window, selected_item):

        try:
            # list comprehension for new edited values
            updated_values = [entry.get() for entry in self.edited_entry_dictionary.values()]

            data = pd.read_csv("crisis_events.csv")

            selected_id = int(self.end_plan_tree.item(selected_item, 'values')[0])

            if selected_id in data[data.columns[0]].values:
                row_index = data[data[data.columns[0]] == selected_id].index[0]

                # Validate and convert data using the validate function in general functions file
                #validated_values = validate_and_convert_data(updated_values, data, row_index)

                validated_values = validate_data(updated_values, data, row_index)
                casted_values = cast_data(validated_values, data)

                # start of new code for saving data:
                """for i, col_name in enumerate(data.columns):
                    updated_value = updated_values[i]

                    # Check if the input field is not empty
                    if updated_value != '':
                        # Determine the column data type in the DataFrame
                        col_type = data[col_name].dtype

                        # Check if the column is of integer type
                        if col_type == 'int64':
                            if updated_value.isdigit():
                                # Convert to integer if input is a digit
                                updated_values[i] = int(updated_value)
                            else:
                                # If input is not a digit, retain the original value
                                updated_values[i] = data.at[row_index, col_name]

                        # Check if the column is of float type
                        elif col_type == 'float64':
                            try:
                                # Try converting to float
                                updated_values[i] = float(updated_value)
                            except ValueError:
                                # If input is not a valid float, retain the original value
                                updated_values[i] = data.at[row_index, col_name]

                        # For string or other types, keep the new value as it is
                        else:
                            updated_values[i] = updated_value

                    # If the input field is empty, retain the original value
                    else:
                        updated_values[i] = data.at[row_index, col_name]"""

                # Iterate over each column and convert updated values to the correct type
                '''for i, col_att in enumerate(data.columns):
                    col_type = data[col_att].dtype

                    # Convert the value to the column's type
                    if pd.api.types.is_numeric_dtype(col_type):
                        if updated_values[i] != '':
                            updated_values[i] = col_type.type(updated_values[i])
                        else:
                            updated_values[i] = pd.NA'''

                '''data.loc[row_index] = updated_values
                data.to_csv("crisis_events.csv", index=False)
                self.end_plan_tree.item(selected_item, values=updated_values)'''

                '''data.loc[row_index] = validated_values
                data.to_csv("crisis_events.csv", index=False)
                self.end_plan_tree.item(selected_item, values=validated_values)'''

                data.loc[row_index] = casted_values
                data.to_csv("crisis_events.csv", index=False)
                self.end_plan_tree.item(selected_item, values=casted_values)


            edit_plan_window.destroy()
            # CSV data
            csv_file = "crisis_events.csv"
            # csv_data = self.load_csv_data(csv_file)
            self.upload_csv_data(self.end_plan_tree, csv_file)

        except:

            messagebox.showinfo("Data Types", "Please select valid data types to save your edit")






    def cancel_btn(self, edit_plan_window, selected_item):
        edit_plan_window.destroy()
