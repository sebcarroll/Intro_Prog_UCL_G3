import tkinter as tk
from tkinter import messagebox
import os
import pickle
import pandas as pd

class t_case_sensitive(Exception):
    pass
class t_no_text(Exception):
    pass
class t_incorrect_details(Exception):
    pass
class t_deleted_account(Exception):
    pass
class t_deactivated_account(Exception):
    pass

class VolunteerLoginPage(tk.Frame, t_deactivated_account, t_deleted_account, t_case_sensitive, t_no_text, t_incorrect_details):
    def __init__(self, root, window, go_to_volunteer_main, open_admin_login, open_volunteer_login, exit_software):
        super().__init__(root)
        self.root = root
        self.window = window
        self.go_to_volunteer_main = go_to_volunteer_main
        self.open_admin_login = open_admin_login
        self.open_volunteer_login = open_volunteer_login
        self.exit_software = exit_software

        try:
            self.y_personal_info = pd.read_csv('volunteer_info.csv', index_col='Username')
            self.y_personal_info = self.y_personal_info.to_dict(orient='index')
            print(self.y_personal_info)

        except(FileNotFoundError):
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

            df = pd.DataFrame.from_dict(self.y_personal_info, orient='index')
            df.index.name = 'Username'
            df.to_csv('volunteer_info.csv', index='Username')
            self.y_personal_info = pd.read_csv('volunteer_info.csv')

        #self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}

        welcome_label = tk.Label(
            self,
            text='Welcome to the UCL Humanity Rescue Volunteer Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='blue'
        )
        welcome_label.grid(row=0, column=0, padx=30, pady=30)

        instruction_label = tk.Label(
            self,
            text='Volunteer login',
            font=('TkDefaultFont', 20)
        )
        instruction_label.grid(row=1, column=0, pady=30)

        volunteer_entries_frame = tk.Frame(self)
        volunteer_entries_frame.grid()

        # Label frame for this page that then stores all of the labels and entries
        volunteer_log_in_frame = tk.LabelFrame(volunteer_entries_frame)
        volunteer_log_in_frame.grid(row=2, column=0, pady=30)

        # Volunteer title
        #self.t_volunteer_title = tk.Label(self, text='Volunteer login', font=('Arial bold', 50))
        #self.t_volunteer_title.grid(row=0, column=0, pady=30)

        # Username entry box
        self.name_label = tk.Label(volunteer_log_in_frame, text='Username')
        self.name_label.grid(row=6, column=0, pady=10, padx=10)
        self.name_entry = tk.Entry(volunteer_log_in_frame)
        self.name_entry.grid(row=6, column=1, pady=10, padx=10)

        # Password entry box
        self.password_label2 = tk.Label(volunteer_log_in_frame, text='Password')
        self.password_label2.grid(row=8, column=0, pady=10)
        self.password_entry = tk.Entry(volunteer_log_in_frame, show='*')
        self.password_entry.grid(row=8, column=1, pady=10)
        self.password_entry.bind("<KeyPress>", self.caps_lock_on)
        self.password_entry.bind("<KeyRelease>", self.caps_lock_off)

        # # Username entry box
        # self.t_name_label = tk.Label(self, text='Username')
        # self.t_name_label.grid(row=1, column=0)
        # self.t_name_entry = tk.Entry(self)
        # self.t_name_entry.grid(row=2, column=0)
        #
        # # Password entry box
        # self.t_password_label2 = tk.Label(self, text='Password')
        # self.t_password_label2.grid(row=3, column=0, pady=5)
        # self.t_password_entry = tk.Entry(self, show='*')
        # self.t_password_entry.grid(row=4, column=0)

        # Login box
        # self.entry_button = tk.Button(self, text='Login', command=self.t_details_confirmation, height=1, width=20)
        # self.entry_button.grid(row=5, column=0, pady=20)
        #
        # # Back to landing page
        # login_btn = tk.Button(self.window, text="Back", command=self.exit_and_go_back)
        # login_btn.grid(row=10, column=0, pady=10)


        login_btn = tk.Button(volunteer_log_in_frame, text="Login", command=self.t_details_confirmation)
        login_btn.grid(row=10, column=1, pady=10)
        # Swap button from command=self.t_details_confirmation to command=self.on_login to bypass

        # Back to landing page
        back_button = tk.Button(volunteer_log_in_frame, text="Back", command=self.exit_and_go_back)
        back_button.grid(row=10, column=0, pady=10)


        # Shows caps lock on/off (OLD BINDING NOT WORKING)
        self.label_caps = tk.Label(self, text='')
        self.label_caps.grid(row=4, column=1)
        #self.bind("<KeyPress>", self.caps_lock_on)
        #self.bind("<KeyRelease>", self.caps_lock_off)
        for i in range(3):
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

    # For caps lock on/off
    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on')

    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is off')

    # Login checker
    def t_details_confirmation(self):
        username = self.name_entry.get()
        password = self.password_entry.get()
        try:
            if username not in self.y_personal_info.keys():
                raise t_deleted_account
            elif self.y_personal_info[username]['Deactivated'] == True:
                raise t_deactivated_account
            else:
                if password == str(self.y_personal_info[username]['password']):
                    self.go_to_volunteer_main(username)
                elif password != self.y_personal_info[username]['password']:
                    raise t_incorrect_details

            # if (username.lower() or password.lower()) in self.volunteer_dict:
            # raise t_case_sensitive
        except(t_incorrect_details):
            tk.messagebox.showinfo(title='Incorrect details', message='The password does not match the username')
        # except(t_case_sensitive):
        # tkinter.messagebox.showinfo(title='Incorrect capitals', message='Check to make sure you didn\'t accidentally use caps lock')
        except(t_deleted_account):
            tk.messagebox.showinfo(title='Username non-existent', message='That is not a valid volunteer username')
        except(t_deactivated_account):
            tk.messagebox.showinfo(title='Deactivated account',
                                        message='Your account has been deactivated, \nPlease contact admin for more details')



    def on_login(self):
        # Add volunteer login logic here
        username = ""
        self.go_to_volunteer_main(username)

    def exit_and_go_back(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        from landing_page import LandingPage
        LandingPage.create_landing_page_widgets(self)

