import tkinter as tk
from tkinter import messagebox, PhotoImage

class AdminLoginPage(tk.Frame):
    def __init__(self, root, window, go_to_admin_main, open_admin_login, open_volunteer_login, exit_software):
        super().__init__(root)
        self.root = root
        self.window = window
        self.go_to_admin_main = go_to_admin_main
        self.open_admin_login = open_admin_login
        self.open_volunteer_login = open_volunteer_login
        self.exit_software = exit_software

        welcome_label = tk.Label(
            self,
            text='UCL Humanity Rescue Admin Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='orange red', relief=tk.RAISED, borderwidth=5
        )
        welcome_label.grid(row=1, column=0, padx=30, pady=30)

        admin_entries_frame = tk.Frame(self, relief=tk.RAISED, borderwidth=5)
        admin_entries_frame.grid()

        admin_log_in_frame = tk.LabelFrame(admin_entries_frame, borderwidth=5)
        admin_log_in_frame.grid(row=3, column=1, pady=30, padx=30)

        # Username entry box
        self.name_label = tk.Label(admin_log_in_frame, text='Username', font=('TkDefault', 17))
        self.name_label.grid(row=6, column=0, pady=10, padx=10)
        self.name_entry = tk.Entry(admin_log_in_frame)
        self.name_entry.grid(row=6, column=1, pady=10, padx=10)

        # Password entry box
        self.password_label2 = tk.Label(admin_log_in_frame, text='Password', font=('TkDefault', 17))
        self.password_label2.grid(row=8, column=0, pady=10)
        self.password_entry = tk.Entry(admin_log_in_frame, show='*')
        self.password_entry.grid(row=8, column=1, pady=10)

        try:
            self.image3 = PhotoImage(file="Images/admin_icon.png").subsample(8, 8)
            image_label = tk.Label(admin_log_in_frame, image=self.image3, relief=tk.RAISED, borderwidth=5)
            image_label.grid(row=5, column=1, pady=10, padx=(0,0))
        except:
            pass

        try:
            self.logo = PhotoImage(file="Images/logo.png").subsample(4, 4)
            image_label = tk.Label(admin_log_in_frame, image=self.logo, relief=tk.RAISED)
            image_label.grid(row=5, column=0, pady=10, padx=(0, 0))
        except:
            pass

        self.password_entry.bind("<KeyPress>", self.caps_lock_on)
        self.password_entry.bind("<KeyRelease>", self.caps_lock_off)

        # Login button
        login_btn = tk.Button(admin_log_in_frame, text="Login", command=self.details_confirmation)
        login_btn.grid(row=10, column=1, pady=10)
        # Swap button from command=self.details_confirmation to command=self.on_login to bypass

        # Back to landing page
        login_btn = tk.Button(admin_log_in_frame, text="Back", command=self.exit_and_go_back)
        login_btn.grid(row=10, column=0, pady=10)


        # Shows caps lock on/off (OLD BINDING NOT WORKING)
        self.label_caps = tk.Label(admin_log_in_frame, text='')
        self.label_caps.grid(row=4, column=1)
        # self.bind("<KeyPress>", self.caps_lock_on)
        # self.bind("<KeyRelease>", self.caps_lock_off)
        for i in range(11):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # For caps lock on/off
    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on', fg='red')
    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is off', fg ='red')

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
        self.go_to_admin_main()

    def exit_and_go_back(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        from landing_page import LandingPage
        LandingPage.create_landing_page_widgets(self)
