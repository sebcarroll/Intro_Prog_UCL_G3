import tkinter as tk
import pickle
import os
from AdminSubpages.create_plan import AdminCreatePlan
from AdminSubpages.admin_end_event import AdminEndEvent
from AdminSubpages.admin_edit_details import AdminEditVolunteerDetails
from AdminSubpages.admin_resource_allocation import AdminResourceAllocation

class AdminHomepage:
    def __init__(self, root, go_to_landing_page):
        self.root = root
        self.go_to_landing_page = go_to_landing_page
        self.window = tk.Toplevel(self.root)
        self.window.title('Admin Homepage')
        self.window.geometry('1300x600')
        self.window.configure(background="red")
        #self.window.attributes('-fullscreen', True)

        self.create_plan = AdminCreatePlan(self.window, self.back_button_to_admin_main)
        self.admin_end_event = AdminEndEvent(self.window, self.back_button_to_admin_main)
        self.admin_edit_details = AdminEditVolunteerDetails(self.window, self.back_button_to_admin_main)
        self.admin_resource_allocation = AdminResourceAllocation(self.window, self.back_button_to_admin_main)

        self.window.bind('<F11>', self.toggle_fullscreen)
        self.window.bind('<Escape>', self.end_fullscreen)
        self.window.protocol("WM_DELETE_WINDOW", self.window_exit_button)

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

        self.create_gui_admin_main()

    def create_gui_admin_main(self):
        # WELCOME TITLE
        self.admin_welcome_title = tk.Label(self.window, text='Welcome to the admin portal', font=('Arial', 40), bg='grey', fg='white')
        self.admin_welcome_title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=20)
        self.admin_welcome_title.configure(background="grey")

        # MAIN BUTTONS
        # Create new event button
        self.btn_create_event = tk.Button(self.window, text="Create new event", command=self.create_event)
        self.btn_create_event.grid(row=1, column=0, pady=(50,10), ipadx=93, ipady=25)

        # End an event button
        self.btn_end_event = tk.Button(self.window, text="End an event", command=self.end_event)
        self.btn_end_event.grid(row=2, column=0, pady=10, ipadx=105, ipady=25)

        # View summaries button
        self.btn_view_summaries = tk.Button(self.window, text="View Summaries", command=self.view_summaries)
        self.btn_view_summaries.grid(row=3, column=0, pady=10, ipadx=98, ipady=25)

        # Edit volunteer accounts button
        self.btn_edit_accounts = tk.Button(self.window, text="Edit volunteer accounts", command=self.edit_accounts)
        self.btn_edit_accounts.grid(row=4, column=0, pady=10, ipadx=80, ipady=25)

        # Allocate resources button
        self.btn_allocate_resources = tk.Button(self.window, text="Allocate resources", command=self.allocate_resources)
        self.btn_allocate_resources.grid(row=5, column=0, pady=(10,50), ipadx=93, ipady=25)


        for i in range(6):
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

    #def create_event(self):
        # Open the resource allocation GUI
        #new_plan(self.window, self.back_button_to_admin_main)
        #new_window = tk.Toplevel()
        #apcg.create_plan_gui(new_window)

    def create_event(self):
        # This needs linking to create plan final
        self.create_plan.create_plan_gui(self)

    def end_event(self):
        # Open the admin end event GUI
        self.admin_end_event.create_gui_end_event(self)

    def view_summaries(self):
        # Class not yet made
        print("Viewing summaries...")

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

    def our_cmd(self):
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
        self.root.destroy()

