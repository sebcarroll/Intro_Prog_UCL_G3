import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
import csv

class RefugeeDisplay:
    def __init__(self, window, back_button_to_volunteer_main, get_camp_id_for_volunteer):
        self.window = window
        self.back_button_to_volunteer_main = back_button_to_volunteer_main
        self.get_camp_id_for_volunteer = get_camp_id_for_volunteer
        self.camp_id = None

    def create_gui_refugee_display(self, window):
        for i in self.window.winfo_children():
            i.grid_forget()
        for i in range(9):
            self.window.grid_columnconfigure(i, weight=1)
        display_refugee_frame = tk.Frame(self.window)
        display_refugee_frame.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
        for i in range(9):
            display_refugee_frame.grid_columnconfigure(i, weight=1)
        for i in range(9):
            display_refugee_frame.grid_rowconfigure(i, weight=1)

        # Labels
        display_refugee_title = tk.Label(display_refugee_frame, text="Display Refugees", font=('TKDefault', 25), fg='white')
        display_refugee_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
        display_refugee_title.configure(background="grey")

        self.display_refugee_tree = ttk.Treeview(display_refugee_frame, height=15)
        self.display_refugee_tree.grid(row=1, column=0, columnspan=9, sticky="ew", padx=10, pady=5)

        # Button Frame:
        btn_frame = tk.Frame(display_refugee_frame)
        btn_frame.grid(row=2, column=4, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # Buttons
        # View event
        view_btn = tk.Button(btn_frame, text="View Refugee Profile", command=lambda: self.view_csv_data_entry())
        view_btn.grid(row=0, column=0, padx=20, pady=(50,10))

        # Edit event
        edit_btn = tk.Button(btn_frame, text="Edit Refugee Profile", command=lambda: self.edit_csv_data_entry())
        edit_btn.grid(row=0, column=1, padx=20, pady=(50,10))

        # Delete button
        delete_btn = tk.Button(btn_frame, text="Delete Refugee Profile", command=lambda: self.delete_csv_data_entry(self.display_refugee_tree, csv_file))
        delete_btn.grid(row=0, column=2, padx=20, pady=(50,10))

        # Back button
        back_button = tk.Button(btn_frame, text='Back to Home', command=self.back_button_to_volunteer_main)
        back_button.grid(row=2, column=1, padx=5, pady=40)

        # CSV data
        csv_file = "refugee_info.csv"
        # csv_data = self.load_csv_data(csv_file)
        self.upload_csv_data(self.display_refugee_tree, csv_file)

    def upload_csv_data(self, tree, filename):

        self.camp_id = self.get_camp_id_for_volunteer()

        data = pd.read_csv(filename)
        data = data[data['Camp ID'] == self.camp_id]

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
        selected_item = self.display_refugee_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a refugee profile to delete")
            return
        if messagebox.askokcancel("Delete Refugee Profile?", "Are you sure you want to delete this refugee profile?\nYou will not be able to recover this refugee profile"):
            selected_item = tree.selection()
            if selected_item:
                # Get the row index of the selected row
                index = int(selected_item[0])

                # Load current CSV data, delete the entry, then save the deletion to the csv
                data = pd.read_csv(filename)
                data = data.drop(index)
                data.to_csv(filename, index=False)

                # Refresh treeview to reflect change
                self.upload_csv_data(tree, filename)

    def view_csv_data_entry(self):
        selected_item = self.display_refugee_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a refugee profile to view")
            return

        refugee_details = self.display_refugee_tree.item(selected_item, 'values')

        # Attributes from the treeview
        column_attributes = self.display_refugee_tree['columns']
        treeview_width = len(column_attributes)

        # Open pop up view window
        refugee_profile_window = tk.Toplevel(self.window)
        refugee_profile_window.title("View Refugee Details")
        refugee_profile_window.grab_set()

        # Create a label and entry for each plan attribute using column attributes by looping over the count of headers in the csv
        for i in range(treeview_width):
            att = column_attributes[i]
            value = refugee_details[i]
            # Attribute label
            label = tk.Label(refugee_profile_window, text=f"{att}:")
            label.grid(row=i, column=0)
            # Data label
            current_camp_info = tk.Label(refugee_profile_window, textvariable=tk.StringVar(refugee_profile_window, value=value))
            current_camp_info.grid(row=i, column=1)

        # Close button
        save_button = tk.Button(refugee_profile_window, text="Close",command=lambda: self.cancel_btn(refugee_profile_window, selected_item))
        save_button.grid(row=len(refugee_details) + 1, column=1)

    def edit_csv_data_entry(self):
        selected_item = self.display_refugee_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select a refugee profile to edit")
            return

        refugee_details = self.display_refugee_tree.item(selected_item, 'values')

        # Attributes from the treeview
        column_attributes = self.display_refugee_tree['columns']
        treeview_width = len(column_attributes)

        # Open pop up edit window
        refugee_profile_window = tk.Toplevel(self.window)
        refugee_profile_window.title("Edit Refugee Details")
        refugee_profile_window.grab_set()
        # Create a dictionary to store new edited info with key as attribute, value as new edited entry
        self.edited_entry_dictionary = {}

        # Get camp IDs available using the function at the end of this file
        self.camp_ids = self.get_camp_ids_from_csv()

        # Create a label and entry for each plan attribute using column attributes by looping over the header count in csv
        for i in range(treeview_width):

            att = column_attributes[i]
            value = refugee_details[i]

            label = tk.Label(refugee_profile_window, text=f"{att}:")
            label.grid(row=i, column=0)

            if att == "Camp ID":
                # Create a dropdown for Camp ID only
                camp_ID_box = ttk.Combobox(refugee_profile_window, values=self.camp_ids, state='readonly')
                camp_ID_box.set(value)  # Set the current value
                camp_ID_box.grid(row=i, column=1)
                self.edited_entry_dictionary[att] = camp_ID_box
            else:
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

            data = pd.read_csv("refugee_info.csv")

            selected_id = self.display_refugee_tree.item(selected_item, 'values')[0]

            if selected_id in data[data.columns[0]].values:
                row_index = data[data[data.columns[0]] == selected_id].index[0]

                # Iterate over each column and convert updated values to the correct type
                for i, col_name in enumerate(data.columns):
                    col_type = data[col_name].dtype

                    # Convert the value to the column's current type so we save similar data per attribute
                    if pd.api.types.is_numeric_dtype(col_type):
                        if updated_values[i] != '':
                            updated_values[i] = col_type.type(updated_values[i])
                        else:
                            updated_values[i] = pd.NA

                data.loc[row_index] = updated_values
                data.to_csv("refugee_info.csv", index=False)
                self.display_refugee_tree.item(selected_item, values=updated_values)

            refugee_profile_window.destroy()
            # csv data
            csv_file = "refugee_info.csv"
            # csv_data = self.load_csv_data(csv_file)
            self.upload_csv_data(self.display_refugee_tree, csv_file)

        except:

            messagebox.showinfo("Data Types", "Please select valid data types to save your edit")

    def cancel_btn(self, edit_plan_window, selected_item):
        edit_plan_window.destroy()

    def get_camp_ids_from_csv(self):
        camp_ids = []
        try:
            with open('crisis_events.csv', 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    if row[7] == "Active":
                        camp_ids.append(row[0])
        except FileNotFoundError:
            messagebox.showinfo("File not found",
                                "The file 'crisis_events.csv' was not found.\n\nYou will not be able to change to another camp ID")
            #print("Error: 'crisis_events.csv' file not found.")
        return camp_ids