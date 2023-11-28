import tkinter
import pickle
import re
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import tkinter as tk
import pandas as pd

window = tkinter.Tk()
window.title('Welcome to the UCL Humanity Rescue Portal')
window.geometry('1000x600')


class na_case_sensitive(Exception):
    pass


class na_no_text(Exception):
    pass


class na_incorrect_details(Exception):
    pass


class na_invalid_name(Exception):
    pass


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


class invalid_email(Exception):
    pass


class invalid_phone_number(Exception):
    pass


class invalid_name(Exception):
    pass


class file_not_found(Exception):
    pass


class LandingPage(t_deactivated_account, t_deleted_account, t_case_sensitive, t_no_text, t_incorrect_details,
                  file_not_found):
    def __init__(self):
        # window.protocol("WM_DELETE_WINDOW", window_exit_button)
        for i in window.winfo_children():
            i.destroy()
        landing_page_frame = tkinter.Frame(window)
        landing_page_frame.pack()

        welcome_label = tkinter.Label(
            landing_page_frame,
            text='Welcome to the UCL Humanity Rescue Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='white'
        )
        welcome_label.grid(row=0, column=3, padx=30, pady=30)
        welcome_label.configure(background="red")

        instruction_label = tkinter.Label(
            landing_page_frame,
            text='Please select admin or volunteer sign in',
            font=('TkDefaultFont', 20)
        )
        instruction_label.grid(row=1, column=3, padx=30, pady=30)
        instruction_label.configure(background="lightgrey")

        # Admin login button
        admin_login_btn = tkinter.Button(window, text="Admin Login", command=na_admin_main_page)
        admin_login_btn.pack(ipadx=100, ipady=25)
        admin_login_btn.configure(background="lightgreen")
        # Volunteer login button
        volunteer_login_btn = tkinter.Button(window, text="Volunteer Login", command=tvolunteer_main_page)
        volunteer_login_btn.pack(ipadx=93, ipady=25, pady=10)
        volunteer_login_btn.configure(background="lightblue")
        # Exit program button
        # exit_btn = tkinter.Button(self.window, text="Exit Software", foreground='white', command=self.exit_software)
        # exit_btn.pack(ipadx=10, ipady=2, pady=70)
        # exit_btn.configure(background="black")

        window.mainloop()


class tvolunteer_main_page(t_deactivated_account, t_deleted_account, t_case_sensitive, t_no_text, t_incorrect_details,
                           file_not_found):

    def __init__(self) -> None:
        # Volunteer dictionary - Nested: Can access via self.y_personal_info[username][key]

        try:
            if os.path.getsize('refugee.pickle') > 0:
                with open('refugee.pickle', 'rb') as file:
                    self.na_refugee_info = pickle.load(file)

            else:
                self.na_refugee_info = {
                    'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                                 'Second Language': ''}
                }

        except(FileNotFoundError):
            self.na_refugee_info = {
                'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                             'Second Language': ''}}


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


        self.y_camp_info = {"Country": "America", "Max Capacity": ""}
        self.y_camp_info['ID'] = {"Country": "America 132", "Max Capacity": 1000, 'Food packets': 0,
                                  'Medical supplies': 0, 'Water and sanitation': 0, 'Clothing': 0,
                                  'Shelter materials': 0}
        try:
            if os.path.getsize('Camp.pickle') > 0:
                with open('Camp.pickle', 'rb') as f:
                    self.y_camp_info = pickle.load(f)
            else:
                self.y_camp_info['ID'] = {"Country": "America 132", "Max Capacity": 1000, 'Food packets': 0,
                                          'Medical supplies': 0, 'Water and sanitation': 0, 'Clothing': 0,
                                          'Shelter materials': 0}
        except(FileNotFoundError):
            self.y_camp_info['ID'] = {"Country": "America 132", "Max Capacity": 1000, 'Food packets': 0,
                                      'Medical supplies': 0, 'Water and sanitation': 0, 'Clothing': 0,
                                      'Shelter materials': 0}

        self.t_volunteer_login()

    def t_volunteer_login(self):
        # Anything on window before is removed and populates with the following code
        for i in window.winfo_children():
            i.destroy()

        # Volunteer frame put on screen
        self.t_volunteer_frame = tkinter.Frame(window)
        self.t_volunteer_frame.pack()

        # Volunteer frame white boarder
        self.t_info_frame = tkinter.LabelFrame(self.t_volunteer_frame, text='Volunteer login', font=25)
        self.t_info_frame.grid(row=0, column=0, padx=20, pady=10)

        # Volunteer title
        self.t_volunteer_title = tkinter.Label(self.t_volunteer_frame, text='Volunteer login', font=('Arial bold', 50))
        self.t_volunteer_title.grid(row=0, column=0, pady=30)

        # Username entry box
        self.t_name_label = tkinter.Label(self.t_volunteer_frame, text='Username')
        self.t_name_label.grid(row=1, column=0)
        self.t_name_entry = tkinter.Entry(self.t_volunteer_frame)
        self.t_name_entry.grid(row=2, column=0)

        # Password entry box
        self.t_password_label2 = tkinter.Label(self.t_volunteer_frame, text='Password')
        self.t_password_label2.grid(row=3, column=0, pady=5)
        self.t_password_entry = tkinter.Entry(self.t_volunteer_frame, show='*')
        self.t_password_entry.grid(row=4, column=0)

        # Login box
        self.t_entry_button = tkinter.Button(self.t_volunteer_frame, text='Login', command=self.t_details_confirmation,
                                             height=1, width=20)
        self.t_entry_button.grid(row=5, column=0, pady=20)

        # Shows caps lock on/off
        self.label_caps = tkinter.Label(self.t_volunteer_frame)
        self.label_caps.grid(row=4, column=1)
        window.bind("<KeyPress>", self.caps_lock_on)
        window.bind("<KeyRelease>", self.caps_lock_off)
        back_button = tkinter.Button(self.t_volunteer_frame, text='Back', command=LandingPage)
        back_button.grid(row=6, column=0, padx=10, pady=10)

    # Login checker
    def t_details_confirmation(self):

        self.username = self.t_name_entry.get()
        password = self.t_password_entry.get()
        try:
            if self.username not in self.y_personal_info.keys():
                raise t_deleted_account

            elif self.y_personal_info[self.username]['Deactivated'] == True:
                raise t_deactivated_account

            else:
                if password == str(self.y_personal_info[self.username]['password']):
                    self.t_volunteer_summary()
                else:
                    print(password, self.y_personal_info[self.username]['password'])
                    raise t_incorrect_details

            # if (username.lower() or password.lower()) in self.volunteer_dict:
            # raise t_case_sensitive
        except(t_incorrect_details):
            tkinter.messagebox.showinfo(title='Incorrect details', message='The password does not match the username')
        except(t_deleted_account):
            tkinter.messagebox.showinfo(title='Username non-existent', message='That is not a valid volunteer username')
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

    # Main homepage for volunteers
    def t_volunteer_summary(self):
        for i in window.winfo_children():
            i.destroy()
        self.t_summary_frame = tkinter.Frame(window)
        self.t_summary_frame.pack()
        self.t_summary_title = tkinter.Label(self.t_summary_frame, text='Welcome to the volunteer portal',
                                             font=('Arial Bold', 40))
        self.t_summary_title.grid(row=0, column=3, pady=30)
        self.t_summary_editdetails = tkinter.Button(self.t_summary_frame, text='Personal information',
                                                    command=self.t_personal_information_base, height=2, width=20)
        self.t_summary_editdetails.grid(row=3, column=3, pady=5)
        self.t_summary_editcamp = tkinter.Button(self.t_summary_frame, text='Edit camp information',
                                                 command=self.t_edit_camp, height=2, width=20)
        self.t_summary_editcamp.grid(row=4, column=3, pady=5)
        self.t_summary_refugee = tkinter.Button(self.t_summary_frame, text='Create a refugee profile',
                                                command=self.t_create_refugee, height=2, width=20)
        self.t_summary_refugee.grid(row=5, column=3)

    # UI for personal info - very similar to the t_volunteer_login function:
    def t_personal_information_base(self):
        for i in window.winfo_children():
            i.destroy()
        t_personal_frame = tkinter.Frame(window)
        t_personal_frame.pack()
        t_personal_labelframe = tkinter.LabelFrame(t_personal_frame)
        t_personal_labelframe.grid(row=3, column=3, padx=10, pady=10)
        t_personal_title = tkinter.Label(t_personal_frame, text='Volunteer Details', font=('Arial Bold', 30)).grid(
            row=0, column=3, pady=30)
        t_personal_namelabel = tkinter.Label(t_personal_labelframe, text='Name', font=('TkDefaultFont', 15)).grid(row=4,
                                                                                                                  column=2,
                                                                                                                  pady=5)
        t_personal_name = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['name'],
                                        font=('TkDefaultFont', 15))
        t_personal_name.grid(row=4, column=3, pady=5)

        # Email label
        t_personal_emailabel = tkinter.Label(t_personal_labelframe, text='Email Address: ',
                                             font=('TkDefaultFont', 15)).grid(row=6, column=2, pady=5)
        t_personal_email = tkinter.Label(t_personal_labelframe,
                                         text=self.y_personal_info[self.username]['Email Address'],
                                         font=('TkDefaultFont', 15))
        t_personal_email.grid(row=6, column=3, pady=5)

        t_personal_phonenumberlabel = tkinter.Label(t_personal_labelframe, text='Phone number: ',
                                                    font=('TkDefaultFont', 15)).grid(row=8, column=2, pady=5)
        t_phonenumber = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['Phone Number'],
                                      font=('TkDefaultFont', 15))
        t_phonenumber.grid(row=8, column=3, pady=5)

        t_personal_commitmentlabel = tkinter.Label(t_personal_labelframe, text='Commitment: ',
                                                   font=('TkDefaultFont', 15)).grid(row=10, column=2, pady=5)
        t_commitment = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['Commitment'],
                                     font=('TkDefaultFont', 15))
        t_commitment.grid(row=10, column=3, pady=5)

        t_personal_namelabel = tkinter.Label(t_personal_labelframe, text='Work type: ',
                                             font=('TkDefaultFont', 15)).grid(row=12, column=2, pady=5)
        t_work_type_label = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['Work Type'],
                                          font=('TkDefaultFont', 15))
        t_work_type_label.grid(row=12, column=3, pady=5)

        # Store details button, need to put it in the
        t_edit_details = tkinter.Button(t_personal_frame, text='Edit details', command=self.t_personal_info_edit,
                                        height=1, width=20)
        t_edit_details.grid(row=14, column=3)
        t_back_to_summary = tkinter.Button(t_personal_frame, text='Back', command=self.t_volunteer_summary)
        t_back_to_summary.grid(row=14, column=1)

        # Button to go straight to edit camp
        n_to_editcamp = tkinter.Button(t_personal_frame, text='Edit camp information', command=self.t_edit_camp,
                                       height=2, width=20)
        n_to_editcamp.grid(row=2, column=1)

        n_to_editcamp = tkinter.Button(t_personal_frame, text='Create a refugee profile', command=self.t_create_refugee,
                                       height=2, width=20)
        n_to_editcamp.grid(row=3, column=1)

        # If you want to change an of your personal information which should then update the personal info dict.

    def t_personal_info_edit(self):
        for i in window.winfo_children():
            i.destroy()
        t_personal_frame = tkinter.Frame(window)
        t_personal_frame.pack()
        t_personal_labelframe = tkinter.LabelFrame(t_personal_frame)
        t_personal_labelframe.grid(row=3, column=3)
        personal_title = tkinter.Label(t_personal_frame, text='Edit details', font=('Arial Bold', 30))
        personal_title.grid(row=0, column=3, pady=30)

        #  Currently set name and current title
        current_title = tkinter.Label(t_personal_labelframe, text='Current details', font=('TkinterDefault', 20))
        current_title.grid(row=4, column=2)

        preset_name = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['name'],
                                    font=('TkinterDefault', 15))
        preset_name.grid(row=5, column=2, padx=5)

        # Edit column title
        edit_title = tkinter.Label(t_personal_labelframe, text='Edit', font=('TkinterDefault', 20))
        edit_title.grid(row=4, column=3, padx=5)

        # Name entry box
        self.t_personal_nameEntry = tkinter.Entry(t_personal_labelframe, text='name')
        self.t_personal_nameEntry.grid(row=5, column=3)

        # Email header/label
        # t_personal_email = tkinter.Label(t_personal_labelframe, text=' Edit Email address')
        # Current email
        personal_email = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['Email Address'],
                                       font=('TkinterDefault', 15))
        personal_email.grid(row=7, column=2, padx=5)

        # Email entry box
        self.t_personal_emailEntry = tkinter.Entry(t_personal_labelframe)
        self.t_personal_emailEntry.grid(row=7, column=3)
        # t_phonenumber = tkinter.Label(t_personal_labelframe, text='Edit Phone number')

        # Phone number Entry and label
        phone_number = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['Phone Number'],
                                     font=('TkinterDefault', 15))
        phone_number.grid(row=9, column=2, padx=5)

        self.t_phonenumberEntry = tkinter.Entry(t_personal_labelframe)
        self.t_phonenumberEntry.grid(row=9, column=3)

        # Commitment label
        commitment_label = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['Commitment'],
                                         font=('TkinterDefault', 15))
        commitment_label.grid(row=11, column=2, padx=5)

        # Commitment type entry
        self.t_commitmentEntry = ttk.Combobox(t_personal_labelframe, values=['Full time', 'Part time', 'Occasional'],
                                              state='readonly')
        self.t_commitmentEntry.grid(row=11, column=3)

        # Work type label
        work_type_label = tkinter.Label(t_personal_labelframe, text=self.y_personal_info[self.username]['Work Type'],
                                        font=('TkinterDefault', 15))
        work_type_label.grid(row=13, column=2, padx=5)

        # Work type entry
        self.t_worktypeEntry = ttk.Combobox(t_personal_labelframe, values=['Medical Aid', 'Food counselling'],
                                            state='readonly')
        self.t_worktypeEntry.grid(row=13, column=3)

        # Store details box
        t_store_details = tkinter.Button(t_personal_frame, text='Store details', command=self.t_personal_info_dict,
                                         height=1, width=20)
        t_store_details.grid(row=17, column=3)

        # Back to details page
        t_back_to_details = tkinter.Button(t_personal_frame, text='Back to view details',
                                           command=self.t_personal_information_base)
        t_back_to_details.grid(row=17, column=1)

        # Back to summary page
        back_to_summary = tkinter.Button(t_personal_frame, text='Back to summary page',
                                         command=self.t_volunteer_summary)
        back_to_summary.grid(row=17, column=5)

    def t_personal_info_dict(self):
        try:
            # Update self.y_personal_info dictionary
            if self.t_personal_nameEntry.get() == '':
                name = self.y_personal_info[self.username]['name']
            else:
                name = self.t_personal_nameEntry.get()
            if self.t_personal_emailEntry.get() == '':
                email = self.y_personal_info[self.username]['Email Address']
            else:
                email = self.t_personal_emailEntry.get()
            if self.t_phonenumberEntry.get() == '':
                phone = self.y_personal_info[self.username]['Phone Number']
            else:
                phone = self.t_phonenumberEntry.get()
            if self.t_commitmentEntry.get() == '':
                commitment = self.y_personal_info[self.username]['Commitment']
            else:
                commitment = self.t_commitmentEntry.get()
            if self.t_worktypeEntry.get() == '':
                work = self.y_personal_info[self.username]['Work Type']
            else:
                work = self.t_worktypeEntry.get()

            # If entered non-alpha characters, raise error
            if re.search(r'^[A-Za-z]', name):
                self.y_personal_info[self.username]['name'] = name.strip()
            else:
                raise invalid_name

            # If entered non-number characters, raise error
            if re.search(r'^[0-9]+', phone):
                self.y_personal_info[self.username]['Phone Number'] = phone
            else:
                raise invalid_phone_number

            # Make sure they include correct email format
            if re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
                self.y_personal_info[self.username]['Email Address'] = email
            else:
                raise invalid_email

            self.y_personal_info[self.username]['Commitment'] = commitment
            self.y_personal_info[self.username]['Work Type'] = work

            new_data = pd.DataFrame.from_dict(self.y_personal_info, orient='index')
            new_data.index.name = 'Username'
            new_data.to_csv('volunteer_info.csv')


            self.t_personal_information_base()

        except(invalid_email):
            tkinter.messagebox.showinfo(title='Invalid Email', message='Please enter a valid email address')
        except(invalid_phone_number):
            tkinter.messagebox.showinfo(title='Invalid Phone Number', message='Please enter a valid phone number')
        except(invalid_name):
            tkinter.messagebox.showinfo(title='Invalid Name', message='Please enter a valid name')

        except FileNotFoundError:
            pass

    # Edit camp information page
    def t_edit_camp(self):
        for i in window.winfo_children():
            i.destroy()
        t_edit_campframe = tkinter.Frame(window)
        t_edit_campframe.pack()
        t_edit_camp_title = tkinter.Label(t_edit_campframe, text='Edit camp', font=('TkDefaultFont', 30), pady=30)
        t_edit_camp_title.grid(row=0, column=1)
        t_camp_labelframe = tkinter.LabelFrame(t_edit_campframe, text=self.y_camp_info['ID']['Country'],
                                               font=('TkDefaultFont', 20))
        t_camp_labelframe.grid(row=1, column=1)

        # Current amount you can add
        t_current_capacity = tkinter.Label(t_camp_labelframe, text='Current Capacity: ', font=('TkDefaultFont', 15))
        t_current_capacity.grid(row=2, column=3)
        t_capacity_label = tkinter.Label(t_camp_labelframe, text=self.y_camp_info['ID']['Max Capacity'],
                                         font=('TkDefaultFont', 15))
        t_capacity_label.grid(row=2, column=5)

        # Capacity for new refugees box and label
        t_camp_capacity = tkinter.Label(t_camp_labelframe,
                                        text=f'Add new refugees: ')  # Need to add current number here next to it so Ying add that in with dictionary or however.
        t_camp_capacity.grid(row=4, column=3, padx=5)
        self.t_camp_campacitybox = ttk.Spinbox(t_camp_labelframe, from_=0, to=1000, style='info.TSpinbox')
        self.t_camp_campacitybox.grid(row=4, column=5, padx=5)

        # Request type of resource box and label
        n_resource_type = tkinter.Label(t_camp_labelframe, text='Select resource type you would like to request')
        n_resource_type.grid(row=5, column=3, padx=5)
        self.n_resource_typebox = ttk.Combobox(t_camp_labelframe,
                                               values=['Food packets', 'Medical supplies', 'Water and sanitation',
                                                       'Clothing', 'Shelter materials'])
        self.n_resource_typebox.grid(row=5, column=5, padx=5)

        # Request quantity of resource box and label
        n_resource_quantity = tkinter.Label(t_camp_labelframe, text='Select quantity of resource')
        n_resource_quantity.grid(row=6, column=3, padx=5)
        self.n_resource_quantbox = ttk.Spinbox(t_camp_labelframe, from_=0, to=1000)
        self.n_resource_quantbox.grid(row=6, column=5, padx=5)

        n_to_personal_info = tkinter.Button(t_edit_campframe, text='Personal information',
                                            command=self.t_personal_information_base, height=2, width=20)
        n_to_personal_info.grid(row=1, column=0, padx=10)

        n_to_refugee = tkinter.Button(t_edit_campframe, text='Create a refugee profile', command=self.t_create_refugee,
                                      height=2, width=20)
        n_to_refugee.grid(row=2, column=0, padx=10)

        # Save changes button, need to add this to a dictionary.
        t_save_changes = tkinter.Button(t_edit_campframe, text='Save changes', command=self.na_refugee_info_dict)
        t_save_changes.grid(row=14, column=1, padx=5, pady=10)

    def na_refugee_info_dict(self):
        try:
            with open('Camp.pickle', 'wb') as f:
                refugee_change = self.t_camp_campacitybox.get()
                refugee_capacity = self.y_camp_info['ID']['Max Capacity']

                if int(refugee_capacity) - int(refugee_change) > -1:
                    refugee_capacity -= int(refugee_change)
                else:
                    raise t_incorrect_details

                request_resources_type = self.n_resource_typebox.get()
                request_resources_quant = self.n_resource_quantbox.get()
                current_resources = self.y_camp_info['ID'][request_resources_type]
                current_resources += int(request_resources_quant)
                self.y_camp_info['ID']['Max Capacity'] = refugee_capacity
                self.y_camp_info['ID'][request_resources_type] = current_resources
                pickle.dump(self.y_camp_info, f)

                changes = f"Remaining Refugee Capacity = {refugee_capacity}\n {request_resources_type}: {current_resources}"

                messagebox.showinfo(title="Saved", message=f"Changes have been saved\n{changes}")

                self.t_edit_camp()

        except(t_incorrect_details):
            tkinter.messagebox.showinfo(title='Current Capacity Exceeded',
                                        message='The current capacity is exceeded, if you require more refugees, please contact the administrator')

    def t_create_refugee(self):
        for i in window.winfo_children():
            i.destroy()

        # Main frame for this whole page
        refugeeframe = tkinter.Frame(window)
        refugeeframe.pack()

        # Title for the page
        refugee_title = tkinter.Label(refugeeframe, text='Create Refugee Profile', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=1, pady=30)

        # Label frame for this page that then stores all of the labels and entries
        refugee_labelframe = tkinter.LabelFrame(refugeeframe)
        refugee_labelframe.grid(row=1, column=1)

        # Family members
        family_label = tkinter.Label(refugee_labelframe, text='Enter total number members in this family',
                                     font=('TkinterDefault', 15))
        family_label.grid(row=5, column=3, padx=5)
        self.family_labelbox = ttk.Spinbox(refugee_labelframe, from_=0, to=20, style='info.TSpinbox')
        self.family_labelbox.grid(row=5, column=4, padx=5)

        # Medical conditions, we need to add dictionaries and everything for this
        medical_conditionslabel = tkinter.Label(refugee_labelframe,
                                                text='Enter any medical condition(s) for each family member. If none, please enter \"none\"',
                                                font=("TkinterDefault", 15))
        medical_conditionslabel.grid(row=7, column=3, padx=5)
        self.t_medical_conditionsEntry = tkinter.Entry(refugee_labelframe)
        self.t_medical_conditionsEntry.grid(row=7, column=4, padx=5)

        # Languages spoken by refugees
        languages_spokenlabel = tkinter.Label(refugee_labelframe,
                                              text='Please select main language spoken in the family',
                                              font=('TkinterDefault', 15))
        languages_spokenlabel.grid(row=9, column=3, padx=5)
        self.t_languages_spokenEntry = ttk.Combobox(refugee_labelframe,
                                                    values='English Chinese Hindi Spanish French Arabic Bengali Portuguese Russian Urdu Indonesian German Swahili Marathi Tamil Telugu Turkish Vietnamese Korean Italian Thai Gujarati Persian Polish Pashto Kannada Ukrainian Somali Kurdish')
        self.t_languages_spokenEntry.grid(row=9, column=4, padx=5)

        # secondlanguage entry box
        second_languagelabel = tkinter.Label(refugee_labelframe,
                                             text='Please enter any other languages spoken by each family member. If none, please enter \'none\'',
                                             font=('TkinterDefault', 15))
        second_languagelabel.grid(row=11, column=3, padx=5)
        self.t_second_languageEntry = tkinter.Entry(refugee_labelframe)
        self.t_second_languageEntry.grid(row=11, column=4, padx=5)

        na_store_details = tkinter.Button(refugee_labelframe, text="Store refugee info",
                                          command=self.na_refugee_info_dict, height=1, width=20)
        na_store_details.grid(row=17, column=3)

        na_save_changes = tkinter.Button(refugee_labelframe, text='Save changes', command='Store in dictionary')
        na_save_changes.grid(row=13, column=1, padx=5, pady=10)

        # Back button
        na_back_button = tkinter.Button(refugee_labelframe, text='Back', command=self.t_volunteer_summary)
        na_back_button.grid(row=13, column=3, padx=5, pady=10)

        # Button to go back to personal information
        n_to_personal_info = tkinter.Button(refugeeframe, text='Personal information',
                                            command=self.t_personal_information_base, height=2, width=20)
        n_to_personal_info.grid(row=1, column=0, padx=10)

        # Button to go straight to edit camp
        n_to_editcamp = tkinter.Button(refugeeframe, text='Edit camp information', command=self.t_edit_camp, height=2,
                                       width=20)
        n_to_editcamp.grid(row=2, column=0)

    def t_display_resources(self):
        for i in window.winfo_children():
            i.destroy()

        # Creating the main label
        resources_frame = tkinter.Frame(window)
        resources_frame.pack()

        # Title
        resources_title = tkinter.Label(resources_frame, text='Resources Currently Available',
                                        font=('TkinterDefault', 30))
        resources_title.grid(row=0, column=1)

        # Creating label frame
        resources_labelframe = tkinter.LabelFrame(resources_frame)
        resources_labelframe.grid(row=1, column=1)

        # Not sure what is meant to go in here at the moment so will just leave it for now.
        t_back_button = tkinter.Button(resources_frame, text='Back', command=self.t_volunteer_summary)
        t_back_button.grid(row=9, column=0, padx=5, pady=10)


class na_admin_main_page(na_case_sensitive, na_no_text, na_incorrect_details, na_invalid_name, LandingPage):

    def __init__(self) -> None:
        self.na_admin_login()

    def na_admin_login(self):
        for i in window.winfo_children():
            i.destroy()

        # admin frame put on screen
        self.na_admin_frame = tkinter.Frame(window)
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
        self.na_entry_button = tkinter.Button(self.na_admin_frame, text='Login', command=self.na_admin_details,
                                              height=1, width=20)
        self.na_entry_button.grid(row=5, column=0, pady=20)

        # Shows caps lock on/off
        self.label_caps = tkinter.Label(self.na_admin_frame)
        self.label_caps.grid(row=4, column=1)
        window.bind("<KeyPress>", self.caps_lock_on)
        window.bind("<KeyRelease>", self.caps_lock_off)
        back_button = tkinter.Button(self.na_admin_frame, text='Back', command=LandingPage)
        back_button.grid(row=6, column=0, padx=10, pady=10)

        # Launches tkinter

    def na_admin_details(self):
        user = self.na_name_entry.get()
        password = self.na_password_entry.get()
        if (user == 'admin') and (password == '111'):
            AdminHomepage()

        # try:
        #     if self.username not in self.y_personal_info.keys():
        #         raise t_deleted_account
        #     elif self.y_personal_info[self.username]['Deactivated'] == True:
        #         raise t_deactivated_account
        #     else:
        #         if password == self.y_personal_info[self.username]['password']:
        #             self.t_volunteer_summary()
        #         elif password != self.y_personal_info[self.username]['password']:
        #             raise t_incorrect_details

        #     # if (username.lower() or password.lower()) in self.volunteer_dict:
        #     # raise t_case_sensitive
        # except(t_incorrect_details):
        #     tkinter.messagebox.showinfo(title='Incorrect details',
        #                                 message='The password does not match the username')
        # # except(t_case_sensitive):
        # # tkinter.messagebox.showinfo(title='Incorrect capitals', message='Check to make sure you didn\'t accidentally use caps lock')
        # except(t_deleted_account):
        #     tkinter.messagebox.showinfo(title='Username non-existent',
        #                                 message='That is not a valid volunteer username')
        # except(t_deactivated_account):
        #     tkinter.messagebox.showinfo(title='Deactivated account',
        #                                 message='Your account has been deactivated, \nPlease contact admin for more details')


class AdminHomepage(LandingPage):
    def __init__(self):
        for i in window.winfo_children():
            i.destroy()
        # self.window.geometry('1300x600')
        # window.configure(background="skyblue")
        # window.attributes('-fullscreen', True)
        self.events_dict = {}
        self.events_dict['123123231'] = {'New Camp ID': "", "Crisis type": "", "Other crisis type": "",
                                         "Description": "", "Country": "", "Other Country": "", "Name": "",
                                         "Start date": ""}

        # window.bind('<F11>', self.toggle_fullscreen)
        # window.bind('<Escape>', self.end_fullscreen)
        # window.protocol("WM_DELETE_WINDOW", self.window_exit_button)

        # MENU BAR:
        menu_bar = tk.Menu(window)
        window.config(menu=menu_bar)
        # create a menu item 1
        # file_menu = tk.Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="File", menu=file_menu)
        # file_menu.add_command(label="New Plan", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="Settings", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="Log Out", command=self.exit_and_go_back)
        # file_menu.add_separator()
        # file_menu.add_command(label="Exit", command=self.exit_software)
        # # create a menu item 2
        # file_menu = tk.Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="Edit", menu=file_menu)
        # file_menu.add_command(label="Edit Event", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="Resources", command=self.our_cmd)
        # # create a menu item 3
        # file_menu = tk.Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="View", menu=file_menu)
        # file_menu.add_command(label="View Events", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="View Summaries", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="Allocate Resources", command=self.our_cmd)
        # # create a menu item 4
        # file_menu = tk.Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="Accounts", menu=file_menu)
        # file_menu.add_command(label="Create", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="Volunteers", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="Admins", command=self.our_cmd)
        # # create a menu item 5
        # file_menu = tk.Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="Settings", menu=file_menu)
        # file_menu.add_command(label="Display", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="Audio", command=self.our_cmd)
        # # create a menu item 6
        # file_menu = tk.Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label="Help", menu=file_menu)
        # file_menu.add_command(label="Contact Support", command=self.our_cmd)
        # file_menu.add_separator()
        # file_menu.add_command(label="About", command=self.our_cmd)

        # WELCOME TITLE
        self.admin_welcome_title = tk.Label(window, text='Welcome to the admin portal', font=('Arial Bold', 40))
        self.admin_welcome_title.grid(row=0, column=3, pady=30)

        # MAIN BUTTONS
        # Create new event button
        self.btn_create_event = tk.Button(window, text="Create new event", command=self.new_plan)
        self.btn_create_event.grid(row=3, column=3, pady=5)

        # End an event button
        self.btn_end_event = tk.Button(window, text="End an event", command=self.end_event)
        self.btn_end_event.grid(row=5, column=3, pady=5)

        # View summaries button
        self.btn_view_summaries = tk.Button(window, text="View Events", command=self.view_events)
        self.btn_view_summaries.grid(row=7, column=3, pady=5)

        # Edit volunteer accounts button
        self.btn_edit_accounts = tk.Button(window, text="Edit volunteer accounts", command=self.edit_accounts)
        self.btn_edit_accounts.grid(row=9, column=3, pady=5)

        # Allocate resources button
        self.btn_allocate_resources = tk.Button(window, text="Allocate resources", command=self.allocate_resources)
        self.btn_allocate_resources.grid(row=11, column=3, pady=5)

        back_button = tkinter.Button(window, text='Back to Login', command=LandingPage)
        back_button.grid(row=17, column=1, padx=5, pady=10)

    # For caps lock on/off
    def new_plan(self):
        for i in window.winfo_children():
            i.destroy()

        new_plan_frame = tkinter.Frame(window)
        new_plan_frame.grid()

        def new_window():
            new_window = tkinter.Toplevel()
            new_window.title("Calendar Humanitarian Crisis")

            # new_window = tk.Toplevel()
            # new_window.title('start date window')
            # new_window.config(width=300, height=200)

            # add functions for the date
            def is_valid_date(day, month, year):
                try:
                    date_str = f"{day} {month} {year}"
                    selected_date = datetime.strptime(date_str, "%d %B %Y").date()
                    current_date = datetime.now().date()
                    return selected_date >= current_date
                    return True
                except ValueError:
                    return False

            def get_selected_date():
                day = self.day_combobox.get()
                month = self.month_combobox.get()
                year = self.year_combobox.get()
                new_window.destroy()

                if is_valid_date(day, month, year):
                    selected_date = f"{day} {month} {year}"
                    messagebox.showinfo("Selected Date", f"start date of event: {selected_date}")
                else:
                    messagebox.showerror("Invalid Date", "Please select a valid date.")

            current_date = datetime.now()
            current_year = current_date.year
            current_month = current_date.strftime("%B")
            current_day = current_date.day

            day_label = ttk.Label(new_window, text="Day:")
            day_label.grid(row=0, column=0)
            self.day_combobox = ttk.Combobox(new_window, values=list(range(1, 32)))
            self.day_combobox.grid(row=0, column=1)
            self.day_combobox.set(current_day)

            month_label = ttk.Label(new_window, text="Month:")
            month_label.grid(row=0, column=2)
            self.month_combobox = ttk.Combobox(new_window,
                                               values=["January", "February", "March", "April", "May", "June", "July",
                                                       "August", "September", "October", "November", "December"])
            self.month_combobox.grid(row=0, column=3)
            self.month_combobox.set(current_month)

            year_label = ttk.Label(new_window, text="Year:")
            year_label.grid(row=0, column=4)
            self.year_combobox = ttk.Combobox(new_window, values=list(range(current_year, current_year + 5)))
            self.year_combobox.grid(row=0, column=5)
            self.year_combobox.set(current_year)

            get_date_button = ttk.Button(new_window, text="select date", command=get_selected_date)
            get_date_button.grid(row=1, column=0, columnspan=6, pady=10)

            # Create a button to destroy this window
            button_close = ttk.Button(
                new_window,
                text="Close window",
                command=new_window.destroy)
            button_close.place(x=75, y=75)

        button_open = ttk.Button(
            new_plan_frame,
            text="Select Date",
            command=new_window)

        button_open.place(x=100, y=100)

        refugee_title = tkinter.Label(new_plan_frame, text='Create New Plan', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=1, pady=30)

        camp_ID_label = tkinter.Label(new_plan_frame, text='New Camp ID', font=('TkinterDefault', 15))
        camp_ID_label.grid(row=3, column=3)
        self.camp_IDbox = tkinter.Entry(new_plan_frame)
        self.camp_IDbox.grid(row=3, column=4, padx=5)

        crisis_type_label = tkinter.Label(new_plan_frame, text='Crisis Type', font=('TkinterDefault', 15))
        crisis_type_label.grid(row=5, column=3, padx=5)
        crisis_type = ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]
        self.crisis_type_combobox = ttk.Combobox(new_plan_frame, values=crisis_type)
        self.crisis_type_combobox.grid(row=5, column=4, padx=5)

        other_crisis_label = tkinter.Label(new_plan_frame, text='If crisis type not in list, please enter here',
                                           font=('TkinterDefault', 15))
        other_crisis_label.grid(row=7, column=3, padx=5)
        self.other_crisis_label_Entry = tkinter.Entry(new_plan_frame)
        self.other_crisis_label_Entry.grid(row=7, column=4, padx=5)
        self.other_crisis_label_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        description_label = tkinter.Label(new_plan_frame, text='Description', font=('TkinterDefault', 15))
        description_label.grid(row=9, column=3, padx=5)
        self.description_label_Entry = tkinter.Entry(new_plan_frame)
        self.description_label_Entry.grid(row=9, column=4, padx=5)
        self.description_label_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        country_label = tkinter.Label(new_plan_frame, text='Country of crisis', font=('TkinterDefault', 15))
        country_label.grid(row=11, column=3, padx=5)
        self.country_Entry = ttk.Combobox(new_plan_frame, values=[
            "Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan", "Democratic Republic of the Congo",
            "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic", "Libya",
            "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon", "Zimbabwe", "Eritrea",
            "North Korea", "Eswatini", "Zambia", "Malawi"])
        self.country_Entry.grid(row=11, column=4, padx=5)

        other_country_label = tkinter.Label(new_plan_frame, text='If country not in list, please enter here',
                                            font=('TkinterDefault', 15))
        other_country_label.grid(row=13, column=3, padx=5)
        self.other_country_Entry = tkinter.Entry(new_plan_frame)
        self.other_country_Entry.grid(row=13, column=4, padx=5)
        self.other_country_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        created_by_label = tkinter.Label(new_plan_frame, text='Enter your name', font=("TkinterDefault", 15))
        created_by_label.grid(row=15, column=3, padx=5)
        self.created_by_Entry = tkinter.Entry(new_plan_frame)
        self.created_by_Entry.grid(row=15, column=4, padx=5)

        save_plan_button = tkinter.Button(new_plan_frame, text="Save plan", command=self.plan_dict, height=1, width=20)
        save_plan_button.grid(row=17, column=3)

        back_button = tkinter.Button(new_plan_frame, text='Back to Home', command=AdminHomepage)
        back_button.grid(row=17, column=1, padx=5, pady=10)

    def character_limit(self):
        from tkinter import END
        if len(self.description_label_Entry.get()) > 100:
            self.description_label_Entry.delete(100, END)

    def plan_dict(self):
        try:
            self.camp_ID = self.camp_IDbox.get()
            self.events_dict[self.camp_ID] = {'New Camp ID': "", "Crisis type": "", "Other crisis type": "",
                                              "Description": "", "Country": "", "Other Country": "", "Name": "",
                                              "Start date": ""}
            crisis_type = self.crisis_type_combobox.get()
            other_crisis = self.other_crisis_label_Entry.get()
            description = self.description_label_Entry.get()
            country = self.country_Entry.get()
            other_country = self.other_country_Entry.get()
            admin_name = self.created_by_Entry.get()
            # start_day = self.day_combobox.get()
            self.events_dict[self.camp_ID]['New Camp ID'] = self.camp_ID
            self.events_dict[self.camp_ID]['Crisis type'] = crisis_type
            self.events_dict[self.camp_ID]['Other crisis type'] = other_crisis
            self.events_dict[self.camp_ID]['Description'] = description
            self.events_dict[self.camp_ID]["Country"] = country
            self.events_dict[self.camp_ID]["Other Country"] = other_country
            self.events_dict[self.camp_ID]["Name"] = admin_name
            print(self.events_dict)
        except:
            self.events_dict = {'New Camp ID': "", "Crisis type": "", "Other crisis type": "", "Description": "",
                                "Country": "", "Other Country": "", "Name": "", "Start date": ""}
        print(list(self.events_dict.keys()))

    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on')

    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='')

    def end_event(self):
        pass

    def view_events(self):
        for i in window.winfo_children():
            i.destroy()
        # All T

        events_title = tkinter.Label(window, text='Events', font=('TkDefaultFont', 30))
        events_title.grid(row=0, column=5)
        self.view_events_frame = tkinter.LabelFrame(window)
        self.view_events_frame.grid(row=1, column=3)

        # Getting the camp ID

        print(list(self.events_dict.keys()))
        self.get_camp_ID = ttk.Combobox(self.view_events_frame, values=[list(self.events_dict.keys())])
        self.get_camp_ID.grid(row=2, column=3, padx=10, pady=10)

        # Showing the camp ID
        show_information = tkinter.Button(self.view_events_frame, text='Show information', command=self.t_events_labels)
        show_information.grid(row=3, column=3)
        back_button = tkinter.Button(self.view_events_frame, text='Back to Home', command=AdminHomepage)
        back_button.grid(row=17, column=1, padx=5, pady=10)

    def t_events_labels(self):

        chosen_id = self.get_camp_ID.get()

        events_camp_label = tkinter.Label(self.view_events_frame, text='Camp ID: ', font=('TkDefaultFont', 15))
        events_camp_label.grid(row=5, column=3, padx=10, pady=10)
        if chosen_id != '':
            events_camp_info = tkinter.Label(self.view_events_frame, text=self.events_dict[chosen_id]['New Camp ID'],
                                             font=('TkDefaultFont', 15))
            events_camp_info.grid(row=5, column=4, padx=10, pady=10)

            # Crisistype label and info
            events_crisis = tkinter.Label(self.view_events_frame, text='Crisis type: ', font=('TkDefaultFont', 15))
            events_crisis.grid(row=6, column=3, padx=10, pady=10)
            events_crisis_info = tkinter.Label(self.view_events_frame, text=self.events_dict[chosen_id]['Crisis type'])
            events_crisis_info.grid(row=6, column=4, padx=10, pady=10)

            # Other crisis type
            if self.events_dict[chosen_id]['Other crisis type'] != "":
                events_other_crisis = tkinter.Label(self.view_events_frame,
                                                    text=self.events_dict[chosen_id]['Other crisis type'],
                                                    font=('TkDefaultFont', 15))
                events_other_crisis.grid(row=7, column=4, padx=10, pady=10)
            # Description
            events_description_label = tkinter.Label(self.view_events_frame, text='Description: ',
                                                     font=('TkDefaultFont', 15))
            events_description_label.grid(row=8, column=3, padx=10, pady=10)
            events_description_info = tkinter.Label(self.view_events_frame,
                                                    text=self.events_dict[chosen_id]['Description'],
                                                    font=('TkDefaultFont', 15))
            events_description_info.grid(row=8, column=4, padx=10, pady=10)

            events_country_label = tkinter.Label(self.view_events_frame, text='Countries: ', font=('TkDefaultFont', 15))
            events_country_label.grid(row=9, column=3)
            events_country_info = tkinter.Label(self.view_events_frame, text=self.events_dict[chosen_id]["Country"],
                                                font=('TkDefaultFont', 15))
            events_country_info.grid(row=9, column=4, padx=10, pady=10)
            if self.events_dict[chosen_id]["Other Country"] != '':
                events_other_country = tkinter.Label(self.view_events_frame,
                                                     text=self.events_dict[chosen_id]['Other Country'])
                events_other_country.grid(row=9, column=4)

    def edit_accounts(self):
        pass

    def allocate_resources(self):
        pass


LandingPage()
