import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



class k_admin_mainpage():
    def __init__(self) -> None:
        self.k_login_details = {'Admin' : {'password': '111'}
    }
        self.window = tkinter.Tk()
        self.window.title('Whatever')
        self.k_admin_login()
        self.k_login_confirmation()

    def k_admin_login(self):
        for i in self.window.winfo_children():
            i.destroy()
        # admin frame put on screen
        self.k_admin_frame = tkinter.Frame(self.window)
        self.k_admin_frame.pack()

    #Volunteer frame white border
        self.k_info_frame = tkinter.LabelFrame(self.k_admin_frame, text= 'Admin login', font=25)
        self.k_info_frame.grid(row=0, column=0, padx=20, pady=10)

    #admin title
        self.k_admin_title = tkinter.Label(self.k_admin_frame, text='Admin login', font=('Arial bold', 50))
        self.k_admin_title.grid(row=0, column=0, pady=30)

    # Username entry box
        self.k_name_label = tkinter.Label(self.k_admin_frame, text='Username')
        self.k_name_label.grid(row=1, column=0)
        self.k_name_entry = tkinter.Entry(self.k_admin_frame)
        self.k_name_entry.grid(row=2, column=0)

    # Password entry box
        self.k_password_label2 = tkinter.Label(self.k_admin_frame, text='Password')
        self.k_password_label2.grid(row=3, column=0, pady=5)
        self.k_password_entry = tkinter.Entry(self.k_admin_frame, show='*')
        self.k_password_entry.grid(row=4, column=0)

    # Login box
        self.k_entry_button = tkinter.Button(self.k_admin_frame, text='Login', command=self.k_login_confirmation,height=1, width=20)
        self.k_entry_button.grid(row=5, column=0, pady=20)

    # Shows caps lock on/off
        self.label_caps = tkinter.Label(self.k_admin_frame)
        self.label_caps.grid(row=4, column=1)
        self.window.bind("<KeyPress>", self.caps_lock_on)
        self.window.bind("<KeyRelease>", self.caps_lock_off)

    # Launches tkinter
        self.window.mainloop()
   
    #Login check 
    def k_login_confirmation(self):
        self.username = self.k_name_entry.get()
        password = self.k_password_entry.get()
        if self.username not in self.k_login_details.keys():
            raise k_incorrect_details
        else:
            if password == self.k_login_details[self.username]['password']:
                print()
                self.t_volunteer_summary()
            elif password != self.k_login_details[self.username]['password']:
                raise k_incorrect_details

        if k_incorrect_details:
            tkinter.messagebox.showinfo(title='Incorrect details', message='incorrect username or password please try again')
    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on')
    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='')


    def k_admin_summary(self):
        for i in self.winfo_children():
            i.destroy()
        self.k_summary_frame = tkinter.frame(self.window)
        self.k_summary_frame.pack()
        self.k_summary_title = tkinter.Label(self.k_summary_frame, text='Welcome to the volunteer portal', font=('Arial Bold', 40))
        self.k_summary_title.grid(row=0, column=3, pady=30)

        
k_admin_mainpage()


