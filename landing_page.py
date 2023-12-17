import tkinter as tk
from admin_login_page import AdminLoginPage
from volunteer_login_page import VolunteerLoginPage
from tkinter import messagebox, PhotoImage
import pandas as pd

class LandingPage:
    def __init__(self, root, go_to_admin_main, go_to_volunteer_main):
        self.root = root
        self.go_to_admin_main = go_to_admin_main
        self.go_to_volunteer_main = go_to_volunteer_main
        self.window = tk.Toplevel(self.root)
        self.window.title('Welcome to the UCL Humanity Rescue Portal')
        self.window.geometry('800x500')
        self.window.configure(background="lightgrey")
        self.create_landing_page_widgets()
        self.window.protocol("WM_DELETE_WINDOW", self.window_exit_button)

        try:
            self.y_personal_info = pd.read_csv('volunteer_info.csv', index_col='Username')
            self.y_personal_info = self.y_personal_info.to_dict(orient='index')
            #print(self.y_personal_info)

        except(FileNotFoundError):
            self.y_personal_info = {
                'volunteer1': {'Camp ID': '', 'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': False, 'Deleted': False},
                'volunteer2': {'Camp ID': '', 'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': False, 'Deleted': False},
                'volunteer3': {'Camp ID': '', 'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': True, 'Deleted': False},
                'volunteer4': {'Camp ID': '', 'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': False, 'Deleted': False}
            }

            df = pd.DataFrame.from_dict(self.y_personal_info, orient='index')
            df.index.name = 'Username'
            df.to_csv('volunteer_info.csv', index='Username')
            self.y_personal_info = pd.read_csv('volunteer_info.csv')

    def create_landing_page_widgets(self):
        welcome_label = tk.Label(
            self.window,
            text='Welcome to the UCL Humanity Rescue Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='white'
        )
        welcome_label.pack(padx=25, pady=25)
        welcome_label.configure(background="orange")

        self.logo = PhotoImage(file="Images/logo.png").subsample(4, 4)
        image_label = tk.Label(self.window, image=self.logo, relief=tk.RAISED)
        image_label.pack(pady=0, padx=(0, 0))

        instruction_label = tk.Label(
            self.window,
            text='Please select admin or volunteer sign in',
            font=('TkDefaultFont', 10)
        )
        instruction_label.pack(pady=(20,20))
        instruction_label.configure(background="lightgrey")

        # Admin login button
        admin_login_btn = tk.Button(self.window, text="Admin Login", command=self.open_admin_login)
        admin_login_btn.pack(ipadx=100, ipady=25)
        admin_login_btn.configure(background="lightgreen")
        # Volunteer login button
        volunteer_login_btn = tk.Button(self.window, text="Volunteer Login", command=self.open_volunteer_login)
        volunteer_login_btn.pack(ipadx=93, ipady=25, pady=10)
        volunteer_login_btn.configure(background="lightblue")
        # Exit program button
        exit_btn = tk.Button(self.window, text="Exit Software", foreground='black', command=self.exit_software)
        exit_btn.pack(ipadx=10, ipady=2, pady=20)
        #exit_btn.configure(background="black")


    def open_admin_login(self):
        for widget in self.window.winfo_children():
            if widget.winfo_class() != 'Menu':
                widget.destroy()
        self.admin_login_frame = AdminLoginPage(
            self.window,
            self.window,
            self.go_to_admin_main,
            self.open_admin_login,
            self.open_volunteer_login,
            self.exit_software
        )
        self.admin_login_frame.pack(fill='both', expand=True)

    def open_volunteer_login(self):
        for widget in self.window.winfo_children():
            if widget.winfo_class() != 'Menu':
                widget.destroy()
        self.volunteer_login_frame = VolunteerLoginPage(
            self.window,
            self.window,
            self.go_to_volunteer_main,
            self.open_admin_login,
            self.open_volunteer_login,
            self.exit_software
        )
        self.volunteer_login_frame.pack(fill='both', expand=True)

    def exit_software(self):
        self.root.quit()

    def window_exit_button(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()
        #self.root.destroy()

    def destroy(self):
        self.window.destroy()
