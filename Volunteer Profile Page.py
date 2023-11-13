import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
        self.y_personal_info = {
            'volunteer1': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '', 'Work Type': '', 'Deactivated': False, 'Deleted': False},
            'volunteer2': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '', 'Work Type': '', 'Deactivated': False, 'Deleted': False},
            'volunteer3': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '', 'Work Type': '', 'Deactivated': False, 'Deleted': False},
            'volunteer4': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '', 'Work Type': '', 'Deactivated': False, 'Deleted': False}
        }

        self.y_camp_info = {"Syria" : {"ID": "123098", "Max Capacity": ""}}
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
        self.label_caps.grid(row= 4, column=1)
        self.window.bind("<KeyPress>", self.caps_lock_on)
        self.window.bind("<KeyRelease>", self.caps_lock_off)

        self.window.mainloop()

    
        
        
      


    def t_details_confirmation(self):
        self.username = self.t_name_entry.get()
        password = self.t_password_entry.get()
        try:
            if self.username not in self.y_personal_info.keys():
                raise t_deleted_account
            else:
                if password == self.y_personal_info[self.username]['password']:
                    print(self.y_personal_info)
                    self.t_volunteer_summary()
                elif password != self.y_personal_info[self.username]['password']:
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

    def t_volunteer_summary(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.t_summary_frame = tkinter.Frame(self.window)
        self.t_summary_frame.pack()
        self.t_summary_title = tkinter.Label(self.t_summary_frame, text='Welcome to the volunteer portal', font=('Arial Bold', 40))
        self.t_summary_title.grid(row=0, column=3, pady=30)
        self.t_summary_editdetails = tkinter.Button(self.t_summary_frame, text= 'Edit personal information', command=self.t_personal_information_base, height=2, width=20)
        self.t_summary_editdetails.grid(row=3, column=3, pady=5)
        self.t_summary_editcamp = tkinter.Button(self.t_summary_frame, text='Edit camp information', command= self.t_edit_camp, height=2, width= 20)
        self.t_summary_editcamp.grid(row=4, column=3, pady=5)
        self.t_summary_refugee = tkinter.Button(self.t_summary_frame, text= 'Create a refugee profile', command= self.t_create_refugee, height=2, width=20)
        self.t_summary_refugee.grid(row=5, column=3)
        self.t_summary_resources = tkinter.Button(self.t_summary_frame, text= 'Display resources available', command= self.t_display_resources, height=2, width=20)
        self.t_summary_resources.grid(row=6, column=3)
        
        

        # This is the UI for personal information, don't touch it Ying.
    def t_personal_information_base(self):
        for i in self.window.winfo_children():
            i.destroy()
        t_personal_frame = tkinter.Frame(self.window)
        t_personal_frame.pack()
        t_personal_labelframe = tkinter.LabelFrame(t_personal_frame)
        t_personal_labelframe.grid(row=3, column=3)
        t_personal_title = tkinter.Label(t_personal_frame, text= 'Edit details', font=('Arial Bold', 30)).grid(row=0, column=3, pady=30)
        t_personal_name = tkinter.Label(t_personal_labelframe, text='Full name')
        t_personal_name.grid(row=4, column=3)

        # Name entry
        self.t_personal_nameEntry = tkinter.Entry(t_personal_labelframe, text='name').grid(row=5, column=3)
        # Email label
        t_personal_email = tkinter.Label(t_personal_labelframe, text='Email address')
        t_personal_email.grid(row=6, column=3)

        #mail entry
        self.t_personal_emailEntry = tkinter.Entry(t_personal_labelframe).grid(row=7, column=3)
        t_phonenumber = tkinter.Label(t_personal_labelframe, text='Phone number')

        # Phone number Entry
        self.t_phonenumberEntry = tkinter.Entry(t_personal_labelframe)
        t_phonenumber.grid(row=8, column=3)
        self.t_phonenumberEntry.grid(row=9, column=3)
        t_commitment = tkinter.Label(t_personal_labelframe, text='Commitment')

        # Commitment type entry
        self.t_commitmentEntry =ttk.Combobox(t_personal_labelframe, values=['Full time', 'Part time', 'Occasional'], state='readonly')
        t_commitment.grid(row=10, column=3)
        self.t_commitmentEntry.grid(row=11, column=3)

        t_work_type_label = tkinter.Label(t_personal_labelframe, text='Work type')
        t_work_type_label.grid(row=12, column= 3)

        # Work type entry
        self.t_worktypeEntry = ttk.Combobox(t_personal_labelframe, values=['Medical Aid', 'Food counselling'])
        self.t_worktypeEntry.grid(row=13, column=3)
        
        t_store_details = tkinter.Button(t_personal_frame, text='Store details', command= self.t_personal_info_dict, height=1, width=20)
        t_store_details.grid(row=14, column=3) 
        t_back_to_summary = tkinter.Button(t_personal_frame, text='Back', command= self.t_volunteer_summary)
        t_back_to_summary.grid(row=5, column= 1)

        # If you want to change an of your personal information which should then update the personal info dict.
    def t_personal_info_edit(self):
        pass

    def t_personal_info_dict(self):
        self.y_personal_info[self.username]['name'] = self.t_personal_nameEntry.get()
        self.y_personal_info[self.username]['Email Address'] = self.t_personal_emailEntry.get()
        self.y_personal_info[self.username]['Phone Number'] = self.t_personal_phonenumberEntry.get()
        self.y_personal_info[self.username]['Commitment'] = self.t_personal_commitmentEntry.get()
        self.y_personal_info[self.username]["Work Type"] = self.t_personal_worktypeEntry.get()
        # Edit camp information page
    def t_edit_camp(self):
        for i in self.window.winfo_children():
            i.destroy()
        t_edit_campframe = tkinter.Frame(self.window)
        t_edit_campframe.pack()
        t_edit_camp_title = tkinter.Label(t_edit_campframe, text='Edit camp', font=('Arial Bold', 30), pady=30)
        t_edit_camp_title.grid(row=0, column=3)
        t_camp_labelframe = tkinter.LabelFrame(t_edit_campframe)
        t_camp_labelframe.grid(row=1, column=1)

        # Camp ID box and label
        t_camp_ID_label = tkinter.Label(t_camp_labelframe, text= 'Camp ID')
        t_camp_ID_label.grid(row=3, column=3)
        self.t_camp_ID_box = ttk.Combobox(t_camp_labelframe, values= self.y_camp_info['Syria']['ID'])
        self.t_camp_ID_box.grid(row=4, column=3)

        # Capacity for new refugees box and label
        t_camp_capacity = tkinter.Label
        

        # Back button
        t_back_button = tkinter.Button(t_edit_campframe, text='Back', command= self.t_volunteer_summary)
        t_back_button.grid(row=5, column=1)



    def t_create_refugee(self):
        for i in self.window.winfo_children():
            i.destroy()
        t_create_refugeeframe = tkinter.Frame(self.window)
        t_create_refugeeframe.pack()



tvolunteer_main_page()
