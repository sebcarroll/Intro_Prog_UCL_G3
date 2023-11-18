import tkinter as tk
import pickle
import os
from AdminSubpages.create_plan import new_plan, na_refugee_info_dict

class AdminHomepage:
    def __init__(self, root, go_to_landing_page):
        self.root = root
        self.go_to_landing_page = go_to_landing_page
        self.new_plan_entry_widgets = None

        self.window = tk.Toplevel(self.root)
        self.window.title('Admin Homepage')
        self.window.geometry('1300x600')

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


        # Initialize na_refugee_info before trying to load from the pickled file
        self.na_refugee_info = {
            'refugee1': {'Camp ID': '', 'Family Members': '', 'Medical Conditions': '', 'Languages Spoken': '', 'Second Language': ''}
        }
        self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}

        # MENU BAR:
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        # create a menu item 1
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Plan", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Log Out", command=self.exit_and_go_back)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_software)
        # create a menu item 2
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=file_menu)
        file_menu.add_command(label="Edit Event", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Resources", command=self.our_cmd)
        # create a menu item 3
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=file_menu)
        file_menu.add_command(label="View Events", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="View Summaries", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Allocate Resources", command=self.our_cmd)
        # create a menu item 4
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Accounts", menu=file_menu)
        file_menu.add_command(label="Create", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Volunteers", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Admins", command=self.our_cmd)
        # create a menu item 5
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_command(label="Display", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Audio", command=self.our_cmd)
        # create a menu item 6
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=file_menu)
        file_menu.add_command(label="Contact Support", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="About", command=self.our_cmd)

        self.admin_welcome_title = tk.Label(self.window, text='Welcome to the Admin portal', font=('Arial Bold', 40))
        self.admin_welcome_title.grid(row=0, column=3, pady=30)

        # MAIN BUTTONS
        # Create new event button
        self.btn_create_event = tk.Button(self.window, text="Create new event", command=self.create_event)
        self.btn_create_event.grid(row=3, column=3, pady=5)

        # End an event button
        self.btn_end_event = tk.Button(self.window, text="End an event", command=self.end_event)
        self.btn_end_event.grid(row=5, column=3, pady=5)

        # View summaries button
        self.btn_view_summaries = tk.Button(self.window, text="View Summaries", command=self.view_summaries)
        self.btn_view_summaries.grid(row=7, column=3, pady=5)

        # Edit volunteer accounts button
        self.btn_edit_accounts = tk.Button(self.window, text="Edit volunteer accounts", command=self.edit_accounts)
        self.btn_edit_accounts.grid(row=9, column=3, pady=5)

        # Allocate resources button
        self.btn_allocate_resources = tk.Button(self.window, text="Allocate resources", command=self.allocate_resources)
        self.btn_allocate_resources.grid(row=11, column=3, pady=5)




    #def create_event(self):
        # Open the resource allocation GUI
        #new_plan(self.window, self.back_button_to_admin_main)
        #new_window = tk.Toplevel()
        #apcg.create_plan_gui(new_window)

    def create_event(self):
        self.new_plan_entry_widgets = new_plan(self.window, self.na_refugee_info, self.back_button_to_admin_main, self.new_plan_details_storage_handler)
    def new_plan_details_storage_handler(self, camp_ID, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry):
        na_refugee_info_dict(self.na_refugee_info, camp_ID, family_label, medical_conditionsEntry, languages_spokenEntry, second_languageEntry)






    def end_event(self):
        # Add functionality for ending an event
        print("Ending an event...")
        # Implement the function's logic here

    def view_summaries(self):
        # Add functionality for viewing summaries
        print("Viewing summaries...")
        # Implement the function's logic here

    def edit_accounts(self):
        # Add functionality for editing volunteer accounts
        print("Editing volunteer accounts...")
        # Implement the function's logic here

    def allocate_resources(self):
        # Open the resource allocation GUI
        print("Allocating resources...")








    def back_button_to_admin_main(self):
        # Clear current contents
        for widget in self.window.winfo_children():
            widget.grid_forget()
        # Repopulate main page
        self.admin_welcome_title.grid(row=0, column=3, pady=30)
        self.btn_create_event.grid(row=3, column=3, pady=5)
        # End an event button
        self.btn_end_event.grid(row=5, column=3, pady=5)
        # View summaries button
        self.btn_view_summaries.grid(row=7, column=3, pady=5)
        # Edit volunteer accounts button
        self.btn_edit_accounts.grid(row=9, column=3, pady=5)
        # Allocate resources button
        self.btn_allocate_resources.grid(row=11, column=3, pady=5)

    def our_cmd(self):
        pass

    def exit_and_go_back(self):
        self.window.destroy()
        self.go_to_landing_page()

    def exit_software(self):
        self.root.quit()

    def destroy(self):
        self.window.destroy()



