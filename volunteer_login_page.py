import tkinter as tk
from tkinter import messagebox
import os
import pickle

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
    def __init__(self, root, go_to_volunteer_main):
        super().__init__(root)
        self.go_to_volunteer_main = go_to_volunteer_main
        try:
            if os.path.getsize('data.pickle') > 0:
                with open('data.pickle', 'rb') as file:
                    self.y_personal_info = pickle.load(file)
            else:
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

        self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}

        #self.t_volunteer_login
        #self.t_details_confirmation

        # Volunteer frame put on screen
        #self.t_volunteer_frame = tk.Frame(self)
        #self.t_volunteer_frame.pack()

        # Volunteer frame white boarder
        #self.t_info_frame = tk.LabelFrame(self.t_volunteer_frame, text='Volunteer login', font=25)
        #self.t_info_frame.grid(row=0, column=0, padx=20, pady=10)


        # Volunteer title
        self.t_volunteer_title = tk.Label(self, text='Volunteer login', font=('Arial bold', 50))
        self.t_volunteer_title.grid(row=0, column=0, pady=30)

        # Username entry box
        self.t_name_label = tk.Label(self, text='Username')
        self.t_name_label.grid(row=1, column=0)
        self.t_name_entry = tk.Entry(self)
        self.t_name_entry.grid(row=2, column=0)

        # Password entry box
        self.t_password_label2 = tk.Label(self, text='Password')
        self.t_password_label2.grid(row=3, column=0, pady=5)
        self.t_password_entry = tk.Entry(self, show='*')
        self.t_password_entry.grid(row=4, column=0)
        self.t_password_entry.bind("<KeyPress>", self.caps_lock_on)
        self.t_password_entry.bind("<KeyRelease>", self.caps_lock_off)

        # Login box
        self.t_entry_button = tk.Button(self, text='Login', command=self.t_details_confirmation, height=1, width=20)
        self.t_entry_button.grid(row=5, column=0, pady=20)

        # Shows caps lock on/off (OLD BINDING NOT WORKING)
        self.label_caps = tk.Label(self, text='')
        self.label_caps.grid(row=4, column=1)
        #self.bind("<KeyPress>", self.caps_lock_on)
        #self.bind("<KeyRelease>", self.caps_lock_off)

    # For caps lock on/off
    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on')

    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is off')

    # Login checker
    def t_details_confirmation(self):
        username = self.t_name_entry.get()
        password = self.t_password_entry.get()
        try:
            if username not in self.y_personal_info.keys():
                raise t_deleted_account
            elif self.y_personal_info[username]['Deactivated'] == True:
                raise t_deactivated_account
            else:
                if password == self.y_personal_info[username]['password']:
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
        self.go_to_volunteer_main()
