import tkinter
import pickle
import re
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


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


class tvolunteer_main_page(t_deactivated_account, t_deleted_account, t_case_sensitive, t_no_text, t_incorrect_details):

    def __init__(self) -> None:
        # Volunteer dictionary - Nested: Can access via self.y_personal_info[username][key]
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
        self.window = tkinter.Tk()
        self.window.title('Whatever')
        self.t_volunteer_login()
        self.t_details_confirmation()

    def t_volunteer_login(self):
        # Anything on window before is removed and populates with the following code
        for i in self.window.winfo_children():
            i.destroy()

        # Volunteer frame put on screen
        self.t_volunteer_frame = tkinter.Frame(self.window)
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
        self.window.bind("<KeyPress>", self.caps_lock_on)
        self.window.bind("<KeyRelease>", self.caps_lock_off)

        # Launches tkinter
        self.window.mainloop()

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
                if password == self.y_personal_info[self.username]['password']:
                    self.t_volunteer_summary()
                elif password != self.y_personal_info[self.username]['password']:
                    raise t_incorrect_details

            # if (username.lower() or password.lower()) in self.volunteer_dict:
            # raise t_case_sensitive
        except(t_incorrect_details):
            tkinter.messagebox.showinfo(title='Incorrect details', message='The password does not match the username')
        # except(t_case_sensitive):
        # tkinter.messagebox.showinfo(title='Incorrect capitals', message='Check to make sure you didn\'t accidentally use caps lock')
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
        for i in self.window.winfo_children():
            i.destroy()
        self.t_summary_frame = tkinter.Frame(self.window)
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
        self.t_summary_resources = tkinter.Button(self.t_summary_frame, text='Display resources available',
                                                  command=self.t_display_resources, height=2, width=20)
        self.t_summary_resources.grid(row=6, column=3)

    # UI for personal info - very similar to the t_volunteer_login function:
    def t_personal_information_base(self):
        for i in self.window.winfo_children():
            i.destroy()
        t_personal_frame = tkinter.Frame(self.window)
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

        # If you want to change an of your personal information which should then update the personal info dict.

    def t_personal_info_edit(self):
        for i in self.window.winfo_children():
            i.destroy()
        t_personal_frame = tkinter.Frame(self.window)
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
        self.t_worktypeEntry = ttk.Combobox(t_personal_labelframe, values=['Medical Aid', 'Food counselling'])
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
            with open('data.pickle', 'wb') as file:
                name = self.t_personal_nameEntry.get()
                email = self.t_personal_emailEntry.get()
                phone = self.t_phonenumberEntry.get()
                commitment = self.t_commitmentEntry.get()
                work = self.t_worktypeEntry.get()

                try:
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

                    self.y_personal_info[self.username]['Work Type'] = work
                    self.y_personal_info[self.username]['Commitment'] = commitment
                    self.t_personal_information_base()

                except(invalid_email):
                    tkinter.messagebox.showinfo(title='Invalid Email', message='Please enter a valid email address')
                except(invalid_phone_number):
                    tkinter.messagebox.showinfo(title='Invalid Phone Number', message='Please enter a valid phone number')
                except(invalid_name):
                    tkinter.messagebox.showinfo(title='Invalid Name', message='Please enter a valid name')

                pickle.dump(self.y_personal_info, file)
                
        except FileNotFoundError:
            pass

    # Edit camp information page
    def t_edit_camp(self):
        for i in self.window.winfo_children():
            i.destroy()
        t_edit_campframe = tkinter.Frame(self.window)
        t_edit_campframe.pack()
        t_edit_camp_title = tkinter.Label(t_edit_campframe, text='Edit camp', font=('Arial Bold', 30), pady=30)
        t_edit_camp_title.grid(row=0, column=1)
        t_camp_labelframe = tkinter.LabelFrame(t_edit_campframe)
        t_camp_labelframe.grid(row=1, column=1)

        # Camp ID box and label
        t_camp_ID_label = tkinter.Label(t_camp_labelframe, text='Camp ID')
        t_camp_ID_label.grid(row=3, column=3)
        self.t_camp_ID_box = ttk.Combobox(t_camp_labelframe, values=self.y_camp_info['Syria']['ID'])
        self.t_camp_ID_box.grid(row=3, column=4, padx=5)

        # Capacity for new refugees box and label
        t_camp_capacity = tkinter.Label(t_camp_labelframe,
                                        text='Capacity for new refugees:')  # Need to add current number here next to it so Ying add that in with dictionary or however.
        t_camp_capacity.grid(row=4, column=3, padx=5)
        self.t_camp_campacitybox = ttk.Spinbox(t_camp_labelframe, from_=0, to=1000, style='info.TSpinbox')
        self.t_camp_campacitybox.grid(row=4, column=4, padx=5)

        # Save changes button, need to add this to a dictionary.
        t_save_changes = tkinter.Button(t_edit_campframe, text='Save changes', command='Store in dictionary')
        t_save_changes.grid(row=7, column=1, padx=5, pady=10)

        # Back button
        t_back_button = tkinter.Button(t_edit_campframe, text='Back', command=self.t_volunteer_summary)
        t_back_button.grid(row=7, column=0, padx=5, pady=10)

    def t_create_refugee(self):
        for i in self.window.winfo_children():
            i.destroy()
        # Main frame for this whole page
        refugeeframe = tkinter.Frame(self.window)
        refugeeframe.pack()

        # Title for the page
        refugee_title = tkinter.Label(refugeeframe, text='Create Refugee Profile', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=1, pady=30)

        # Label frame for this page that then stores all of the labels and entries
        refugee_labelframe = tkinter.LabelFrame(refugeeframe)
        refugee_labelframe.grid(row=1, column=1)

        # Camp ID
        t_camp_ID_label = tkinter.Label(refugee_labelframe, text='Camp ID', font=('TkinterDefault', 15))
        t_camp_ID_label.grid(row=3, column=3)
        self.t_camp_IDbox = ttk.Combobox(refugee_labelframe, values=self.y_camp_info['Syria']['ID'])
        self.t_camp_IDbox.grid(row=3, column=4, padx=5)

        # Medical conditions, we need to add dictionaries and everything for this
        medical_conditionslabel = tkinter.Label(refugee_labelframe, text='Medical conditions',
                                                font=('TkinterDefault', 15))
        medical_conditionslabel.grid(row=5, column=3, padx=5)
        medical_conditonsbox = ttk.Combobox(refugee_labelframe, values='We haven\'nt come up with this dictionary yet')
        medical_conditonsbox.grid(row=5, column=4)
        # I'm going to add another box for other that pops up if their medical conditions isn't in the list
        # Just haven't decided how I want to hide it and then have it appear just yet.

        # Family members
        family_label = tkinter.Label(refugee_labelframe, text='Family members', font=('TkinterDefault', 15))
        family_label.grid(row=7, column=3, padx=5)
        family_box = ttk.Combobox(refugee_labelframe, values='We haven\'t done this yet')
        family_box.grid(row=7, column=4)
        # Also thinking of adding a similar thing to this where if they already have members in the camp its fine but if not
        # A separate box comes down that allows them to type the name into it, shouldn't be complicated I just cbf rn

        # Back button
        t_back_button = tkinter.Button(refugeeframe, text='Back', command=self.t_volunteer_summary)
        t_back_button.grid(row=9, column=0, padx=5, pady=10)

    def t_display_resources(self):
        for i in self.window.winfo_children():
            i.destroy()

        # Creating the main label
        resources_frame = tkinter.Frame(self.window)
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


tvolunteer_main_page()