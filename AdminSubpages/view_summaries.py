import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
from general_functions import validate_data
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

        self.end_plan_tree = ttk.Treeview(end_plan_frame, height=15)
        self.end_plan_tree.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Horizontal scrollbar
        xscrollbar = ttk.Scrollbar(end_plan_frame, orient='horizontal', command=self.end_plan_tree.xview)
        xscrollbar.grid(row=2, column=0, sticky='ew', columnspan=2)
        self.end_plan_tree.configure(xscrollcommand=xscrollbar.set)

        # Button Frame:
        btn_frame = tk.Frame(end_plan_frame)
        btn_frame.grid(row=3, column=0, pady=10)
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

        # View data button
        generate_data_btn = tk.Button(btn_frame, text="Generate Charts", command=lambda: self.generate_charts_window())
        generate_data_btn.grid(row=0, column=3, padx=20, pady=(50,10))

        # Back button
        back_button = tk.Button(btn_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=2, column=1, columnspan=2, padx=5, pady=40)


        # CSV data
        csv_file = "crisis_events.csv"
        self.upload_csv_data(self.end_plan_tree, csv_file)
        # csv_data = self.load_csv_data(csv_file)
        try:
            self.upload_csv_data(self.end_plan_tree, csv_file)
        except:
            messagebox.showwarning("No data found",
                                   "There is a problem accessing the database\n\nThe file may be missing or corrupted")

    def generate_charts_window(self):
        # Create a new window for the pie chart
        generate_charts_window = tk.Toplevel(self.window)
        generate_charts_window.title("View charts")
        generate_charts_window.geometry("800x400")

        # Call the method to create the pie chart in the new window
        self.create_pie_chart_status(generate_charts_window)
        self.create_bar_chart_crisis_type(generate_charts_window)

    def create_pie_chart_status(self, window):
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
        canvas = tk.Canvas(window, width=200, height=200)
        # canvas.grid(row=17, column=0, padx=10, pady=5)
        canvas.pack()

        # Create a canvas for the pie chart labels
        canvas_legend_pie = tk.Canvas(window, width=200, height=200)
        canvas_legend_pie.place(x=50,y=75)

        # Draw active slice
        canvas.create_arc(50, 50, 150, 150, start=0, extent=active_percentage, fill='green', outline='white')
        # Draw inactive slice
        canvas.create_arc(50, 50, 150, 150, start=active_percentage, extent=inactive_percentage, fill='red',
                          outline='white')

        # Add legend (key)
        legend_labels_crisis_status = ['Active Crisis', 'Inactive Crisis']
        legend_colors_crisis_status = ['green', 'red']

        for i, label in enumerate(legend_labels_crisis_status):
            # Draw legend rectangle
            canvas_legend_pie.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=legend_colors_crisis_status[i], outline='white')
            # Draw legend label
            canvas_legend_pie.create_text(40, 20 + i * 20, text=label, anchor=tk.W, fill='black')

    def create_bar_chart_crisis_type(self, window):
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

        # Calculate total count
        total = war_count + environmental_count + supply_shortage_count + political_unrest_count + displacement_count + other_count


        # # Calculate percentage
        # total = war_count + environmental_count + supply_shortage_count + political_unrest_count + displacement_count + other_count
        # war_percentage = (war_count / total) * 360
        # environmental_percentage = (environmental_count / total) * 360
        # supply_shortage_percentage = (supply_shortage_count / total) * 360
        # political_unrest_percentage = (political_unrest_count / total) * 360
        # displacement_percentage = (displacement_count / total) * 360
        # other_percentage = (other_count / total) * 360

        # Create a bar chart using canvas
        canvas = tk.Canvas(window, width=400, height=200)
        canvas.pack()

        # Create a canvas for the bar chart labels
        canvas_legend_bar = tk.Canvas(window, width=200, height=200)
        canvas_legend_bar.place(x=50,y=225)

        # Define bar width and gap
        bar_width = 40
        gap = 20

        # Calculate the x-coordinates for each bar
        x_war = 50
        x_environmental = x_war + bar_width + gap
        x_supply_shortage = x_environmental + bar_width + gap
        x_political_unrest = x_supply_shortage + bar_width + gap
        x_displacement = x_political_unrest + bar_width + gap
        x_other = x_displacement + bar_width + gap

        # Calculate the heights of each bar
        height_factor = 100  # You can adjust this factor to control the height of the bars
        height_war = war_count * height_factor / total
        height_environmental = environmental_count * height_factor / total
        height_supply_shortage = supply_shortage_count * height_factor / total
        height_political_unrest = political_unrest_count * height_factor / total
        height_displacement = displacement_count * height_factor / total
        height_other = other_count * height_factor / total

        # Draw rectangles for each bar
        canvas.create_rectangle(x_war, 150 - height_war, x_war + bar_width, 150, fill='red', outline='white')
        canvas.create_rectangle(x_environmental, 150 - height_environmental, x_environmental + bar_width, 150, fill='blue', outline='white')
        canvas.create_rectangle(x_supply_shortage, 150 - height_supply_shortage, x_supply_shortage + bar_width, 150, fill='green', outline='white')
        canvas.create_rectangle(x_political_unrest, 150 - height_political_unrest, x_political_unrest + bar_width, 150, fill='yellow', outline='white')
        canvas.create_rectangle(x_displacement, 150 - height_displacement, x_displacement + bar_width, 150, fill='purple', outline='white')
        canvas.create_rectangle(x_other, 150 - height_other, x_other + bar_width, 150, fill='orange', outline='white')

        # # Draw slices of the pie chart
        # canvas.create_arc(50, 50, 150, 150, start=0, extent=war_percentage, fill='red', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage, extent=environmental_percentage, fill='blue', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage, extent=supply_shortage_percentage, fill='green', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage, extent=political_unrest_percentage, fill='yellow', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage + political_unrest_percentage, extent=displacement_percentage, fill='purple', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage + political_unrest_percentage + displacement_percentage, extent=other_percentage, fill='orange', outline='white')

        # Add legend (key)
        legend_labels_crisis_type = ['War', 'Environmental', 'Supply Shortage', 'Political Unrest', 'Displacement', 'Other']
        legend_colors_crisis_type = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

        for i, label in enumerate(legend_labels_crisis_type):
            # Draw legend rectangle
            canvas_legend_bar.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=legend_colors_crisis_type[i], outline='white')
            # Draw legend label
            canvas_legend_bar.create_text(40, 20 + i * 20, text=label, anchor=tk.W, fill='black')

    def upload_csv_data(self, tree, filename):
        data = pd.read_csv(filename)

        # Convert 'Camp ID' to integer, handling missing or non-integer values
        data['Camp ID'] = pd.to_numeric(data['Camp ID'], errors='coerce').fillna(0).astype('int64')
        #print(data['Camp ID'])

        volunteer_counts = self.volunteer_camp_count()
        #print("Volunteer counts from method:", volunteer_counts)

        # Ensure volunteer_counts is a Series and perform mapping
        if isinstance(volunteer_counts, pd.Series):
            data['Volunteers'] = data['Camp ID'].map(volunteer_counts).fillna(0).astype('int64')
            #print(data['Volunteer Count'])
        else:
            data['Volunteers'] = 0

        # The following block will convert floats to integers for the GUI to remove the ".0"
        # columns with float numbers
        float_columns = data.select_dtypes(include=['float']).columns
        # Convert floats to integers for display in treeview
        for col in float_columns:
            data[col] = data[col].fillna(0).astype('int64')

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

                # VALIDATE data using the validate function in general functions file
                validated_values = validate_data(updated_values, data, row_index)

                # CASTING to correct data type for the column
                for i, col_att in enumerate(data.columns):
                    col_type = data[col_att].dtype

                    # Convert the value to the column's type
                    if pd.api.types.is_numeric_dtype(col_type):
                        if validated_values[i] != '':
                            validated_values[i] = col_type.type(validated_values[i])
                        else:
                            validated_values[i] = pd.NA

                data.loc[row_index] = validated_values
                data.to_csv("crisis_events.csv", index=False)
                self.end_plan_tree.item(selected_item, values=validated_values)

            edit_plan_window.destroy()
            # CSV data
            csv_file = "crisis_events.csv"
            # csv_data = self.load_csv_data(csv_file)
            self.upload_csv_data(self.end_plan_tree, csv_file)

        except:
            messagebox.showinfo("Data Types", "Please select valid data types to save your edit")


    def volunteer_camp_count(self):
        try:
            volunteer_info_df = pd.read_csv("volunteer_info.csv")
            # Convert 'Camp ID' to integer
            volunteer_info_df['Camp ID'] = pd.to_numeric(volunteer_info_df['Camp ID'], errors='coerce').fillna(0).astype('int64')
            #print(volunteer_info_df['Camp ID'].value_counts())
            return volunteer_info_df['Camp ID'].value_counts()
        except Exception as e:
            #messagebox.showwarning("Error", f"Error in processing volunteer_info.csv: {e}")
            messagebox.showwarning("No data found",
                                   "There is a problem accessing the database\n\nThe file may be missing or corrupted")
            return pd.Series()

    def cancel_btn(self, edit_plan_window, selected_item):
        edit_plan_window.destroy()
