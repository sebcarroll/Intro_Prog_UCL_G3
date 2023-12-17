import tkinter as tk
from tkinter import ttk, Listbox
from tkinter import messagebox
import csv
import pandas as pd
import re
class invalid_email(Exception):
    pass
class invalid_phone_number(Exception):
    pass
class invalid_name(Exception):
    pass
class AdminEditVolunteerDetails(invalid_email, invalid_name, invalid_phone_number):
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main
        self.volunteer_listbox = None  # To be initialized later
    # def read_crisis_events_csv(self):
    #     self.camp_ids_from_csv = []
    #     try:
    #         with open('crisis_events.csv', 'r') as file:
    #             csv_reader = csv.reader(file)
    #             next(csv_reader)
    #             for row in csv_reader:
    #                 if row[7] == "Active":
    #                     self.camp_ids_from_csv.append(row[0])
    #     except FileNotFoundError:
    #         print("Error: 'crisis_events.csv' file not found.")
    #     self.camp_ids = list(self.camp_ids_from_csv)

    def upload_csv_data(self, tree, filename):
        data = pd.read_csv(filename, dtype={'Phone Number': str})

        data['Phone Number'] = data['Phone Number'].astype(str)

        # The following block will convert floats to integers for the GUI to remove the ".0"
        # columns with float numbers
        float_columns = data.select_dtypes(include=['float']).columns
        # Convert floats to integers for display in treeview
        for col in float_columns:
            data[col] = data[col].fillna(0).astype(int)
        columns_to_display = [col for col in data.columns if col != "Deleted"]
        tree.delete(*tree.get_children())
        tree['columns'] = columns_to_display
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        for col in columns_to_display:
            tree.column(col, anchor=tk.CENTER, width=80)
            tree.heading(col, text=col, anchor=tk.CENTER)

        for index, row in data.iterrows():
            tree.insert("", tk.END, values=list(row), iid=str(index))

    def create_gui(self, window):
        # Main frame for this whole page
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

        '''display_volunteer_frame = tk.Frame(self.window)
        display_volunteer_frame.grid(sticky="nsew", padx=5, pady=5, columnspan=9)
        for i in range(9):
            display_volunteer_frame.grid_columnconfigure(i, weight=1)'''

        # Labels
        volunteer_title = tk.Label(display_volunteer_frame, text="Edit Volunteer Details", font=('TKDefault', 25), fg='white')
        volunteer_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
        volunteer_title.configure(background="grey")

        # Listbox to display volunteer usernames
        # edit_details_labelFrame = tk.LabelFrame(self.window)
        # edit_details_labelFrame.grid(row=1, column=0)
        # self.volunteer_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        # self.populate_volunteer_listbox()
        # self.volunteer_listbox.grid(row=1, column=0, pady=5)
        #display_volunteer_frame = tk.Frame(self.window)
        #display_volunteer_frame.grid(sticky="nsew", padx=5, pady=5)
        #display_volunteer_frame.grid_columnconfigure(0, weight=1)
        #display_volunteer_frame.grid_rowconfigure(1, weight=3)
        #display_volunteer_frame.grid_rowconfigure(2, weight=1)


        self.display_volunteer_tree = ttk.Treeview(display_volunteer_frame, height=10)
        self.display_volunteer_tree.grid(row=1, column=0, columnspan=9, sticky="ew", padx=10, pady=5)

        # Button Frame:
        btn_frame = tk.Frame(display_volunteer_frame)
        btn_frame.grid(row=2, column=4, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # Buttons
        tk.Button(btn_frame, text="Edit Account", command=self.edit_details, width=20).grid(row=0,
                                                                                          column=0, padx=10, pady=5)

        tk.Button(btn_frame, text="Create Account", command=self.create_account_gui, width=20).grid(row=1,
                                                                                            column=0, padx=10, pady=5)

        tk.Button(btn_frame, text="Deactivate Account", command=self.deactivate_account, width=20).grid(row=2,
                                                                                                column=0, padx=10, pady=5)
        tk.Button(btn_frame, text="Reactivate Account", command=self.reactivate_account, width=20).grid(row=3,
                                                                                                column=0, padx=10, pady=5)
        tk.Button(btn_frame, text="Delete Account", command=self.delete_account, width=20).grid(row=4, column=0,
                                                                                        padx=10, pady=5)
        # Back button
        back_button = tk.Button(btn_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=5, column=0, padx=5, pady=10)

        # for i in range(9):
        #     self.window.grid_rowconfigure(i, weight=1)
        # self.window.grid_columnconfigure(0, weight=1)

    # def populate_volunteer_listbox(self):
    #     try:
    #         with open('volunteer_info.csv', 'r', newline='') as csvfile:
    #             reader = csv.DictReader(csvfile)
    #             for row in reader:
    #                 username = row['Username']
    #                 self.volunteer_listbox.insert(tk.END, username)
    #     except FileNotFoundError:
    #         messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")
        csv_file = 'volunteer_info.csv'
        try:
            self.upload_csv_data(self.display_volunteer_tree, csv_file)
        except:
            headers = ["Username", "Camp ID", "password", "name", "Email Address", "Phone Number", "Commitment",
                       "Work Type", "Deactivated", "Deleted"]
            empty_df = pd.DataFrame(columns=headers)
            empty_df.to_csv(csv_file, index=False)
            messagebox.showinfo("File Created", "A new file was created as 'volunteer_info.csv' was not found.")
            self.upload_csv_data(self.display_volunteer_tree, csv_file)

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

    # def create_listbox_with_label(self, widget, text_label, row_num, column_num, list_of_options):
    #     '''
    #     Creates a labelled listbox with a scrollbar and binds the selection event to an action.
    #
    #     :param widget: The window in which the listbox is to be contained.
    #     :param text_label: The name of the label that you want the list box to have
    #     :param row_num: The relative position vertically that you want the list box and label to be displayed in.
    #     :param column_num: The relative position horizontally that you want the list box and label to be displayed in.
    #     :param list_of_options: The list containing the options available to the user to be selected.
    #     :return: listbox and scrollbar widgets
    #     '''
    #     label = tk.Label(widget, text=text_label)
    #     label.grid(row=row_num, column=column_num)
    #
    #     scrollbar = tk.Scrollbar(widget)
    #     scrollbar.grid(row=row_num, column=column_num + 2, sticky='ns')
    #
    #     listbox = tk.Listbox(widget, yscrollcommand=scrollbar.set, height=1, exportselection=0)
    #     listbox.grid(row=row_num, column=column_num + 1)
    #
    #     scrollbar.config(command=listbox.yview)
    #
    #     for item in list_of_options:
    #         listbox.insert(tk.END, item)
    #
    #     return listbox, scrollbar

    # def get_selected_listbox_value(self, event, listbox, list):
    #     '''
    #     Returns the selected value within a listbox so that the selected value can be saved as a variable for further use. If no input provided, it will use the first option given in the list of options as a default.
    #     :param event: A variable that is passed to the function when a binding event takes place.
    #     :param listbox: The listbox that the value to be saved is coming from.
    #     :param list: The list of options from which the option is selected. If no option selected, then the first option is selected as default
    #     :return:
    #     '''
    #     print(f"Current listbox selection indices: {listbox.curselection()}")
    #     selected_indices = listbox.curselection()
    #     if selected_indices:
    #         selected_value = listbox.get(selected_indices[0])
    #         print(f"Selected value: {selected_value}")
    #         return selected_value
    #     elif list:
    #         default_value = list[0]
    #         print("No selection made. Using the default value.")
    #         return default_value
    #     else:
    #         print("The list is empty. No default value can be used.")
    #         return None
    def create_account_gui(self):
        self.read_crisis_events_csv()
        # Create a new window for creating a new account
        self.create_account_window = tk.Toplevel(self.window)
        self.create_account_window.title("Create New Account")
        self.create_account_window.grab_set()

        # Labels and Entry widgets for user input
        tk.Label(self.create_account_window, text="Username:").grid(row=1, column=0, padx=10, pady=10)
        username_entry = tk.Entry(self.create_account_window)
        username_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.create_account_window, text="Password:").grid(row=2, column=0, padx=10, pady=10)
        password_entry = tk.Entry(self.create_account_window, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=10)

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
        work_type_entry = ttk.Combobox(self.create_account_window, values=['Medical Aid', 'Food counselling'], state='readonly')
        work_type_entry.grid(row=8, column=1, padx=10, pady=10)

        camp_ID_label = tk.Label(self.create_account_window, text='Camp ID: ' )
        camp_ID_label.grid(row=3, column= 0, padx=10, pady=10)
        camp_ID_box = ttk.Combobox(self.create_account_window, values= self.camp_ids, state='readonly')
        camp_ID_box.grid(row=3, column=1, padx=10, pady=10)


        # Button to confirm and create the account
        confirm_button = tk.Button(self.create_account_window, text="Create Account",
                                   command=lambda: self.create_account({
                                       'Username': username_entry.get(),
                                       'Camp ID': camp_ID_box.get(),
                                       'password': password_entry.get(),
                                       'name': name_entry.get(),
                                       'Email Address': email_entry.get(),
                                       'Phone Number': phone_entry.get(),
                                       'Commitment': commitment_entry.get(),
                                       'Work Type': work_type_entry.get(),
                                       'Deactivated': 'False'
                                   }))

        confirm_button.grid(row=9, column=0,columnspan=2, pady=10, ipadx=20, ipady=15)
        for i in range(10):
            self.create_account_window.grid_rowconfigure(i, weight=1)
        self.create_account_window.grid_columnconfigure(0, weight=1)

    def create_account(self, new_volunteer):

        username_check = new_volunteer['Username']
        password_check = new_volunteer['password']
        name_check = new_volunteer['name']
        email_check = new_volunteer['Email Address']
        phone_check = new_volunteer['Phone Number']

        if name_check.isalpha() == False:
            raise invalid_name

        if not (email_check and re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',
                                        email_check)):
            raise invalid_email

        if not re.search(r'^[0-9]+', str(phone_check)):
            raise invalid_phone_number



        if self.username_exists(username_check):
            tk.messagebox.showerror("Error",f"Username '{username_check}' already exists. Please choose a different username.")
            return

        if not username_check:
            tk.messagebox.showerror("Error", "Username must be filled in")
            return

        if not password_check:
            tk.messagebox.showerror("Error", "Password must be filled in")
            return




        try:
            with open('volunteer_info.csv', 'a', newline='') as csvfile:
                fieldnames = ['Username', 'Camp ID', 'password', 'name', 'Email Address', 'Phone Number', 'Commitment',
                              'Work Type', 'Deactivated']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_volunteer)
            message_label = tk.Label(self.create_account_window, text="")
            submit_button_row = 10
            submit_button_column = 0
            submit_column_span = 2
            username = new_volunteer['Name']
            # message_label.config(text="Values Submitted and Saved. Please return to the home page.")
            # message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
            #                    sticky='W')
            tk.messagebox.showinfo(title='Details Saved', message=f"Details for {username} successfully created.")
            self.create_account_window.destroy()
            self.upload_csv_data(self.display_volunteer_tree, 'volunteer_info.csv')

        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")

    def username_exists(self, username):
        try:
            with open('volunteer_info.csv', 'r', newline = '')as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row ['Username']==username:
                        return True
        except FileNotFoundError:
            tk.messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")
        return False



    def edit_details(self):
        self.read_crisis_events_csv()
        selected_index = self.display_volunteer_tree.focus()

        if selected_index:
            # Get the username of the selected volunteer
            item_values = self.display_volunteer_tree.item(selected_index, 'values')
            username_to_edit = item_values[0]

            # Open the CSV file and find the volunteer's details
            try:
                with open('volunteer_info.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['Username'] == username_to_edit:
                            # Creates a new window for editing details
                            self.edit_details_window = tk.Toplevel(self.window)
                            self.edit_details_window.title("Edit Volunteer Details")
                            self.edit_details_window.grab_set()

                            # Labels and Entry widgets for user input
                            tk.Label(self.edit_details_window, text="Username:").grid(row=1, column=0, padx=10, pady=10)
                            username_entry = tk.Entry(self.edit_details_window)
                            username_entry.insert(0, row['Username'])
                            username_entry.grid(row=1, column=1, padx=10, pady=10)

                            tk.Label(self.edit_details_window, text="Password:").grid(row=2, column=0, padx=10, pady=10)
                            password_entry = tk.Entry(self.edit_details_window, show="*")
                            password_entry.insert(0, row['password'])
                            password_entry.grid(row=2, column=1, padx=10, pady=10)

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
                                                           values=['Medical Aid', 'Food counselling'], state='readonly')
                            work_type_entry.set(row['Work Type'])
                            work_type_entry.grid(row=8, column=1, padx=10, pady=10)

                            # camp_id_listbox: Listbox
                            # self.camp_id_listbox, self.camp_id_scrollbar = self.create_listbox_with_label(
                            #     self.edit_details_window,
                            #     "Volunteer Camp Assignation:", 1, 0,
                            #     self.camp_ids)
                            # self.camp_id = self.get_selected_listbox_value(None, self.camp_id_listbox, self.camp_ids)
                            camp_ID_label = tk.Label(self.edit_details_window, text="Camp ID:")
                            camp_ID_label.grid(row=3, column=0, padx=10, pady=10)
                            Camp_ID_box = ttk.Combobox(self.edit_details_window, values=self.camp_ids, state='readonly')
                            Camp_ID_box.set(row['Camp ID'])
                            Camp_ID_box.grid(row=3, column=1, padx=10, pady=10)

                            # Button to confirm and create the account
                            confirm_button = tk.Button(self.edit_details_window, text="Save Changes",
                                                       command=lambda: self.save_changes(
                                                           old_username=username_to_edit,
                                                           updated_details={
                                                               'Username': username_entry.get(),
                                                               'Camp ID': Camp_ID_box.get(),
                                                               'password': password_entry.get(),
                                                               'name': name_entry.get(),
                                                               'Email Address': email_entry.get(),
                                                               'Phone Number': phone_entry.get(),
                                                               'Commitment': commitment_entry.get(),
                                                               'Work Type': work_type_entry.get(),
                                                               'Deactivated': 'False'
                                                           },
                                                           edit_details_window=self.edit_details_window
                                                       ))

                            confirm_button.grid(row=9, column=0, columnspan=2, pady=10, ipadx=20, ipady=15)
                            for i in range(10):
                                self.edit_details_window.grid_rowconfigure(i, weight=1)
                            self.edit_details_window.grid_columnconfigure(0, weight=1)

            except FileNotFoundError:
                messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")
    def save_changes(self, old_username, updated_details,edit_details_window):

        new_username = updated_details['Username']
        new_password = updated_details['password']
        new_name = updated_details['name']
        new_email = updated_details['Email Address']
        new_phone = updated_details['Phone Number']

        try:

            if new_name.isalpha() == False:
                raise invalid_name

            if not (new_email and re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', new_email)):
                raise invalid_email


            if not re.search(r'^[0-9]+', str(new_phone)):
                raise invalid_phone_number



            if new_username != old_username and self.username_exists(new_username):
                tk.messagebox.showerror("Error", f"Username '{new_username}' already exists. Please choose a different username.")
                return

            if not new_username:
                tk.messagebox.showerror("Error", "Username must be filled in")
                return

            if not new_password:
                tk.messagebox.showerror("Error", "Password must be filled in")
                return

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

            tk.messagebox.showinfo("Update", f"Details for {old_username} updated successfully.")
            edit_details_window.destroy()
            self.upload_csv_data(self.display_volunteer_tree, 'volunteer_info.csv')

        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")
        except(invalid_name):
            tk.messagebox.showinfo(title='Invalid Name', message='Please enter a valid name')

        except(invalid_email):
            tk.messagebox.showinfo(title='Invalid Email', message='Please enter a valid email address')
        except(invalid_phone_number):
            tk.messagebox.showinfo(title='Invalid Phone Number', message='Please enter a valid phone number')






    def reactivate_account(self):
        selected_index = self.display_volunteer_tree.focus()
        if selected_index:
            username_to_reactivate = self.display_volunteer_tree.item(selected_index, 'values')[0]
            confirm_reactivate = messagebox.askokcancel('Confirmation', f"Are you sure you want to reactivate account for '{username_to_reactivate}'?")
            if confirm_reactivate:
                self.update_account_status(username_to_reactivate, deactivated=False)
                #tk.messagebox.showinfo(f"Account for f'{username_to_reactivate}' reactivated successfully")
                self.upload_csv_data(self.display_volunteer_tree, 'volunteer_info.csv')
        else:
            tk.messagebox.showwarning("No Selection", "Please select a volunteer.")

    def deactivate_account(self):
        selected_index = self.display_volunteer_tree.focus()
        if selected_index:
            username_to_deactivate = self.display_volunteer_tree.item(selected_index, 'values')[0]
            confirm_deactivate = tk.messagebox.askokcancel("Confirmation", f"Are you sure you want to deactivate the account for '{username_to_deactivate}'?")

            if confirm_deactivate:
                self.update_account_status(username_to_deactivate, deactivated=True)
                #tk.messagebox.showinfo("Success" f"The account for '{username_to_deactivate}' has been deactivated successfully")
                self.upload_csv_data(self.display_volunteer_tree, 'volunteer_info.csv')
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")

    def delete_account(self):
        selected_index = self.display_volunteer_tree.focus()
        if selected_index:
            username_to_delete = self.display_volunteer_tree.item(selected_index, 'values')[0]
            confirm_delete = tk.messagebox.askokcancel("Confirmation",
                                                    f"Are you sure you want to delete the account '{username_to_delete}'?")
            if confirm_delete:
                self.remove_account(username_to_delete)
                tk.messagebox.showinfo("Success", f"The account '{username_to_delete}' has been deleted successfully.")
                self.remove_account(username_to_delete)
                self.upload_csv_data(self.display_volunteer_tree, 'volunteer_info.csv')
        else:
            tk.messagebox.showwarning("No Selection", "Please select a volunteer.")

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

            self.upload_csv_data(self.display_volunteer_tree, 'volunteer_info.csv')

        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")

    def update_account_status(self, username, deactivated):
        try:
            csv_file = 'volunteer_info.csv'
            data = pd.read_csv(csv_file, dtype={'Phone Number': str})

            mask = data['Username'] == username
            if mask.any():
                current_status = data.loc[mask, 'Deactivated'].iloc[0]

                if (current_status and deactivated) or (not current_status and not deactivated):
                    action = "inactive" if deactivated else "active"
                    messagebox.showinfo("Status Unchanged", f"Account for {username} is already {action.lower()}.")
                else:
                    # Convert 'Phone Number' column explicitly to string
                    data['Phone Number'] = data['Phone Number'].astype(str)

                    # Update the 'Deactivated' column
                    data.loc[mask, 'Deactivated'] = deactivated

                    # Save the updated DataFrame to the CSV file
                    data.to_csv(csv_file, index=False)

                    action = "Deactivated" if deactivated else "Reactivated"
                    messagebox.showinfo(action, f"Account for {username} {action.lower()} successfully.")
                    self.upload_csv_data(self.display_volunteer_tree, csv_file)
            else:
                messagebox.showwarning("Error", f"Account for {username} not found.")

        except FileNotFoundError:
            messagebox.showwarning("Error", "'volunteer_info.csv' file not found.")