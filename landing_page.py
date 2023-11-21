import tkinter as tk
from admin_login_page import AdminLoginPage
from volunteer_login_page import VolunteerLoginPage

class LandingPage:
    def __init__(self, root, go_to_admin_main, go_to_volunteer_main):
        self.root = root
        self.go_to_admin_main = go_to_admin_main
        self.go_to_volunteer_main = go_to_volunteer_main
        self.window = tk.Toplevel(self.root)
        self.window.title('Welcome to the UCL Humanity Rescue Portal')
        self.window.geometry('1000x600')
        self.create_landing_page_widgets()

    def create_landing_page_widgets(self):
        welcome_label = tk.Label(
            self.window,
            text='Welcome to the UCL Humanity Rescue Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='orange'
        )
        welcome_label.pack(padx=50, pady=50)

        instruction_label = tk.Label(
            self.window,
            text='Please select admin or volunteer sign in',
            font=('TkDefaultFont', 20)
        )
        instruction_label.pack(pady=25)


        # Admin login button
        admin_login_btn = tk.Button(self.window, text="Admin Login", command=self.open_admin_login)
        admin_login_btn.pack(ipadx=100, ipady=25)
        # Volunteer login button
        volunteer_login_btn = tk.Button(self.window, text="Volunteer Login", command=self.open_volunteer_login)
        volunteer_login_btn.pack(ipadx=90, ipady=25)
        # Exit program button
        exit_btn = tk.Button(self.window, text="Exit Software", command=self.exit_software)
        exit_btn.pack(ipadx=30, ipady=10)


    def open_admin_login(self):
        for widget in self.window.winfo_children():
            if widget.winfo_class() != 'Menu':
                widget.destroy()
        self.admin_login_frame = AdminLoginPage(
            self.window,
            self.window,
            self.go_to_admin_main,
            self.open_admin_login,
            self.open_volunteer_login,
            self.exit_software
        )
        self.admin_login_frame.pack(fill='both', expand=True)

    def open_volunteer_login(self):
        # Clear current widgets and open volunteer login frame
        for widget in self.window.winfo_children():
            if widget.winfo_class() != 'Menu':
                widget.destroy()
        self.volunteer_login_frame = VolunteerLoginPage(
            self.window,
            self.go_to_volunteer_main
        )
        self.volunteer_login_frame.pack(fill='both', expand=True)

    def exit_software(self):
        self.root.quit()

    def destroy(self):
        self.window.destroy()
