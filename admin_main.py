import tkinter as tk
import pandas as pd
from tkinter import messagebox, PhotoImage
# Imports for the main button commands
from AdminSubpages.create_plan import AdminCreatePlan
from AdminSubpages.admin_end_event import AdminEndEvent
from AdminSubpages.view_summaries import AdminViewSummaries
from AdminSubpages.admin_edit_details import AdminEditVolunteerDetails
from AdminSubpages.admin_resource_allocation import AdminResourceAllocation
# Imports for the menu commands
#from AdminSubpages.view_summaries_with_pie_chart import AdminViewSummariesWithCharts
from AdminSubpages.admin_refugee_profiles import AdminRefugeeDisplay
from AdminSubpages.admin_volunteer_accounts import AdminVolunteerDisplay
from admin_help import AdminHelp
from AdminSubpages.edit_camp_capacity import edit_camp_details
from AdminSubpages.admin_new_refugee import new_refugee, na_refugee_info_dict
from general_pie_charts import SummaryCharts
from country_map import CountryMap

class AdminHomepage:
    def __init__(self, root, go_to_landing_page):
        self.root = root
        self.go_to_landing_page = go_to_landing_page
        self.window = tk.Toplevel(self.root)
        self.window.title('Admin Homepage')
        self.window.geometry('1400x700')

        # Default theme
        #self.default_bg = self.window.cget('bg')
        self.current_theme = tk.StringVar(value='no_theme')
        self.apply_theme('no_theme')

        #self.window.configure(background="red")
        #self.window.attributes('-fullscreen', True)

        # Instances for button commands
        self.create_plan = AdminCreatePlan(self.window, self.back_button_to_admin_main)
        self.admin_end_event = AdminEndEvent(self.window, self.back_button_to_admin_main)
        self.admin_view_summaries = AdminViewSummaries(self.window, self.back_button_to_admin_main)
        self.admin_edit_details = AdminEditVolunteerDetails(self.window, self.back_button_to_admin_main)
        self.admin_resource_allocation = AdminResourceAllocation(self.window, self.back_button_to_admin_main)
        # Instances for menu commands
        #self.view_summaries_with_pie_chart = AdminViewSummariesWithCharts(self.window, self.back_button_to_admin_main)
        self.pie_charts_instance = SummaryCharts(self.window, self.back_button_to_admin_main)
        self.map_instance = CountryMap(self.window, self.back_button_to_admin_main)
        self.admin_display_refugees = AdminRefugeeDisplay(self.window, self.back_button_to_admin_main)
        self.admin_display_volunteers = AdminVolunteerDisplay(self.window, self.back_button_to_admin_main)
        self.admin_help = AdminHelp(self.window, self.back_button_to_admin_main)

        self.window.bind('<F11>', self.toggle_fullscreen)
        self.window.bind('<Escape>', self.end_fullscreen)

        # Set the X button to close program or stop root
        self.window.protocol("WM_DELETE_WINDOW", self.window_exit_button)

        # MENU BAR:
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Home", command=self.back_button_to_admin_main)
        file_menu.add_separator()
        file_menu.add_command(label="New Plan", command=self.create_event)
        file_menu.add_command(label="New Refugee", command=self.t_create_refugee)
        #file_menu.add_command(label="Settings", command=self.do_nothing)
        file_menu.add_separator()
        file_menu.add_command(label="Log Out", command=self.exit_and_go_back)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_software)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=file_menu)
        file_menu.add_command(label="Edit Camp Capacity", command=self.t_edit_camp)
        file_menu.add_separator()
        file_menu.add_command(label="Edit Refugee Profiles", command=self.edit_view_delete_refugee)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=file_menu)
        file_menu.add_command(label="View Summaries", command=self.view_summaries)
        file_menu.add_separator()
        file_menu.add_command(label="View Charts", command=self.view_charts)
        file_menu.add_command(label="View Map", command=self.view_map)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Accounts", menu=file_menu)
        file_menu.add_command(label="Create", command=self.create_volunteer_account)
        file_menu.add_separator()
        file_menu.add_command(label="Volunteer Accounts", command=self.edit_view_delete_volunteers)
        #file_menu.add_separator()
        #file_menu.add_command(label="Admin", command=self.do_nothing)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_command(label="Display", command=self.open_theme_window)
        #file_menu.add_separator()
        #file_menu.add_command(label="Audio", command=self.do_nothing)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=file_menu)
        file_menu.add_command(label="Information", command=self.help_info)
        file_menu.add_command(label="About", command=self.help_about)
        file_menu.add_separator()
        file_menu.add_command(label="Support", command=self.help_support)


        try:
            # Update self.t_create_refugee dictionary
            self.refugee_info = pd.read_csv('refugee_info.csv', index_col='Name')
            self.refugee_info = self.refugee_info.to_dict(orient='index')
        except FileNotFoundError:
            headers = ['Name', 'Camp ID', 'Family Members', 'Medical Conditions', 'Languages Spoken', 'Second Language']
            empty_df = pd.DataFrame(columns=headers)
            empty_df.to_csv('refugee_info.csv', index=False)

            self.refugee_info = {}

        self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}
        self.na_refugee_info = {
            'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '',
                         'Second Language': ''}
        }

        self.create_gui_admin_main()

    def create_gui_admin_main(self):
        # WELCOME TITLE
        self.admin_welcome_title = tk.Label(self.window, text='Welcome to the Admin Portal', font=('Arial', 40), bg='grey', fg='white', relief=tk.RAISED, borderwidth=5)
        self.admin_welcome_title.grid(row=0, column=0, columnspan=9, sticky="nsew", padx=10, pady=20)
        self.admin_welcome_title.configure(background="grey")

        # MAIN BUTTONS
        # Create new event button
        self.btn_create_event = tk.Button(self.window, text="Create New Event", command=self.create_event)
        self.btn_create_event.grid(row=1, column=4, pady=(50,10), ipadx=93, ipady=25)

        try:
            self.image1 = PhotoImage(file="Images/new_camp_image.png").subsample(4, 4)
            image_label = tk.Label(self.window, image=self.image1, relief=tk.RAISED, borderwidth=5)
            image_label.grid(row=1, column=3, pady=(50, 10))
        except:
            pass

        # End an event button
        self.btn_end_event = tk.Button(self.window, text="End an Event", command=self.end_event)
        self.btn_end_event.grid(row=2, column=4, pady=10, ipadx=105, ipady=25)

        try:
            self.image2 = PhotoImage(file="Images/end_camp.png").subsample(4, 4)
            image_label = tk.Label(self.window, image=self.image2, relief=tk.RAISED, borderwidth=5)
            image_label.grid(row=2, column=3, pady=10)
        except:
            pass

        # View summaries button
        self.btn_view_summaries = tk.Button(self.window, text="View Summaries", command=self.view_summaries)
        self.btn_view_summaries.grid(row=3, column=4, pady=10, ipadx=98, ipady=25)

        try:
            self.image3 = PhotoImage(file="Images/summary.png").subsample(4, 4)
            image_label = tk.Label(self.window, image=self.image3, relief=tk.RAISED, borderwidth=5)
            image_label.grid(row=3, column=3, pady=10)
        except:
            pass

        # Edit volunteer accounts button
        self.btn_edit_accounts = tk.Button(self.window, text="Edit Volunteer Accounts", command=self.edit_accounts)
        self.btn_edit_accounts.grid(row=4, column=4, pady=10, ipadx=80, ipady=25)

        try:
            self.image4 = PhotoImage(file="Images/volunteer_accounts.png").subsample(4, 4)
            image_label = tk.Label(self.window, image=self.image4, relief=tk.RAISED, borderwidth=5)
            image_label.grid(row=4, column=3, pady=10)
        except:
            pass

        # Allocate resources button
        self.btn_allocate_resources = tk.Button(self.window, text="Allocate Resources", command=self.allocate_resources)
        self.btn_allocate_resources.grid(row=5, column=4, pady=(10,50), ipadx=93, ipady=25)

        try:
            self.image5 = PhotoImage(file="Images/resource_allocation.png").subsample(4, 4)
            image_label = tk.Label(self.window, image=self.image5, relief=tk.RAISED, borderwidth=5)
            image_label.grid(row=5, column=3, pady=(10,50))
        except:
            pass


        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(9):
            self.window.grid_columnconfigure(i, weight=1)



    # Main Buttons Homepage Commands
    def create_event(self):
        self.create_plan.create_plan_gui(self)

    def end_event(self):
        # Open the admin end event GUI
        self.admin_end_event.create_gui_end_event(self)

    def view_summaries(self):
        # Open the admin end event GUI
        self.admin_view_summaries.create_gui_view_summaries(self)

    def edit_accounts(self):
        # Open the admin edit volunteer details GUI
        self.admin_edit_details.create_gui(self)

    def allocate_resources(self):
        # Open the resource allocation GUI
        self.admin_resource_allocation.create_gui_resource_allocation(self)

    def back_button_to_admin_main(self):
        # Clear current contents
        for widget in self.window.winfo_children():
            widget.grid_forget()
        # Repopulate main page
        self.create_gui_admin_main()

    # Menu Commands
    def create_volunteer_account(self):
        self.admin_edit_details.create_account_gui()

    def view_charts(self):
        self.pie_charts_instance.generate_charts_window()

    def view_map(self):
        self.map_instance.view_country_map_window()

    def edit_view_delete_refugee(self):
        self.admin_display_refugees.create_gui_refugee_display(self)

    def edit_view_delete_volunteers(self):
        self.admin_display_volunteers.create_gui_volunteer_display(self)

    def help_about(self):
        self.admin_help.about_pop_up()

    def help_info(self):
        self.admin_help.info_pop_up()

    def help_support(self):
        self.admin_help.support_pop_up()

    # Edit Camp Info (edit_camp_details.py)
    def t_edit_camp(self):
        edit_camp_details(self.window, self.back_button_to_admin_main)

    def t_create_refugee(self):
        self.refugee_entry_widgets = new_refugee(self.window, self.y_camp_info, self.na_refugee_info, self.back_button_to_admin_main, self.refugee_details_storage_handler)
    def refugee_details_storage_handler(self, camp_ID, name_entry, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry):
        na_refugee_info_dict(self.na_refugee_info, camp_ID, name_entry, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry)


    def do_nothing(self):
        pass

    def exit_and_go_back(self):
        self.window.destroy()
        self.go_to_landing_page()

    def exit_software(self):
        self.root.quit()

    def destroy(self):
        self.window.destroy()

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

        tk.Radiobutton(theme_window, text="Light Theme", variable=self.current_theme,
                       value='light', command=lambda: self.apply_theme('light')).pack(anchor=tk.W)
        tk.Radiobutton(theme_window, text="Dark Theme", variable=self.current_theme,
                       value='dark', command=lambda: self.apply_theme('dark')).pack(anchor=tk.W)
        tk.Radiobutton(theme_window, text="No Theme", variable=self.current_theme,
                       value='no_theme', command=lambda: self.apply_theme('no_theme')).pack(anchor=tk.W)

    def apply_theme(self, theme):
        if theme == 'dark':
            self.window.configure(bg='red3')
        elif theme == 'light':
            self.window.configure(bg='pink')
        else:
            self.window.configure(bg='SystemButtonFace')
