import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from volunteer_login_page import VolunteerLoginPage
import pickle
import re
import os


class invalid_email(Exception):
    pass
class invalid_phone_number(Exception):
    pass
class invalid_name(Exception):
    pass


class VolunteerHomepage(VolunteerLoginPage):
    def __init__(self, root, username, go_to_landing_page):
        #super().__init__(root)
        VolunteerLoginPage.__init__(self, root, go_to_landing_page)
        self.root = root
        self.username = username
        self.go_to_landing_page = go_to_landing_page
        self.window = tk.Toplevel(self.root)
        self.window.title('Volunteer Homepage')
        self.window.geometry('1300x600')

        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Log Out", command=self.exit_and_go_back)

        self.t_summary_title = tk.Label(self.window, text='Welcome to the volunteer portal', font=('Arial Bold', 40))
        self.t_summary_title.grid(row=0, column=3, pady=30)

        self.t_summary_editdetails = tk.Button(self.window, text='Personal information', command=self.t_personal_information_base, height=2, width=20)
        self.t_summary_editdetails.grid(row=3, column=3, pady=5)

        self.t_summary_editcamp = tk.Button(self.window, text='Edit camp information', command=self.t_edit_camp, height=2, width=20)
        self.t_summary_editcamp.grid(row=4, column=3, pady=5)

        self.t_summary_refugee = tk.Button(self.window, text='Create a refugee profile', command=self.t_create_refugee, height=2, width=20)
        self.t_summary_refugee.grid(row=5, column=3)

        self.t_summary_resources = tk.Button(self.window, text='Display resources available', command=self.t_display_resources, height=2, width=20)
        self.t_summary_resources.grid(row=6, column=3)

        try:
            if os.path.getsize('data.pickle') > 0:
                with open('data.pickle', 'rb') as file:
                    self.y_personal_info = pickle.load(file)
            else:
                self.y_personal_info = {
                    'volunteer1': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False},
                    'volunteer2': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False},
                    'volunteer3': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                                   'Work Type': '', 'Deactivated': True, 'Deleted': False},
                    'volunteer4': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False},
                    '': {'password': '', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                                   'Work Type': '', 'Deactivated': False, 'Deleted': False}
                }
        except(FileNotFoundError):
            self.y_personal_info = {
                'volunteer1': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': False, 'Deleted': False},
                'volunteer2': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': False, 'Deleted': False},
                'volunteer3': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': True, 'Deleted': False},
                'volunteer4': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                               'Work Type': '', 'Deactivated': False, 'Deleted': False}
            }

        self.y_camp_info = {"Syria": {"ID": "123098", "Max Capacity": ""}}


    # UI for personal info - very similar to the t_volunteer_login function:
    def t_personal_information_base(self):
        for i in self.window.winfo_children():
            i.grid_forget()
        self.t_personal_frame = tk.Frame(self.window)
        self.t_personal_frame.grid()

        self.t_personal_labelframe = tk.LabelFrame(self.t_personal_frame)
        self.t_personal_labelframe.grid(row=3, column=3, padx=10, pady=10)

        self.t_personal_title = tk.Label(self.t_personal_frame, text='Volunteer Details', font=('Arial Bold', 30))
        self.t_personal_title.grid(row=0,column=3,pady=30)

        # Name label
        self.t_personal_namelabel = tk.Label(self.t_personal_labelframe, text='Name', font=('TkDefaultFont', 15))
        self.t_personal_namelabel.grid(row=4,column=2,pady=5)
        self.t_personal_name = tk.Label(self.t_personal_labelframe, text=self.y_personal_info[self.username]['name'], font=('TkDefaultFont', 15))
        self.t_personal_name.grid(row=4, column=3, pady=5)

        # Email label
        self.t_personal_emailabel = tk.Label(self.t_personal_labelframe, text='Email Address: ', font=('TkDefaultFont', 15))
        self.t_personal_emailabel.grid(row=6, column=2, pady=5)
        self.t_personal_email = tk.Label(self.t_personal_labelframe,text=self.y_personal_info[self.username]['Email Address'],font=('TkDefaultFont', 15))
        self.t_personal_email.grid(row=6, column=3, pady=5)

        # Phone label
        self.t_personal_phonenumberlabel = tk.Label(self.t_personal_labelframe, text='Phone number: ', font=('TkDefaultFont', 15))
        self.t_personal_phonenumberlabel.grid(row=8, column=2, pady=5)
        self.t_phonenumber = tk.Label(self.t_personal_labelframe, text=self.y_personal_info[self.username]['Phone Number'],font=('TkDefaultFont', 15))
        self.t_phonenumber.grid(row=8, column=3, pady=5)


        self.t_personal_commitmentlabel = tk.Label(self.t_personal_labelframe, text='Commitment: ', font=('TkDefaultFont', 15))
        self.t_personal_commitmentlabel.grid(row=10, column=2, pady=5)
        self.t_commitment = tk.Label(self.t_personal_labelframe, text=self.y_personal_info[self.username]['Commitment'], font=('TkDefaultFont', 15))
        self.t_commitment.grid(row=10, column=3, pady=5)

        self.t_personal_namelabel = tk.Label(self.t_personal_labelframe, text='Work type: ', font=('TkDefaultFont', 15))
        self.t_personal_namelabel.grid(row=12, column=2, pady=5)

        self.t_work_type_label = tk.Label(self.t_personal_labelframe, text=self.y_personal_info[self.username]['Work Type'], font=('TkDefaultFont', 15))
        self.t_work_type_label.grid(row=12, column=3, pady=5)

        # Store details button, need to put it in the
        self.t_edit_details = tk.Button(self.t_personal_frame, text='Edit details', command=self.t_personal_info_edit, height=1, width=20)
        self.t_edit_details.grid(row=14, column=3)

        self.t_back_to_summary = tk.Button(self.t_personal_frame, text='Back to Home', command=self.back_button_to_volunteer_main)
        self.t_back_to_summary.grid(row=14, column=1)

        # If you want to change an of your personal information which should then update the personal info dict.





    def t_personal_info_edit(self):
        for i in self.window.winfo_children():
            i.grid_forget()
        self.t_personal_frame = tk.Frame(self.window)
        self.t_personal_frame.grid()

        self.t_personal_labelframe = tk.LabelFrame(self.t_personal_frame)
        self.t_personal_labelframe.grid(row=3, column=3)


        self.personal_title = tk.Label(self.t_personal_frame, text='Edit details', font=('Arial Bold', 30))
        self.personal_title.grid(row=0, column=3, pady=30)

        #  Currently set name and current title
        self.current_title = tk.Label(self.t_personal_labelframe, text='Current details', font=('tkDefault', 20))
        self.current_title.grid(row=4, column=2)

        self.preset_name = tk.Label(self.t_personal_labelframe, text=self.y_personal_info[self.username]['name'], font=('tkDefault', 15))
        self.preset_name.grid(row=5, column=2, padx=5)

        # Edit column title
        self.edit_title = tk.Label(self.t_personal_labelframe, text='Edit', font=('tkDefault', 20))
        self.edit_title.grid(row=4, column=3, padx=5)

        # Name entry box
        self.t_personal_nameEntry = tk.Entry(self.t_personal_labelframe, text='name')
        self.t_personal_nameEntry.grid(row=5, column=3)

        # Email header/label
        # t_personal_email = tk.Label(t_personal_labelframe, text=' Edit Email address')
        # Current email
        self.personal_email = tk.Label(self.t_personal_labelframe,
                                       text=self.y_personal_info[self.username]['Email Address'],
                                       font=('tkDefault', 15))
        self.personal_email.grid(row=7, column=2, padx=5)

        # Email entry box
        self.t_personal_emailEntry = tk.Entry(self.t_personal_labelframe)
        self.t_personal_emailEntry.grid(row=7, column=3)
        # t_phonenumber = tk.Label(t_personal_labelframe, text='Edit Phone number')

        # Phone number Entry and label
        self.phone_number = tk.Label(self.t_personal_labelframe,
                                     text=self.y_personal_info[self.username]['Phone Number'],
                                     font=('tkDefault', 15))
        self.phone_number.grid(row=9, column=2, padx=5)
        self.t_phonenumberEntry = tk.Entry(self.t_personal_labelframe)
        self.t_phonenumberEntry.grid(row=9, column=3)

        # Commitment label
        self.commitment_label = tk.Label(self.t_personal_labelframe,
                                         text=self.y_personal_info[self.username]['Commitment'],
                                         font=('tkDefault', 15))
        self.commitment_label.grid(row=11, column=2, padx=5)

        # Commitment type entry
        self.t_commitmentEntry = ttk.Combobox(self.t_personal_labelframe,
                                              values=['Full time', 'Part time', 'Occasional'],
                                              state='readonly')
        self.t_commitmentEntry.grid(row=11, column=3)

        # Work type label
        self.work_type_label = tk.Label(self.t_personal_labelframe,
                                        text=self.y_personal_info[self.username]['Work Type'],
                                        font=('tkDefault', 15))
        self.work_type_label.grid(row=13, column=2, padx=5)

        # Work type entry
        self.t_worktypeEntry = ttk.Combobox(self.t_personal_labelframe, values=['Medical Aid', 'Food counselling'])
        self.t_worktypeEntry.grid(row=13, column=3)

        # Store details box
        self.t_store_details = tk.Button(self.t_personal_frame, text='Store details', command=self.t_personal_info_dict,
                                         height=1, width=20)
        self.t_store_details.grid(row=17, column=3)

        # Back to details page
        self.t_back_to_details = tk.Button(self.t_personal_frame, text='Back to view details',
                                           command=self.t_personal_information_base)
        self.t_back_to_details.grid(row=17, column=1)

        # Back to summary page
        self.back_to_summary = tk.Button(self.t_personal_frame, text='Back to Home',
                                         command=self.back_button_to_volunteer_main)
        self.back_to_summary.grid(row=17, column=5)




    def t_personal_info_dict(self):
        try:
            # Update self.y_personal_info dictionary
            with open('data.pickle', 'wb') as file:
                name = self.t_personal_nameEntry.get()
                email = self.t_personal_emailEntry.get()
                phone = self.t_phonenumberEntry.get()
                commitment = self.t_commitmentEntry.get()
                work = self.t_worktypeEntry.get()

                try:
                    # If entered non-alpha characters, raise error
                    if re.search(r'^[A-Za-z]', name):
                        self.y_personal_info[self.username]['name'] = name.strip()
                    else:
                        raise invalid_name

                    # If entered non-number characters, raise error
                    if re.search(r'^[0-9]+', phone):
                        self.y_personal_info[self.username]['Phone Number'] = phone
                    else:
                        raise invalid_phone_number
                    # Make sure they include correct email format
                    if re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
                        self.y_personal_info[self.username]['Email Address'] = email
                    else:
                        raise invalid_email

                    self.y_personal_info[self.username]['Work Type'] = work
                    self.y_personal_info[self.username]['Commitment'] = commitment

                except(invalid_email):
                    tk.messagebox.showinfo(title='Invalid Email', message='Please enter a valid email address')
                except(invalid_phone_number):
                    tk.messagebox.showinfo(title='Invalid Phone Number',
                                                message='Please enter a valid phone number')
                except(invalid_name):
                    tk.messagebox.showinfo(title='Invalid Name', message='Please enter a valid name')

                pickle.dump(self.y_personal_info, file)
            # Go back to the details page
            self.t_personal_information_base()
        except FileNotFoundError:
            pass

    # Edit camp information page
    def t_edit_camp(self):
        for i in self.window.winfo_children():
            i.grid_forget()
        self.t_edit_campframe = tk.Frame(self.window)
        self.t_edit_campframe.grid()

        self.t_edit_camp_title = tk.Label(self.t_edit_campframe, text='Edit camp', font=('Arial Bold', 30), pady=30)
        self.t_edit_camp_title.grid(row=0, column=1)

        # Sub-label
        self.t_camp_labelframe = tk.LabelFrame(self.t_edit_campframe)
        self.t_camp_labelframe.grid(row=1, column=1)

        # Camp ID box and label
        self.t_camp_ID_label = tk.Label(self.t_camp_labelframe, text='Camp ID')
        self.t_camp_ID_label.grid(row=3, column=3)
        self.t_camp_ID_box = ttk.Combobox(self.t_camp_labelframe, values=self.y_camp_info['Syria']['ID'])
        self.t_camp_ID_box.grid(row=3, column=4, padx=5)
        # Capacity for new refugees box and label
        self.t_camp_capacity = tk.Label(self.t_camp_labelframe, text='Capacity for new refugees:')
                #NOTE need to add current number here next to it so Ying add that in with dictionary or however.
        self.t_camp_capacity.grid(row=4, column=3, padx=5)
        self.t_camp_campacitybox = ttk.Spinbox(self.t_camp_labelframe, from_=0, to=1000, style='info.TSpinbox')
        self.t_camp_campacitybox.grid(row=4, column=4, padx=5)


        # BUTTONS:
        # Save changes button, need to add this to a dictionary.
        self.t_save_changes = tk.Button(self.t_edit_campframe, text='Save changes', command='Store in dictionary')
        self.t_save_changes.grid(row=7, column=1, padx=5, pady=10)
        # Back button
        self.t_back_button = tk.Button(self.t_edit_campframe, text='Back to Home', command=self.back_button_to_volunteer_main)
        self.t_back_button.grid(row=7, column=0, padx=5, pady=10)



    def t_create_refugee(self):
        for i in self.window.winfo_children():
            i.grid_forget()
        # Main frame for this whole page
        self.refugeeframe = tk.Frame(self.window)
        self.refugeeframe.grid()

        # Title for the page
        self.refugee_title = tk.Label(self.refugeeframe, text='Create Refugee Profile', font=('tkDefault', 30))
        self.refugee_title.grid(row=0, column=1, pady=30)

        # Label frame for this page that then stores all of the labels and entries
        self.refugee_labelframe = tk.LabelFrame(self.refugeeframe)
        self.refugee_labelframe.grid(row=1, column=1)

        # Camp ID
        self.t_camp_ID_label = tk.Label(self.refugee_labelframe, text='Camp ID', font=('tkDefault', 15))
        self.t_camp_ID_label.grid(row=3, column=3)
        self.t_camp_IDbox = ttk.Combobox(self.refugee_labelframe, values=self.y_camp_info['Syria']['ID'])
        self.t_camp_IDbox.grid(row=3, column=4, padx=5)

        # Medical conditions, we need to add dictionaries and everything for this
        self.medical_conditionslabel = tk.Label(self.refugee_labelframe, text='Enter any medical condition(s)',
                                                font=('tkDefault', 15))
        self.medical_conditionslabel.grid(row=5, column=3, padx=5)
        self.medical_conditonsbox = ttk.Combobox(self.refugee_labelframe,
                                            values='We havennt come up with this dictionary yet')
        self.medical_conditonsbox.grid(row=5, column=4)
        # I'm going to add another box for other that pops up if their medical conditions isn't in the list
        # Just haven't decided how I want to hide it and then have it appear just yet.

        # Family members
        self.family_label = tk.Label(self.refugee_labelframe, text='Family members', font=('tkDefault', 15))
        self.family_label.grid(row=7, column=3, padx=5)
        self.family_box = ttk.Combobox(self.refugee_labelframe, values='We havent done this yet')
        self.family_box.grid(row=7, column=4)
        # Also thinking of adding a similar thing to this where if they already have members in the camp its fine but if not
        # A separate box comes down that allows them to type the name into it, shouldn't be complicated I just cbf rn

        # Back button
        self.t_back_button = tk.Button(self.refugeeframe, text='Back to Home', command=self.back_button_to_volunteer_main)
        self.t_back_button.grid(row=9, column=0, padx=5, pady=10)







    def t_display_resources(self):
        for i in self.window.winfo_children():
            i.grid_forget()
        self.resources_frame = tk.Frame(self.window)
        self.resources_frame.grid()

        # Title
        self.resources_title = tk.Label(self.resources_frame, text='Resources Currently Available', font=('tkDefault', 30))
        self.resources_title.grid(row=0, column=1)

        # Creating label frame
        self.resources_labelframe = tk.LabelFrame(self.resources_frame)
        self.resources_labelframe.grid(row=1, column=1)

        # Not sure what is meant to go in here at the moment so will just leave it for now.
        self.t_back_button = tk.Button(self.resources_frame, text='Back to Home', command=self.back_button_to_volunteer_main)
        self.t_back_button.grid(row=9, column=0, padx=5, pady=10)






    def back_button_to_volunteer_main(self):
        # Clear current contents
        for widget in self.window.winfo_children():
            widget.grid_forget()
        # Repopulate main page
        self.t_summary_title.grid(row=0, column=3, pady=30)
        self.t_summary_editdetails.grid(row=3, column=3, pady=5)
        self.t_summary_editcamp.grid(row=4, column=3, pady=5)
        self.t_summary_refugee.grid(row=5, column=3)
        self.t_summary_resources.grid(row=6, column=3)

    def exit_and_go_back(self):
        self.window.destroy()
        self.go_to_landing_page()

    def destroy(self):
        self.window.destroy()

