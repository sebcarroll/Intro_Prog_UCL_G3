import tkinter as tk
from tkinter import ttk, Listbox
from tkinter import messagebox
import csv

class AdminEditVolunteerDetails:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main
        self.volunteer_listbox = None  # To be initialized later

    def create_gui(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        new_plan_frame = tk.Frame(self.window)
        new_plan_frame.grid()

        # Labels
        tk.Label(self.window, text="Admin Edit Volunteer Details", font=('Arial', 40)).grid(row=0, column=0,
                                                                                            columnspan=2,
                                                                                            padx=10, pady=20)
        tk.Label(self.window, text="Select Volunteer:", font=('Arial', 10)).grid(row=1, column=0, columnspan=2,
                                                                                 padx=10, pady=20)

        # Listbox to display volunteer usernames
        self.volunteer_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        self.populate_volunteer_listbox()
        self.volunteer_listbox.grid(row=1, column=1, padx=10, pady=20)

        # Buttons
        tk.Button(self.window, text="Edit Account", command=self.edit_details).grid(row=2,
                                                                                          column=0,
                                                                                          columnspan=2,
                                                                                          pady=10,
                                                                                          ipadx=80,
                                                                                          ipady=25)

        tk.Button(self.window, text="Create Account", command=self.create_account_gui).grid(row=3,
                                                                                            column=0,
                                                                                            columnspan=2,
                                                                                            pady=10,
                                                                                            ipadx=80,
                                                                                            ipady=25)

        tk.Button(self.window, text="Deactivate Account", command=self.deactivate_account).grid(row=4,
                                                                                                column=0,
                                                                                                columnspan=2,
                                                                                                pady=10,
                                                                                                ipadx=80,
                                                                                                ipady=25)
        tk.Button(self.window, text="Reactivate Account", command=self.reactivate_account).grid(row=5,
                                                                                                column=0,
                                                                                                columnspan=2,
                                                                                                pady=10,
                                                                                                ipadx=80,
                                                                                                ipady=25)
        tk.Button(self.window, text="Delete Account", command=self.delete_account).grid(row=6, column=0,
                                                                                        columnspan=2,
                                                                                        pady=10,
                                                                                        ipadx=80,
                                                                                        ipady=25)
        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=17, column=1, padx=5, pady=10)

    def populate_volunteer_listbox(self):
        try:
            with open('volunteer_info.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    username = row['Username']
                    self.volunteer_listbox.insert(tk.END, username)
        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")
    def read_crisis_events_csv(self):
        self.camp_ids_from_csv = []
        try:
            with open('crisis_events.csv', 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    if row[7] == "Active":
                        self.camp_ids_from_csv.append(row[0])
        except FileNotFoundError:
            print("Error: 'crisis_events.csv' file not found.")
        self.camp_ids = self.camp_ids_from_csv

    def create_listbox_with_label(self, widget, text_label, row_num, column_num, list_of_options):
        '''
        Creates a labelled listbox with a scrollbar and binds the selection event to an action.

        :param widget: The window in which the listbox is to be contained.
        :param text_label: The name of the label that you want the list box to have
        :param row_num: The relative position vertically that you want the list box and label to be displayed in.
        :param column_num: The relative position horizontally that you want the list box and label to be displayed in.
        :param list_of_options: The list containing the options available to the user to be selected.
        :return: listbox and scrollbar widgets
        '''
        label = tk.Label(widget, text=text_label)
        label.grid(row=row_num, column=column_num)

        scrollbar = tk.Scrollbar(widget)
        scrollbar.grid(row=row_num, column=column_num + 2, sticky='ns')

        listbox = tk.Listbox(widget, yscrollcommand=scrollbar.set, height=1, exportselection=0)
        listbox.grid(row=row_num, column=column_num + 1)

        scrollbar.config(command=listbox.yview)

        for item in list_of_options:
            listbox.insert(tk.END, item)

        return listbox, scrollbar

    def get_selected_listbox_value(self, event, listbox, list):
        '''
        Returns the selected value within a listbox so that the selected value can be saved as a variable for further use. If no input provided, it will use the first option given in the list of options as a default.
        :param event: A variable that is passed to the function when a binding event takes place.
        :param listbox: The listbox that the value to be saved is coming from.
        :param list: The list of options from which the option is selected. If no option selected, then the first option is selected as default
        :return:
        '''
        print(f"Current listbox selection indices: {listbox.curselection()}")
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_value = listbox.get(selected_indices[0])
            print(f"Selected value: {selected_value}")
            return selected_value
        else:
            default_value = list[0]
            print("No selection made. Using the default value.")
            return default_value

    def create_account_gui(self):
        self.read_crisis_events_csv()
        # Create a new window for creating a new account
        self.create_account_window = tk.Toplevel(self.window)
        self.create_account_window.title("Create New Account")
        self.create_account_window.geometry('800x600')

        # Labels and Entry widgets for user input
        tk.Label(self.create_account_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        username_entry = tk.Entry(self.create_account_window)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.create_account_window, text="Password:").grid(row=3, column=0, padx=10, pady=10)
        password_entry = tk.Entry(self.create_account_window, show="*")
        password_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.create_account_window, text="Name:").grid(row=4, column=0, padx=10, pady=10)
        name_entry = tk.Entry(self.create_account_window)
        name_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.create_account_window, text="Email Address:").grid(row=5, column=0, padx=10, pady=10)
        email_entry = tk.Entry(self.create_account_window)
        email_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self.create_account_window, text="Phone Number:").grid(row=6, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(self.create_account_window)
        phone_entry.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(self.create_account_window, text="Commitment:").grid(row=7, column=0, padx=10, pady=10)
        commitment_entry = ttk.Combobox(self.create_account_window,
                                        values=['Full time', 'Part time', 'Occasional'],
                                        state='readonly')
        commitment_entry.grid(row=7, column=1, padx=10, pady=10)

        tk.Label(self.create_account_window, text="Work Type:").grid(row=8, column=0, padx=10, pady=10)
        work_type_entry = ttk.Combobox(self.create_account_window, values=['Medical Aid', 'Food counselling'])
        work_type_entry.grid(row=8, column=1, padx=10, pady=10)

        camp_id_listbox: Listbox
        self.camp_id_listbox, self.camp_id_scrollbar = self.create_listbox_with_label(self.create_account_window,
                                                                                "Volunteer Camp Assignation:", 1, 0,
                                                                                 self.camp_ids)
        camp_id = self.get_selected_listbox_value(None, self.camp_id_listbox, self.camp_ids)


        # Button to confirm and create the account
        confirm_button = tk.Button(self.create_account_window, text="Create Account",
                                   command=lambda: self.create_account({
                                       'Username': username_entry.get(),
                                       'Camp ID': self.camp_id_listbox.get(self.camp_id_listbox.curselection()),
                                       'Password': password_entry.get(),
                                       'Name': name_entry.get(),
                                       'Email Address': email_entry.get(),
                                       'Phone Number': phone_entry.get(),
                                       'Commitment': commitment_entry.get(),
                                       'Work Type': work_type_entry.get(),
                                       'Deactivated': 'False'
                                   }))

        self.create_account_window.rowconfigure(9, weight=1)
        print("Placing the button on the grid")
        confirm_button.grid(row=9, column=0, columnspan=2, pady=10, ipadx=80, ipady=25, sticky='ew')
        print("Button should be placed now")

    def create_account(self, new_volunteer):
        try:
            with open('volunteer_info.csv', 'a', newline='') as csvfile:
                fieldnames = ['Username', 'Camp ID', 'Password', 'Name', 'Email Address', 'Phone Number', 'Commitment',
                              'Work Type', 'Deactivated']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_volunteer)
            message_label = tk.Label(self.create_account_window, text="")
            submit_button_row = 10
            submit_button_column = 0
            submit_column_span = 2
            message_label.config(text="Values Submitted and Saved. Please return to the home page.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')

        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")

    def edit_details(self):
        self.read_crisis_events_csv()
        selected_index = self.volunteer_listbox.curselection()

        if selected_index:
            # Get the username of the selected volunteer
            username_to_edit = self.volunteer_listbox.get(selected_index)

            # Open the CSV file and find the volunteer's details
            try:
                with open('volunteer_info.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['Username'] == username_to_edit:
                            # Creates a new window for editing details
                            self.edit_details_window = tk.Toplevel(self.window)
                            self.edit_details_window.title("Edit Volunteer Details")

                            # Labels and Entry widgets for user input
                            tk.Label(self.edit_details_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
                            username_entry = tk.Entry(self.edit_details_window)
                            username_entry.insert(0, row['Username'])
                            username_entry.grid(row=0, column=1, padx=10, pady=10)

                            tk.Label(self.edit_details_window, text="Password:").grid(row=3, column=0, padx=10, pady=10)
                            password_entry = tk.Entry(self.edit_details_window, show="*")
                            password_entry.insert(0, row['password'])
                            password_entry.grid(row=3, column=1, padx=10, pady=10)

                            tk.Label(self.edit_details_window, text="Name:").grid(row=4, column=0, padx=10, pady=10)
                            name_entry = tk.Entry(self.edit_details_window)
                            name_entry.insert(0, row['name'])
                            name_entry.grid(row=4, column=1, padx=10, pady=10)

                            tk.Label(self.edit_details_window, text="Email Address:").grid(row=5, column=0, padx=10, pady=10)
                            email_entry = tk.Entry(self.edit_details_window)
                            email_entry.insert(0, row['Email Address'])
                            email_entry.grid(row=5, column=1, padx=10, pady=10)

                            tk.Label(self.edit_details_window, text="Phone Number:").grid(row=6, column=0, padx=10, pady=10)
                            phone_entry = tk.Entry(self.edit_details_window)
                            phone_entry.insert(0, row['Phone Number'])
                            phone_entry.grid(row=6, column=1, padx=10, pady=10)

                            tk.Label(self.edit_details_window, text="Commitment:").grid(row=7, column=0, padx=10, pady=10)
                            commitment_entry = ttk.Combobox(self.edit_details_window,
                                                            values=['Full time', 'Part time', 'Occasional'],
                                                            state='readonly')
                            commitment_entry.set(row['Commitment'])
                            commitment_entry.grid(row=7, column=1, padx=10, pady=10)

                            tk.Label(self.edit_details_window, text="Work Type:").grid(row=8, column=0, padx=10, pady=10)
                            work_type_entry = ttk.Combobox(self.edit_details_window,
                                                           values=['Medical Aid', 'Food counselling'])
                            work_type_entry.set(row['Work Type'])
                            work_type_entry.grid(row=8, column=1, padx=10, pady=10)

                            camp_id_listbox: Listbox
                            self.camp_id_listbox, self.camp_id_scrollbar = self.create_listbox_with_label(
                                self.edit_details_window,
                                "Volunteer Camp Assignation:", 1, 0,
                                self.camp_ids)
                            camp_id = self.get_selected_listbox_value(None, self.camp_id_listbox, self.camp_ids)

                            # Button to confirm and create the account
                            confirm_button = tk.Button(self.edit_details_window, text="Save Changes",
                                                       command=lambda: self.save_changes(
                                                           old_username=username_to_edit,
                                                           updated_details={
                                                               'Username': username_entry.get(),
                                                               'Camp ID': self.camp_id_listbox.get(
                                                                   self.camp_id_listbox.curselection()),
                                                               'Password': password_entry.get(),
                                                               'Name': name_entry.get(),
                                                               'Email Address': email_entry.get(),
                                                               'Phone Number': phone_entry.get(),
                                                               'Commitment': commitment_entry.get(),
                                                               'Work Type': work_type_entry.get(),
                                                               'Deactivated': 'False'
                                                           },
                                                           edit_details_window=self.edit_details_window
                                                       ))

                            confirm_button.grid(row=9, column=0, columnspan=2, pady=10, ipadx=80, ipady=25)

            except FileNotFoundError:
                messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")
    def save_changes(self, old_username, updated_details,edit_details_window):
        try:
            with open('volunteer_info.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                for row in rows:
                    if row['Username'] == old_username:
                        # Update the details with the new values
                        row.update(updated_details)

            with open('volunteer_info.csv', 'w', newline='') as csvfile:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in rows:
                    # Only include fields that match the original fieldnames
                    writer.writerow({fieldname: row[fieldname] for fieldname in fieldnames})

            messagebox.showinfo("Update", f"Details for {old_username} updated successfully.")
            edit_details_window.destroy()
        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")


    def reactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_reactivate = self.volunteer_listbox.get(selected_index)
            self.update_account_status(username_to_reactivate, deactivated=False)
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")

    def deactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_deactivate = self.volunteer_listbox.get(selected_index)
            self.update_account_status(username_to_deactivate, deactivated=True)
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")

    def delete_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_delete = self.volunteer_listbox.get(selected_index)
            self.remove_account(username_to_delete)
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")

    def remove_account(self, username):
        try:
            with open('volunteer_info.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                for row in rows:
                    if row['Username'] == username:
                        rows.remove(row)

            with open('volunteer_info.csv', 'w', newline='') as csvfile:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            messagebox.showinfo("Deletion", f"Account for {username} deleted successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")

    def update_account_status(self, username, deactivated):
        try:
            with open('volunteer_info.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                for row in rows:
                    if row['Username'] == username:
                        if row['Deactivated'] == 'True' and deactivated:
                            messagebox.showinfo("Deactivation", f"Account for {username} is already deactivated.")
                        row['Deactivated'] = str(deactivated).lower()

            with open('volunteer_info.csv', 'w', newline='') as csvfile:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            action = "Deactivation" if deactivated else "Reactivation"
            messagebox.showinfo(action, f"Account for {username} {action.lower()} successful.")
        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")
