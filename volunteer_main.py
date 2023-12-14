import tkinter as tk
from tkinter import ttk
from volunteer_login_page import VolunteerLoginPage
import pickle
import pandas as pd
import os
from VolunteerSubpages.personal_information import personal_information
from VolunteerSubpages.edit_personal_information import edit_personal_info, store_personal_details
from VolunteerSubpages.edit_camp_details import edit_camp_details
from VolunteerSubpages.new_refugee import new_refugee, na_refugee_info_dict
from VolunteerSubpages.resource_display import resource_display
from VolunteerSubpages.refugee_display import RefugeeDisplay
import csv

class invalid_email(Exception):
    pass
class invalid_phone_number(Exception):
    pass
class invalid_name(Exception):
    pass

class VolunteerHomepage():
    def __init__(self, root, username, go_to_landing_page):
        #super().__init__(root)
        #VolunteerLoginPage.__init__(self, root, go_to_landing_page)
        self.root = root
        self.username = username
        self.personal_entry_widgets = None
        self.refugee_entry_widgets = None
        self.go_to_landing_page = go_to_landing_page

        self.window = tk.Toplevel(self.root)
        self.window.title('Volunteer Homepage')
        self.window.geometry('1300x600')

        self.refugee_display_instance = RefugeeDisplay(self.window, self.back_button_to_volunteer_main)
        self.camp_id = self.get_camp_id_for_volunteer()

        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Refugee", command=self.do_nothing)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=self.do_nothing)
        file_menu.add_separator()
        file_menu.add_command(label="Log Out", command=self.exit_and_go_back)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_software)
        # create a menu item 2
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=file_menu)
        file_menu.add_command(label="Edit Camp", command=self.do_nothing)
        file_menu.add_separator()
        file_menu.add_command(label="Resources", command=self.do_nothing)
        # create a menu item 3
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=file_menu)
        file_menu.add_command(label="View Refugees", command=self.do_nothing)
        file_menu.add_separator()
        file_menu.add_command(label="View Resources", command=self.do_nothing)


        try:
            self.y_personal_info = pd.read_csv('volunteer_info.csv', index_col='Username')
            self.y_personal_info = self.y_personal_info.to_dict(orient='index')
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

        try:
            # Update self.t_create_refugee dictionary
            self.refugee_info = pd.read_csv('refugee_info.csv', index_col='Name')
            self.refugee_info = self.refugee_info.to_dict(orient='index')
        except FileNotFoundError:
            self.refugee_info = {
                'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                            'Second Language': ''}
                    }

            df = pd.DataFrame.from_dict(self.refugee_info, orient='index')
            df.index.name = 'Name'
            df.to_csv('refugee_info.csv', index='Name')
            self.refugee_info = pd.read_csv('refugee_info.csv')


        # Initialize y_camp_info before trying to load from the pickled file
        self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}
        # Initialize na_refugee_info before trying to load from the pickled file
        self.na_refugee_info = {
            'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                         'Second Language': ''}
        }

        self.create_gui_volunteer_main()
    def create_gui_volunteer_main(self):
        self.t_summary_title = tk.Label(self.window, text='Welcome to the volunteer portal', font=('Arial Bold', 40),
                                        bg='grey', fg='white')
        self.t_summary_title.grid(row=0, column=0, columnspan=2, sticky='news', padx=20, pady=10)
        self.t_summary_title.configure(background='grey')


        self.show_camp_id_label = tk.Label(self.window, text=f"Your camp id: {self.camp_id}", font=("Arial", 20), fg="black")
        self.show_camp_id_label.grid(row=2, column=0, pady=10, ipadx=0, ipady=0)

        self.t_summary_editdetails = tk.Button(self.window, text='Personal information',
                                               command=self.t_personal_information_base)
        self.t_summary_editdetails.grid(row=3, column=0, pady=(30, 10), ipadx=98, ipady=25)

        self.t_summary_editcamp = tk.Button(self.window, text='Edit camp information', command=self.t_edit_camp)
        self.t_summary_editcamp.grid(row=4, column=0, pady=10, ipadx=98, ipady=25)

        self.t_summary_refugee = tk.Button(self.window, text='Create a refugee profile', command=self.t_create_refugee)
        self.t_summary_refugee.grid(row=5, column=0, pady=10, ipadx=90, ipady=25)

        self.t_summary_resources = tk.Button(self.window, text='Display resources available',
                                             command=self.t_display_resources)
        self.t_summary_resources.grid(row=6, column=0, pady=10, ipadx=85, ipady=25)

        self.summary_refugees = tk.Button(self.window, text='Display Refugees Created',
                                             command=self.display_refugees)
        self.summary_refugees.grid(row=7, column=0, pady=(10, 30), ipadx=85, ipady=25)

        for i in range(8):
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_columnconfigure(0, weight=1)


    def get_camp_id_for_volunteer(self):
        with open("volunteer_info.csv", 'r') as file:
            csv_reader = csv.reader(file)

            # Name is in the first column (index 0)
            for row in csv_reader:
                if row and row[0].strip() == self.username:
                    # Camp ID is the second value (index 1)
                    return row[1].strip()

        # Return None if camp ID for that volunteer not found
        return None



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
    def refugee_details_storage_handler(self, camp_ID, name_entry, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry):
        na_refugee_info_dict(self.na_refugee_info, camp_ID, name_entry, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry)



    # Display Resources (resource_display.py)
    def t_display_resources(self):
        resource_display(self.window, self.back_button_to_volunteer_main)


    def display_refugees(self):
        # Open the resource allocation GUI
        self.refugee_display_instance.create_gui_refugee_display(self)



    # NAVIGATION - VOLUNTEER USERS:

    def back_button_to_volunteer_main(self):
        # Clear current contents
        for widget in self.window.winfo_children():
            widget.grid_forget()
        # Repopulate main page
        self.create_gui_volunteer_main()

    def do_nothing(self):
        pass

    def exit_and_go_back(self):
        self.window.destroy()
        self.go_to_landing_page()

    def destroy(self):
        self.window.destroy()

    def exit_software(self):
        self.root.quit()

    def toggle_fullscreen(self, event=None):
        self.window.attributes('-fullscreen', not self.window.attributes('-fullscreen'))

    def end_fullscreen(self, event=None):
        self.window.attributes('-fullscreen', False)
        self.window.geometry("1300x600")

    def window_exit_button(self):
        self.root.destroy()
