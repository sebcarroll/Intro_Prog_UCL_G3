import tkinter as tk

class AdminLoginPage(tk.Frame):
    def __init__(self, root, go_to_admin_main):
        super().__init__(root)
        self.root = root
        self.go_to_admin_main = go_to_admin_main

        welcome_label = tk.Label(
            self,
            text='Welcome to the UCL Humanity Rescue Portal',
            font=('TkDefaultFont', 25, 'bold'),
            foreground='orange'
        )
        welcome_label.pack(padx=50, pady=50)

        instruction_label = tk.Label(
            self,
            text='Please select admin or volunteer sign in',
            font=('TkDefaultFont', 20)
        )
        instruction_label.pack(pady=25)

        login_btn = tk.Button(self, text="Admin Login", command=self.on_login)
        login_btn.pack(ipadx=50, ipady=15)

    def on_login(self):
        # Add login logic here
        self.go_to_admin_main()