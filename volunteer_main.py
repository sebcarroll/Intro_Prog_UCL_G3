import tkinter as tk
from tkinter import ttk
from volunteer_login_page import VolunteerLoginPage
import pickle
import os
from VolunteerSubpages.personal_information import personal_information
from VolunteerSubpages.edit_personal_information import edit_personal_info, store_personal_details
from VolunteerSubpages.edit_camp_details import edit_camp_details
from VolunteerSubpages.new_refugee import new_refugee, na_refugee_info_dict
from VolunteerSubpages.resource_display import resource_display

class invalid_email(Exception):
    pass
class invalid_phone_number(Exception):
    pass
class invalid_name(Exception):
    pass

class VolunteerHomepage(VolunteerLoginPage):
    def __init__(self, root, username, go_to_landing_page):
        #super().__init__(root)
        VolunteerLoginPage.__init__(self, root, go_to_landing_page)
        self.root = root
        self.username = username
        self.personal_entry_widgets = None
        self.refugee_entry_widgets = None
        self.go_to_landing_page = go_to_landing_page
        self.window = tk.Toplevel(self.root)
        self.window.title('Volunteer Homepage')
        self.window.geometry('1300x600')

        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Log Out", command=self.exit_and_go_back)

        self.t_summary_title = tk.Label(self.window, text='Welcome to the volunteer portal', font=('Arial Bold', 40))
        self.t_summary_title.grid(row=0, column=3, pady=30)

        self.t_summary_editdetails = tk.Button(self.window, text='Personal information', command=self.t_personal_information_base, height=2, width=20)
        self.t_summary_editdetails.grid(row=3, column=3, pady=5)

        self.t_summary_editcamp = tk.Button(self.window, text='Edit camp information', command=self.t_edit_camp, height=2, width=20)
        self.t_summary_editcamp.grid(row=4, column=3, pady=5)

        self.t_summary_refugee = tk.Button(self.window, text='Create a refugee profile', command=self.t_create_refugee, height=2, width=20)
        self.t_summary_refugee.grid(row=5, column=3)

        self.t_summary_resources = tk.Button(self.window, text='Display resources available', command=self.t_display_resources, height=2, width=20)
        self.t_summary_resources.grid(row=6, column=3)

        '''try:
            if os.path.getsize('data.pickle') > 0:
                with open('data.pickle', 'rb') as file:
                    print("this works")
                    self.y_personal_info = pickle.load(file)

            else:
                self.y_personal_info = {
                    'volunteer1': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '',
                                   'Commitment': '',
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False},
                    'volunteer2': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '',
                                   'Commitment': '',
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False},
                    'volunteer3': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '',
                                   'Commitment': '',
                                   'Work Type': '', 'Deactivated': True, 'Deleted': False},
                    'volunteer4': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '',
                                   'Commitment': '',
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

        self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}'''
        try:
            if os.path.getsize('refugee.pickle') > 0:
                with open('refugee.pickle', 'rb') as file:
                    self.na_refugee_info = pickle.load(file)
            else:
                self.na_refugee_info = {
                    'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                                 'Second Language': ''}
                }

            if os.path.getsize('data.pickle') > 0:
                with open('data.pickle', 'rb') as file:
                    print("this works")
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
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False},
                    '': {'password': '', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False}
                }
        except FileNotFoundError:
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
        except FileNotFoundError:
            self.na_refugee_info = {
                'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                             'Second Language': ''}}

        # Initialize y_camp_info before trying to load from the pickled file
        self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}
        # Initialize na_refugee_info before trying to load from the pickled file
        self.na_refugee_info = {
            'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                         'Second Language': ''}
        }


    # SUBPAGES WITHIN VOLUNTEER HOMEPAGE - PYTHON PACKAGE VOLUNTEER SUBPAGES:

    # Volunteer Details (personal_information.py)
    def t_personal_information_base(self):
        personal_information(self.window, self.username, self.y_personal_info, self.t_personal_info_edit, self.back_button_to_volunteer_main)

    # Edit Details (edit_personal_information.py)
    def t_personal_info_edit(self):
        self.personal_entry_widgets = edit_personal_info(self.window, self.username, self.y_personal_info, self.t_personal_information_base, self.back_button_to_volunteer_main, self.personal_details_storage_handler)
    def personal_details_storage_handler(self, nameEntry, emailEntry, phoneEntry, commitmentEntry, worktypeEntry):
        store_personal_details(self.username, self.y_personal_info, nameEntry, emailEntry, phoneEntry, commitmentEntry, worktypeEntry)


    # Edit Camp Info (edit_camp_details.py)
    def t_edit_camp(self):
        edit_camp_details(self.window, self.y_camp_info, self.back_button_to_volunteer_main)



    # Create Refugee (new_refugee.py)
    def t_create_refugee(self):
        self.refugee_entry_widgets = new_refugee(self.window, self.y_camp_info, self.na_refugee_info, self.back_button_to_volunteer_main, self.refugee_details_storage_handler)
    def refugee_details_storage_handler(self, camp_ID, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry):
        na_refugee_info_dict(self.na_refugee_info, camp_ID, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry)




    # Display Resources (resource_display.py)
    def t_display_resources(self):
        resource_display(self.window, self.back_button_to_volunteer_main)




    # NAVIGATION - VOLUNTEER USERS:

    def back_button_to_volunteer_main(self):
        # Clear current contents
        for widget in self.window.winfo_children():
            widget.grid_forget()
        # Repopulate main page
        self.t_summary_title.grid(row=0, column=3, pady=30)
        self.t_summary_editdetails.grid(row=3, column=3, pady=5)
        self.t_summary_editcamp.grid(row=4, column=3, pady=5)
        self.t_summary_refugee.grid(row=5, column=3)
        self.t_summary_resources.grid(row=6, column=3)

    def exit_and_go_back(self):
        self.window.destroy()
        self.go_to_landing_page()

    def destroy(self):
        self.window.destroy()

