import tkinter as tk


class AdminEditVolunteerDetails:
    def __init__(self, window):
        self.window = window

        # If we want to change the title but probably not necessary
        #self.window.title("Admin Edit Volunteer Details")
        self.y_personal_info = {
            'volunteer1': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': False, 'Deleted': False},
            'volunteer2': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': False, 'Deleted': False},
            'volunteer3': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': True, 'Deleted': False},
            'volunteer4': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': False, 'Deleted': False}
        }
        self.volunteer_listbox = None  # To be initialized later
        self.deactivated_accounts = []

    def create_gui(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        new_plan_frame = tk.Frame(self.window)
        new_plan_frame.grid()
        # Labels
        tk.Label(self.window, text="Admin Edit Volunteer Details", font=('Helvetica', 16)).grid(row=0, column=0, pady=10)
        tk.Label(self.window, text="Select Volunteer:").grid(row=1, column=0, padx=10, pady=5)

        # Listbox to display volunteer usernames
        self.window.volunteer_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        for volunteer in self.y_personal_info:
            self.volunteer_listbox.insert(tk.END, volunteer)
        self.window.volunteer_listbox.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.window, text="Edit Account (Deactivate)", command=self.deactivate_account).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="Edit Account (Reactivate)", command=self.reactivate_account).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="Edit Account (Delete)", command=self.delete_account).grid(row=5, column=0, columnspan=2, pady=10)

    # Takes the deactivated account out of the
    def reactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_reactivate = self.volunteer_listbox.get(selected_index)
            if self.y_personal_info[username_to_reactivate]["Deactivated"]:
                self.y_personal_info[username_to_reactivate]["Deactivated"] = False

                print(f"Account for {username_to_reactivate} reactivated.")
            else:
                print(f"Account for {username_to_reactivate} is not deactivated.")
        else:
            print("Please select a volunteer.")

    def deactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_deactivate = self.volunteer_listbox.get(selected_index)
            if not self.y_personal_info[username_to_deactivate]["Deactivated"]:
                self.y_personal_info[username_to_deactivate]["Deactivated"] = True
                print(f"Account for {username_to_deactivate} deactivated.")
            else:
                print(f"Account for {username_to_deactivate} is already deactivated.")
        else:
            print("Please select a volunteer.")

    def delete_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_delete = self.volunteer_listbox.get(selected_index)
            del self.y_personal_info[username_to_delete]
            print(f"Account for {username_to_delete} deleted.")
            self.volunteer_listbox.delete(selected_index)
        else:
            print("Please select a volunteer.")

