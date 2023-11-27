import tkinter as tk
from tkinter import messagebox

class AdminEditVolunteerDetails:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main

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
        self.deactivated_accounts = {}

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
        self.volunteer_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        for volunteer in self.y_personal_info:
            self.volunteer_listbox.insert(tk.END, volunteer)
        self.volunteer_listbox.grid(row=1, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.window, text="Edit Account (Deactivate)", command=self.deactivate_account).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="Edit Account (Reactivate)", command=self.reactivate_account).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="Edit Account (Delete)", command=self.delete_account).grid(row=5, column=0, columnspan=2, pady=10)
        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=17, column=1, padx=5, pady=10)

    
    
    
    
    def reactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_reactivate = self.volunteer_listbox.get(selected_index)
            if self.y_personal_info[username_to_reactivate]["Deactivated"]:
                self.y_personal_info[username_to_reactivate]["Deactivated"] = False
                messagebox.showinfo("Reactivation", f"Account for {username_to_reactivate} reactivated.")
            else:
                messagebox.showinfo("Reactivation", f"Account for {username_to_reactivate} is not deactivated.")
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")

    def deactivate_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_deactivate = self.volunteer_listbox.get(selected_index)
            if not self.y_personal_info[username_to_deactivate]["Deactivated"]:
                self.y_personal_info[username_to_deactivate]["Deactivated"] = True
                messagebox.showinfo("Deactivation", f"Account for {username_to_deactivate} deactivated.")
            else:
                messagebox.showinfo("Deactivation", f"Account for {username_to_deactivate} is already deactivated.")
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")

    def delete_account(self):
        selected_index = self.volunteer_listbox.curselection()
        if selected_index:
            username_to_delete = self.volunteer_listbox.get(selected_index)
            self.y_personal_info[username_to_delete]["Deleted"] = True
            messagebox.showinfo("Deletion", f"Account for {username_to_delete} marked as deleted.")
            self.volunteer_listbox.delete(selected_index)
        else:
            messagebox.showwarning("No Selection", "Please select a volunteer.")