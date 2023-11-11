import tkinter
from tkinter import *


class login:



    def populate_dict(self):
        user_array = []
        for i in range(len(self.users_list)):
            user_array.append(self.users_list[i][0])
        self.dict['User'] = user_array

    def detail_confirmation(self):
        terms = self.terms_status_var.get()
        name = self.name_entry_box.get()
        email = self.email_entry_box.get()
        age = int(self.age_entry_box.get())

        if terms == 'Accepted':
            if name in self.dict['User']:
                tkinter.messagebox.showwarning(title='Username error', message='That username has already been used')
            else:
                self.dict['User'] = name


            if ('@' or '.') not in email:
                tkinter.messagebox.showwarning(title='Email error', message='Invalid email address')
            else:
                self.dict['email'] = email


            if age < 16:
                tkinter.messagebox.showinfo(title='Too young', message='You have to be above 16 to use this website')
            else:
                self.dict['age'] = age
            print(self.dict)
        else:
            tkinter.messagebox.showinfo(title='Terms and conditions', message='You need to accept the terms and '
                                                                               'conditions in order to register')



    def __init__(self):
        self.dict = {'User': ' ', 'email': ' ', 'age': ' ', 'Password':' '}
        self.users_list = [("jane", "jane@example.com", 21), ("bob", "bob@example",
     19), ("jane", "jane2@example.com", 25), ("steve", "steve@somewhere",  15),  ("joe", "joe", 23), ("anna",
      "anna@example.com", -3), ]
        self.populate_dict()
        self.window = tkinter.Tk()
        self.window.title('User login')
        self.register()
        self.detail_confirmation()

    def register(self):
        """ Setting up the actual window"""

        for i in self.window.winfo_children():
            i.destroy()
        self.frame = tkinter.Frame(self.window)
        self.frame.pack()
        """Setting up the frame and boxes to enter into"""
        self.info_frame = tkinter.LabelFrame(self.frame, text='User information')
        self.info_frame.grid(row=0, column=0, padx=20, pady=10)

        """Gathering their name"""
        self.name_entry_label = tkinter.Label(self.info_frame, text='Full name')
        self.name_entry_label.grid(row=0,column=0)
        self.name_entry_box = tkinter.Entry(self.info_frame)
        self.name_entry_box.grid(row=1, column=0)

        """Gathering their email"""
        self.email_entry_label = tkinter.Label(self.info_frame, text='Email address')
        self.email_entry_label.grid(row=0, column=1)
        self.email_entry_box = tkinter.Entry(self.info_frame)
        self.email_entry_box.grid(row=1,column=1)

        """Gathering their age"""
        self.age_entry_label = tkinter.Label(self.info_frame, text='Age')
        self.age_entry_label.grid(row=0, column=2)
        self.age_entry_box = tkinter.Spinbox(self.info_frame, from_=0, to=200)
        self.age_entry_box.grid(row=1, column=2)

        for widget in self.info_frame.winfo_children():
            widget.grid_configure(padx=20, pady=5)

        """Terms and conditions frame and button"""
        self.terms_conditions_frame = tkinter.LabelFrame(self.frame)
        self.terms_conditions_frame.grid(row=1,column=0, sticky='news', padx=20,pady=10)

        self.terms_conditions_label = tkinter.Label(self.terms_conditions_frame, text='Terms and conditions')
        self.terms_conditions_label.grid(row=1,column=0)
        self.terms_status_var = tkinter.StringVar()
        self.terms_conditions_button = tkinter.Checkbutton(self.terms_conditions_frame, text='I accept the terms and conditions',
                                                           variable= self.terms_status_var, onvalue='Accepted', offvalue='Declined')
        self.terms_conditions_button.grid(row=2, column=0)

        """Final button to store all data"""
        self.button = tkinter.Button(self.frame, text='Enter information', command= self.detail_confirmation)
        self.button.grid(row=2, column=0, sticky='news', padx=20, pady=10)

        self.nextpage = tkinter.Button(self.frame, text='Password page', command=self.password_page)
        self.nextpage.grid(row=2, column=1, stick='news', padx=20,pady=20)


        self.window.mainloop()


    def password_page(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.frame2 = tkinter.Frame(self.window)
        self.frame2.pack()
        self.password_frame = tkinter.LabelFrame(self.frame2, text= 'Password making')
        self.password_frame.grid(row=0,column=0,sticky='news', padx=20, pady=20)
        self.password_label = tkinter.Label(self.password_frame, text='Password')
        self.password_label.grid(row=0,column=0, )
        self.password_box = tkinter.Entry(self.password_frame, text='Please choose a password')
        self.password_box.grid(row=1,column=0)

        self.password_confirmation = tkinter.Label(self.password_frame, text='Please confirm your password')
        self.password_confirmation_box = tkinter.Entry(self.password_frame, text='Password')
        self.password_confirmation.grid(row=0, column=2)
        self.password_confirmation_box.grid(row=1, column=2)

        self.password_button = tkinter.Button(self.frame2, text='Back to login page', command= self.register)
        self.password_button.grid(row=3,column=2)

        self.password_check = tkinter.Button(self.password_frame, text='Store your password', command= self.check_password)
        self.password_check.grid(row=3, column=1)

    def check_password(self):
        password = self.password_box.get()
        password2 = self.password_confirmation_box.get()
        if password == password2:
            self.dict['Password'] = password
            print(self.dict)
        else:
            tkinter.messagebox.showwarning(title='Password error', message='The passwords do not match')







login()