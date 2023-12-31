
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import os
import pickle
import pandas as pd
import csv
volunteer_camp_id_for_new_refugee = None

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

        #self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}

        welcome_label = tk.Label(
            self,
            text='UCL Humanity Rescue Volunteer Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='blue', relief=tk.RAISED, borderwidth=5
        )
        welcome_label.grid(row=1, column=0, padx=30, pady=30)

        # instruction_label = tk.Label(
        #     self,
        #     text='Volunteer login',
        #     font=('TkDefaultFont', 20)
        # )
        # instruction_label.grid(row=1, column=0, pady=30)

        volunteer_entries_frame = tk.Frame(self, relief=tk.RAISED, borderwidth=5)
        volunteer_entries_frame.grid()

        # Label frame for this page that then stores all of the labels and entries
        volunteer_log_in_frame = tk.LabelFrame(volunteer_entries_frame, borderwidth=5)
        volunteer_log_in_frame.grid(row=3, column=1, pady=30, padx=30)

        # Username entry box
        self.name_label = tk.Label(volunteer_log_in_frame, text='Username', font=('TkDefault', 17))
        self.name_label.grid(row=6, column=0, pady=10, padx=10)
        self.name_entry = tk.Entry(volunteer_log_in_frame)
        self.name_entry.grid(row=6, column=1, pady=10, padx=10)

        # Password entry box
        self.password_label2 = tk.Label(volunteer_log_in_frame, text='Password', font=('TkDefault', 17))
        self.password_label2.grid(row=8, column=0, pady=10)
        self.password_entry = tk.Entry(volunteer_log_in_frame, show='*')
        self.password_entry.grid(row=8, column=1, pady=10)
        self.password_entry.bind("<KeyPress>", self.caps_lock_on)
        self.password_entry.bind("<KeyRelease>", self.caps_lock_off)

        try:
            self.image3 = PhotoImage(file="Images/volunteer_icon.png").subsample(6, 6)
            image_label = tk.Label(volunteer_log_in_frame, image=self.image3, relief=tk.RAISED, borderwidth=5)
            image_label.grid(row=5, column=1, pady=10, padx=(0, 0))
        except:
            pass

        try:
            self.logo = PhotoImage(file="Images/logo.png").subsample(4, 4)
            image_label = tk.Label(volunteer_log_in_frame, image=self.logo, relief=tk.RAISED)
            image_label.grid(row=5, column=0, pady=10, padx=(0, 0))
        except:
            pass

        login_btn = tk.Button(volunteer_log_in_frame, text="Login", command=self.t_details_confirmation)
        login_btn.grid(row=10, column=1, pady=10)

        # Back to landing page
        back_button = tk.Button(volunteer_log_in_frame, text="Back", command=self.exit_and_go_back)
        back_button.grid(row=10, column=0, pady=10)

        # Shows caps lock on/off (OLD BINDING NOT WORKING)
        self.label_caps = tk.Label(volunteer_log_in_frame, text='')
        self.label_caps.grid(row=4, column=1)
        #self.bind("<KeyPress>", self.caps_lock_on)
        #self.bind("<KeyRelease>", self.caps_lock_off)
        for i in range(11):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # For caps lock on/off
    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on')

    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is off')

    def get_camp_id_for_volunteer_for_new_refugee(self):
        global volunteer_camp_id_for_new_refugee

        with open("volunteer_info.csv", 'r') as file:
            csv_reader = csv.reader(file)
            # Name is in the first column
            for row in csv_reader:
                if row and str(row[0].strip()) == self.username:
                    # Camp ID is the second value
                    volunteer_camp_id_for_new_refugee = row[1].strip()
                    #print(volunteer_camp_id_for_new_refugee)
                    break
        return volunteer_camp_id_for_new_refugee

    # Login checker
    def t_details_confirmation(self):
        self.username = self.name_entry.get()
        #print(self.name_entry.get())
        password = self.password_entry.get()
        try:
            if self.username not in self.y_personal_info.keys():
                raise t_deleted_account
            elif self.y_personal_info[self.username]['Deactivated'] == True:
                raise t_deactivated_account
            else:
                if password == str(self.y_personal_info[self.username]['password']):
                    self.go_to_volunteer_main(self.username)
                    self.get_camp_id_for_volunteer_for_new_refugee()
                elif password != self.y_personal_info[self.username]['password']:
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

