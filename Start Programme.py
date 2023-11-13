import tkinter
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('750x600')
#root['background'] = 'green'
'''do we need to change the name of our Tk or does root always refer to this window'''
root.title('Welcome to the UCL Humanity Rescue Portal')


welcome_label = ttk.Label(root, text = 'Welcome to the UCL Humanity Rescue Portal', font=('TkDefaultFont', 25, 'bold'), foreground='orange')
welcome_label.pack(padx = 50, pady = 50)


instruction_label = ttk.Label(root, text = 'Please select admin or volunteer sign in', font=('TkDefaultFont', 20))
instruction_label.pack(pady = 25)


def open_adminpage():
    adminSignInWindow = Toplevel(root)
    adminSignInWindow.title('Admin Sign In')
    Label(adminSignInWindow, text = 'this is the admin sign in window').pack()
admin_sign_in_button = ttk.Button (root, text = 'Sign in as Admin', command= open_adminpage)
admin_sign_in_button.pack(ipadx=100, ipady=25 )
'''how to change width/size of button'''


def open_volunteerpage():
    volunteerSignInWindow = Toplevel(root)
    volunteerSignInWindow.title('Volunteer Sign In')
    Label(volunteerSignInWindow, text = 'this is the volunteer sign in window').pack()
volunteer_sign_in_button = ttk.Button (root, text = 'Sign in as Volunteer', command= open_volunteerpage)
volunteer_sign_in_button.pack(ipadx=90, ipady=25)


root.mainloop()
