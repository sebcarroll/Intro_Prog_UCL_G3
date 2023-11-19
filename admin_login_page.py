import tkinter as tk
from tkinter import messagebox

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

class AdminLoginPage(tk.Frame):
    def __init__(self, root, go_to_admin_main):
        super().__init__(root)
        self.root = root
        self.go_to_admin_main = go_to_admin_main

        welcome_label = tk.Label(
            self,
            text='Welcome to the UCL Humanity Rescue Admin Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='orange'
        )
        welcome_label.grid(row=1, column=0)

        instruction_label = tk.Label(
            self,
            text='Please sign in',
            font=('TkDefaultFont', 20)
        )
        instruction_label.grid(row=2, column=0)

        # self.t_volunteer_login
        # self.t_details_confirmation

        # Volunteer frame put on screen
        # self.t_volunteer_frame = tk.Frame(self)
        # self.t_volunteer_frame.pack()

        # Volunteer frame white boarder
        # self.t_info_frame = tk.LabelFrame(self.t_volunteer_frame, text='Volunteer login', font=25)
        # self.t_info_frame.grid(row=0, column=0, padx=20, pady=10)

        # Username entry box
        self.name_label = tk.Label(self, text='Username')
        self.name_label.grid(row=6, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=6, column=1)

        # Password entry box
        self.password_label2 = tk.Label(self, text='Password')
        self.password_label2.grid(row=8, column=0, pady=5)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.grid(row=8, column=1)
        self.password_entry.bind("<KeyPress>", self.caps_lock_on)
        self.password_entry.bind("<KeyRelease>", self.caps_lock_off)

        # Login button
        #self.entry_button = tk.Button(self, text='Login', command=self.details_confirmation, height=1, width=20)
        #self.entry_button.grid(row=5, column=0, pady=20)

        login_btn = tk.Button(self, text="Admin Login", command=self.details_confirmation)
        login_btn.grid(row=10, column=1, pady=10)
        # Swap button from  to command=self.on_login to bypass


        # Back to landing page
        login_btn = tk.Button(self, text="Back", command=self.exit_and_go_back)
        login_btn.grid(row=11, column=1, pady=5)


        # Shows caps lock on/off (OLD BINDING NOT WORKING)
        self.label_caps = tk.Label(self, text='')
        self.label_caps.grid(row=4, column=1)
        # self.bind("<KeyPress>", self.caps_lock_on)
        # self.bind("<KeyRelease>", self.caps_lock_off)

        # For caps lock on/off
    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on')

    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is off')

        # Admin login checker
    def details_confirmation(self):
        username = self.name_entry.get()
        password = self.password_entry.get()
            # Incorrect details:
        if username != "admin":
            tk.messagebox.showinfo(title='Invalid username', message='That is not a valid admin username')
        elif username == "admin" and password != "111":
            tk.messagebox.showinfo(title='Invalid password', message='That is not the admin password')
        elif username == "admin" and password == "111":
            # Correct details:
            self.go_to_admin_main()

    # use on_login to bypass login to admin_main:
    def on_login(self):
        # Add login logic here
        self.go_to_admin_main()

    def exit_and_go_back(self):
        pass
        """def exit_and_go_back(self):
            # Clear current contents
            for widget in self.window.winfo_children():
                widget.grid_forget()
            from landing_page import LandingPage
            refresh_landing = LandingPage(self)"""

        # Repopulate main page
        """self.admin_welcome_title.grid(row=0, column=3, pady=30)
        self.btn_create_event.grid(row=3, column=3, pady=5)
        # End an event button
        self.btn_end_event.grid(row=5, column=3, pady=5)
        # View summaries button
        self.btn_view_summaries.grid(row=7, column=3, pady=5)
        # Edit volunteer accounts button
        self.btn_edit_accounts.grid(row=9, column=3, pady=5)
        # Allocate resources button
        self.btn_allocate_resources.grid(row=11, column=3, pady=5)"""