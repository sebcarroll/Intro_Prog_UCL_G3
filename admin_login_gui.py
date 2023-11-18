import tkinter
import pickle
import re
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class na_case_sensitive(Exception):
    pass


class na_no_text(Exception):
    pass


class na_incorrect_details(Exception):
    pass


class na_invalid_name(Exception):
    pass

class na_admin_main_page(na_case_sensitive, na_no_text, na_incorrect_details, na_invalid_name):

    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.title('Whatever')
        self.na_admin_login()
        self.na_details_confirmation()
    def na_admin_login(self):
        for i in self.window.winfo_children():
            i.destroy()

        # admin frame put on screen
        self.na_admin_frame = tkinter.Frame(self.window)
        self.na_admin_frame.pack()

        # admin frame white boarder
        self.na_info_frame = tkinter.LabelFrame(self.na_admin_frame, text='admin login', font=25)
        self.na_info_frame.grid(row=0, column=0, padx=20, pady=10)

        # admin title
        self.na_admin_title = tkinter.Label(self.na_admin_frame, text='admin login', font=('Arial bold', 50))
        self.na_admin_title.grid(row=0, column=0, pady=30)

        # Username entry box
        self.na_name_label = tkinter.Label(self.na_admin_frame, text='Username')
        self.na_name_label.grid(row=1, column=0)
        self.na_name_entry = tkinter.Entry(self.na_admin_frame)
        self.na_name_entry.grid(row=2, column=0)

        # Password entry box
        self.na_password_label = tkinter.Label(self.na_admin_frame, text='Password')
        self.na_password_label.grid(row=3, column=0, pady=5)
        self.na_password_entry = tkinter.Entry(self.na_admin_frame, show='*')
        self.na_password_entry.grid(row=4, column=0)

        # Login box
        self.na_entry_button = tkinter.Button(self.na_admin_frame, text='Login', command=self.na_details_confirmation,
                                             height=1, width=20)
        self.na_entry_button.grid(row=5, column=0, pady=20)

        # Shows caps lock on/off
        self.label_caps = tkinter.Label(self.na_admin_frame)
        self.label_caps.grid(row=4, column=1)
        self.window.bind("<KeyPress>", self.caps_lock_on)
        self.window.bind("<KeyRelease>", self.caps_lock_off)

        # Launches tkinter
        self.window.mainloop()

        def na_admin_details(self):
            self.username = self.t_name_entry.get()
            password = self.t_password_entry.get()
            try:
                if self.username not in self.y_personal_info.keys():
                    raise t_deleted_account
                elif self.y_personal_info[self.username]['Deactivated'] == True:
                    raise t_deactivated_account
                else:
                    if password == self.y_personal_info[self.username]['password']:
                        self.t_volunteer_summary()
                    elif password != self.y_personal_info[self.username]['password']:
                        raise t_incorrect_details

                # if (username.lower() or password.lower()) in self.volunteer_dict:
                # raise t_case_sensitive
            except(t_incorrect_details):
                tkinter.messagebox.showinfo(title='Incorrect details',
                                            message='The password does not match the username')
            # except(t_case_sensitive):
            # tkinter.messagebox.showinfo(title='Incorrect capitals', message='Check to make sure you didn\'t accidentally use caps lock')
            except(t_deleted_account):
                tkinter.messagebox.showinfo(title='Username non-existent',
                                            message='That is not a valid volunteer username')
            except(t_deactivated_account):
                tkinter.messagebox.showinfo(title='Deactivated account',
                                            message='Your account has been deactivated, \nPlease contact admin for more details')

        # For caps lock on/off
        def caps_lock_on(self, event):
            if event.keysym == 'Caps_Lock':
                self.label_caps.config(text='Caps lock is on')

        def caps_lock_off(self, event):
            if event.keysym == 'Caps_Lock':
                self.label_caps.config(text='')
