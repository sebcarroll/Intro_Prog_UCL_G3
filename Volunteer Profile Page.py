import tkinter
from tkinter import *
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



class tvolunteer_main_page(t_deactivated_account, t_deleted_account, t_case_sensitive, t_no_text, t_incorrect_details):

    def __init__(self) -> None:
        self.t_volunteer_dict = {'volunteer1': 'password1', 'volunteer2':'password2'}
        self.window = tkinter.Tk()
        self.window.title('Whatever')
        self.t_volunteer_login()
        self.t_details_confirmation()
        
        
        
        
    def t_volunteer_login(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.t_volunteer_frame = tkinter.Frame(self.window)
        self.t_volunteer_frame.pack()

        self.t_info_frame = tkinter.LabelFrame(self.t_volunteer_frame, text='Volunteer login', font= 25)
        self.t_info_frame.grid(row=0, column=0, padx=20, pady=10)

        self.t_volunteer_title = tkinter.Label(self.t_volunteer_frame, text='Volunteer login', font=('Arial bold', 50))
        self.t_volunteer_title.grid(row=0, column=0, pady= 30)
        self.t_name_label = tkinter.Label(self.t_volunteer_frame, text= 'Username')
        self.t_name_label.grid(row=1, column=0)
        self.t_name_entry = tkinter.Entry(self.t_volunteer_frame)
        self.t_name_entry.grid(row=2, column=0)

        self.t_password_label2 = tkinter.Label(self.t_volunteer_frame, text= 'Password')
        self.t_password_label2.grid(row=3, column=0, pady=5)
        self.t_password_entry = tkinter.Entry(self.t_volunteer_frame, show= '*')
        self.t_password_entry.grid(row=4, column=0)

        self.t_entry_button = tkinter.Button(self.t_volunteer_frame, text= 'Login', command=self.t_details_confirmation, height= 1, width= 20)
        self.t_entry_button.grid(row=5, column=0, pady= 20)

        self.label_caps = tkinter.Label(self.t_volunteer_frame)
        self.label_caps.grid(row= 5, column=1)
        self.window.bind("<KeyPress>", self.caps_lock_on)
        self.window.bind("<KeyRelease>", self.caps_lock_off)

        self.window.mainloop()


    def t_details_confirmation(self):
        username = self.t_name_entry.get()
        password = self.t_password_entry.get()
        try:
            if username not in self.t_volunteer_dict.keys():
                raise t_deleted_account
            else:
                if password == self.t_volunteer_dict[username]:
                    print(self.t_volunteer_dict)
                elif password != self.t_volunteer_dict[username]:
                    raise t_incorrect_details

            #if (username.lower() or password.lower()) in self.volunteer_dict:
                #raise t_case_sensitive
        except(t_incorrect_details):
            tkinter.messagebox.showinfo(title='Incorrect details', message='The password does not match the username')
       # except(t_case_sensitive):
            #tkinter.messagebox.showinfo(title='Incorrect capitals', message='Check to make sure you didn\'t accidentally use caps lock')
        except(t_deleted_account):
            tkinter.messagebox.showinfo(title='Username non-existent', message='That is not a valid volunteer username')

    def caps_lock_on(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='Caps lock is on')
    def caps_lock_off(self, event):
        if event.keysym == 'Caps_Lock':
            self.label_caps.config(text='')
    


tvolunteer_main_page()