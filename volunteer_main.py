import tkinter as tk
from tkinter import ttk, PhotoImage
from volunteer_login_page import VolunteerLoginPage
from tkinter import messagebox
import pandas as pd
import os
from VolunteerSubpages.personal_information import personal_information
from VolunteerSubpages.edit_personal_information import edit_personal_info, store_personal_details
from VolunteerSubpages.edit_camp_details import edit_camp_details
from VolunteerSubpages.new_refugee import new_refugee, na_refugee_info_dict
from VolunteerSubpages.resource_display import resource_display
from VolunteerSubpages.refugee_display import RefugeeDisplay
# Import for menu commands
from admin_help import AdminHelp
from general_pie_charts import SummaryCharts
import csv

class invalid_email(Exception):
    pass
class invalid_phone_number(Exception):
    pass
class invalid_name(Exception):
    pass

class VolunteerHomepage():
    def __init__(self, root, username, go_to_landing_page):
        self.root = root
        self.username = username
        self.personal_entry_widgets = None
        self.refugee_entry_widgets = None
        self.go_to_landing_page = go_to_landing_page

        self.window = tk.Toplevel(self.root)
        self.window.title('Volunteer Homepage')
        self.window.geometry('1400x700')

        # Default theme
        # self.default_bg = self.window.cget('bg')
        self.current_theme = tk.StringVar(value='no_theme')
        self.apply_theme('no_theme')

        #self.camp_id_label = self.get_camp_id_for_volunteer()

        self.admin_help = AdminHelp(self.window, self.back_button_to_volunteer_main)
        self.charts = SummaryCharts(self.window, self.back_button_to_volunteer_main)
        self.refugee_display_instance = RefugeeDisplay(self.window, self.back_button_to_volunteer_main, self.get_current_camp_id)

        self.camp_id_label = self.get_camp_id_for_volunteer()
        self.show_camp_id_label = None

        self.window.protocol("WM_DELETE_WINDOW", self.window_exit_button)

        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Home", command=self.back_button_to_volunteer_main)
        file_menu.add_command(label="New Refugee", command=self.t_create_refugee)
        file_menu.add_separator()
        #file_menu.add_command(label="Settings", command=self.do_nothing)
        file_menu.add_command(label="Log Out", command=self.exit_and_go_back)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_software)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=file_menu)
        file_menu.add_command(label="Edit Camp", command=self.t_edit_camp)
        file_menu.add_separator()
        file_menu.add_command(label="Edit Profile", command=self.t_personal_information_base)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=file_menu)
        file_menu.add_command(label="View Refugees", command=self.display_refugees)
        file_menu.add_separator()
        file_menu.add_command(label="View Resources", command=self.t_display_resources)
        file_menu.add_separator()
        file_menu.add_command(label="View Charts", command=lambda: self.generate_chart_window())

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_command(label="Display", command=self.open_theme_window)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=file_menu)
        file_menu.add_command(label="Information", command=self.help_info)
        file_menu.add_command(label="About", command=self.help_about)
        file_menu.add_separator()
        file_menu.add_command(label="Support", command=self.help_support)


        try:
            self.y_personal_info = pd.read_csv('volunteer_info.csv', index_col='Username', dtype={'Phone Number': str})
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
        self.camp_id_label = self.get_camp_id_for_volunteer()
        self.show_camp_id_label = None

        self.t_summary_title = tk.Label(self.window, text='Welcome to the Volunteer Portal', font=('Arial Bold', 40),
                                        bg='grey', fg='white', relief=tk.RAISED, borderwidth=5)
        self.t_summary_title.grid(row=0, column=0, columnspan=9, sticky='nsew', padx=10, pady=20)
        self.t_summary_title.configure(background='grey')

        self.show_camp_id_label = tk.Label(self.window, text=f"{self.camp_id_label}", font=("Arial Bold", 15), fg="black", relief=tk.RAISED, borderwidth=5)
        self.show_camp_id_label.grid(row=2, column=4, pady=10, ipadx=0, ipady=0)



        self.t_summary_editdetails = tk.Button(self.window, text='Personal Information',
                                               command=self.t_personal_information_base)
        self.t_summary_editdetails.grid(row=3, column=4, pady=(30, 10), ipadx=98, ipady=25)
        self.image1 = PhotoImage(file="Images/personal_info.png").subsample(4, 4)
        image_label = tk.Label(self.window, image=self.image1)
        image_label.grid(row=3, column=3, pady=(30, 10))

        self.t_summary_editcamp = tk.Button(self.window, text='Edit Camp Information', command=self.t_edit_camp)
        self.t_summary_editcamp.grid(row=4, column=4, pady=10, ipadx=93, ipady=25)
        self.image2 = PhotoImage(file="Images/camps.png").subsample(4, 4)
        image_label = tk.Label(self.window, image=self.image2)
        image_label.grid(row=4, column=3, pady=10)

        self.t_summary_refugee = tk.Button(self.window, text='Create a Refugee Profile', command=self.t_create_refugee)
        self.t_summary_refugee.grid(row=5, column=4, pady=10, ipadx=90, ipady=25)
        self.image3 = PhotoImage(file="Images/add_refugee.png").subsample(4, 4)
        image_label = tk.Label(self.window, image=self.image3)
        image_label.grid(row=5, column=3, pady=10)

        self.t_summary_resources = tk.Button(self.window, text='Display Resources Available',
                                             command=self.t_display_resources)
        self.t_summary_resources.grid(row=6, column=4, pady=10, ipadx=80, ipady=25)
        self.image4 = PhotoImage(file="Images/resource_allocation.png").subsample(4, 4)
        image_label = tk.Label(self.window, image=self.image4)
        image_label.grid(row=6, column=3, pady=10)

        self.summary_refugees = tk.Button(self.window, text='Display Refugees Created',
                                             command=self.display_refugees)
        self.summary_refugees.grid(row=7, column=4, pady=(10, 30), ipadx=85, ipady=25)
        self.image5 = PhotoImage(file="Images/new_refugees.png").subsample(4, 4)
        image_label = tk.Label(self.window, image=self.image5)
        image_label.grid(row=7, column=3, pady=(10, 30))

        for i in range(8):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(9):
            self.window.grid_columnconfigure(i, weight=1)


    def get_current_camp_id(self):
        with open("volunteer_info.csv", 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row and row[0].strip() == self.username:
                    # Camp ID is the second value (index 1)
                    self.camp_id = row[1].strip()
                    # Check if the camp ID is blank
                    if not self.camp_id:
                        return None
                    self.camp_id = round(float(self.camp_id))
                    self.camp_ID_label = self.camp_id
                    return self.camp_id
            # Return "No camp ID assigned" if the loop completes without finding a matching volunteer
            return None

    def get_camp_id_for_volunteer(self):
        with open("volunteer_info.csv", 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:

                if row and row[0].strip() == self.username:
                    # Camp ID is the second value (index 1)
                    self.camp_id = row[1].strip()

                    # Check if the camp ID is blank
                    if not self.camp_id:
                        return "NO CAMP ID ASSIGNED"

                    self.camp_id = round(float(self.camp_id))

                    self.camp_ID_label = self.camp_id
                    return f"YOUR CAMP ID: {self.camp_id}"

            # Return "No camp ID assigned" if the loop completes without finding a matching volunteer
            return "No camp ID assigned"



    # SUBPAGES WITHIN VOLUNTEER HOMEPAGE - PYTHON PACKAGE VOLUNTEER SUBPAGES:
    # Volunteer Details (personal_information.py)
    def t_personal_information_base(self):
        personal_information(self.window, self.username, self.y_personal_info, self.t_personal_info_edit, self.back_button_to_volunteer_main)

    # Edit Details (edit_personal_information.py)
    def t_personal_info_edit(self):
        self.personal_entry_widgets = edit_personal_info(self.window, self.username, self.y_personal_info, self.t_personal_information_base, self.back_button_to_volunteer_main, self.personal_details_storage_handler)
    def personal_details_storage_handler(self, nameEntry, emailEntry, phoneEntry, commitmentEntry, worktypeEntry):
        store_personal_details(self.username, self.y_personal_info, nameEntry, emailEntry, phoneEntry, commitmentEntry, worktypeEntry, self.t_personal_information_base)

    # Edit Camp Info (edit_camp_details.py)
    def t_edit_camp(self):
        edit_camp_details(self.window, self.y_camp_info, self.camp_id, self.back_button_to_volunteer_main)

    # Create Refugee (new_refugee.py)
    def t_create_refugee(self):
        self.refugee_entry_widgets = new_refugee(self.window, self.y_camp_info, self.camp_id, self.na_refugee_info, self.back_button_to_volunteer_main, self.refugee_details_storage_handler)
    def refugee_details_storage_handler(self, camp_ID, name_entry, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry):
        na_refugee_info_dict(self.na_refugee_info, camp_ID, name_entry, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry)

    # Display Resources (resource_display.py)
    def t_display_resources(self):
        resource_display(self.window, self.camp_id, self.back_button_to_volunteer_main)

    def display_refugees(self):
        # Open the resource allocation GUI
        self.refugee_display_instance.create_gui_refugee_display(self)



    # MENU COMMANDS

    def help_about(self):
        self.admin_help.about_pop_up()

    def help_info(self):
        self.admin_help.info_pop_up()

    def help_support(self):
        self.admin_help.support_pop_up()

    def generate_chart_window(self):
        self.charts.generate_charts_window()


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
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.destroy()
        #self.root.destroy()


    def open_theme_window(self):
        theme_window = tk.Toplevel(self.root)
        theme_window.title("Select Theme")
        theme_window.geometry("200x100")

        theme_window.grab_set()

        # Radio buttons for theme selection
        tk.Radiobutton(theme_window, text="Light Theme", variable=self.current_theme,
                       value='light', command=lambda: self.apply_theme('light')).pack(anchor=tk.W)
        tk.Radiobutton(theme_window, text="Dark Theme", variable=self.current_theme,
                       value='dark', command=lambda: self.apply_theme('dark')).pack(anchor=tk.W)
        tk.Radiobutton(theme_window, text="No Theme", variable=self.current_theme,
                       value='no_theme', command=lambda: self.apply_theme('no_theme')).pack(anchor=tk.W)

    def apply_theme(self, theme):
        if theme == 'dark':
            self.window.configure(bg='blue')
            # Set other widget and text colors for dark theme
        elif theme == 'light':
            self.window.configure(bg='light blue')
            # Set other widget and text colors for light theme
        else:
            self.window.configure(bg='SystemButtonFace')
