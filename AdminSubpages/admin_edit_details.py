import tkinter as tk
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
        tk.Label(self.window, text="Admin Edit Volunteer Details", font=('Helvetica', 16)).grid(row=0, column=0,
                                                                                                pady=10)
        tk.Label(self.window, text="Select Volunteer:").grid(row=1, column=0, padx=10, pady=5)

        # Listbox to display volunteer usernames
        self.volunteer_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        self.populate_volunteer_listbox()
        self.volunteer_listbox.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.window, text="Edit Account (Deactivate)", command=self.deactivate_account).grid(row=3, column=0,
                                                                                                       columnspan=2,
                                                                                                       pady=10)
        tk.Button(self.window, text="Edit Account (Reactivate)", command=self.reactivate_account).grid(row=4, column=0,
                                                                                                       columnspan=2,
                                                                                                       pady=10)
        tk.Button(self.window, text="Edit Account (Delete)", command=self.delete_account).grid(row=5, column=0,
                                                                                               columnspan=2, pady=10)
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
            print("Error: 'volunteer_info.csv' file not found.")

    def create_account(self):
        pass
            
    #sets deactivated column in the volunteer_info.csv from true to false
    def reactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_reactivate = self.volunteer_listbox.get(selected_index)
            self.update_account_status(username_to_reactivate, deactivated=False)
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")
    #sets deactivated column in the volunteer_info.csv from false to true
    def deactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_deactivate = self.volunteer_listbox.get(selected_index)
            self.update_account_status(username_to_deactivate, deactivated=True)
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")
    #for now the delete account function will set a variable from true to false like deactivated does 
    #however, i think this should be a permanent removal from the csv
    def delete_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_delete = self.volunteer_listbox.get(selected_index)
            self.mark_account_deleted(username_to_delete)
            self.volunteer_listbox.delete(selected_index)
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")



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
            print("Error: 'volunteer_info.csv' file not found.")

    def delete_account(self, username):
        try:
            with open('volunteer_info.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                for row in rows:
                    if row['Username'] == username:
                        row['Deleted'] = 'True'

            with open('volunteer_info.csv', 'w', newline='') as csvfile:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            messagebox.showinfo("Deletion", f"Account for {username} marked as deleted.")
        except FileNotFoundError:
            print("Error: 'volunteer_info.csv' file not found.")