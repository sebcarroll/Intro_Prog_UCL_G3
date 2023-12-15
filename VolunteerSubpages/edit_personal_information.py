import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import re
import pandas as pd


class invalid_email(Exception):
    pass
class invalid_phone_number(Exception):
    pass
class invalid_name(Exception):
    pass


def edit_personal_info(window, username, y_personal_info, t_personal_information_base, back_button_to_volunteer_main, store_details_callback):
    for i in window.winfo_children():
        i.grid_forget()
    t_personal_frame = tk.Frame(window)
    t_personal_frame.grid()

    t_personal_labelframe = tk.LabelFrame(t_personal_frame)
    t_personal_labelframe.grid(row=1, column=0, padx=(window.winfo_width() - t_personal_frame.winfo_reqwidth()) // 4)

    personal_title = tk.Label(t_personal_frame, text='Edit details', font=('Arial Bold', 30))
    personal_title.grid(row=0, column=0, pady=30)

    #  Currently set name and current title

    current_title = tk.Label(t_personal_labelframe, text='Current details', font=('tkDefault', 20))
    current_title.grid(row=0, column=1, padx=5, pady=5)



    # Edit column title
    edit_title = tk.Label(t_personal_labelframe, text='Edit', font=('tkDefault', 20))
    edit_title.grid(row=0, column=2, padx=5, pady=5)

    # Name entry box
    name_label = tk.Label(t_personal_labelframe, text='Name: ', font=('tkDefault', 15))
    name_label.grid(row=1, column=0, padx=5, pady=5)
    preset_name = tk.Label(t_personal_labelframe, text=y_personal_info[username]['name'],
                           font=('tkDefault', 15))
    preset_name.grid(row=1, column=1, padx=5, pady=5)
    t_personal_nameEntry = tk.Entry(t_personal_labelframe,)
    t_personal_nameEntry.grid(row=1, column=2, padx=5, pady=5, sticky='ew')

    # Email header/label
    # t_personal_email = tk.Label(t_personal_labelframe, text=' Edit Email address')
    # Current email
    email_label = tk.Label(t_personal_labelframe, text='Email address: ', font=('tkDefault', 15))
    email_label.grid(row=2, column= 0, padx=5, pady=5)
    personal_email = tk.Label(t_personal_labelframe,
                                   text=y_personal_info[username]['Email Address'],
                                   font=('tkDefault', 15))
    personal_email.grid(row=2, column=1, padx=5, pady=5)

    # Email entry box
    t_personal_emailEntry = tk.Entry(t_personal_labelframe)
    t_personal_emailEntry.grid(row=2, column=2, padx=5, pady=5, sticky='ew')
    # t_phonenumber = tk.Label(t_personal_labelframe, text='Edit Phone number')

    # Phone number Entry and label
    phone_label = tk.Label(t_personal_labelframe, text='Phone number: ', font=('tkDefault', 15))
    phone_label.grid(row=3, column=0, padx=5, pady=5)
    phone_number = tk.Label(t_personal_labelframe,
                                 text=int(y_personal_info[username]['Phone Number']),
                                 font=('tkDefault', 15))
    phone_number.grid(row=3, column=1, padx=5, pady=5)
    t_phonenumberEntry = tk.Entry(t_personal_labelframe)
    t_phonenumberEntry.grid(row=3, column=2, padx=5, pady=5, sticky='ew')

    # Commitment label
    commitment_type = tk.Label(t_personal_labelframe, text='Commitment type: ', font=('tkDefault', 15))
    commitment_type.grid(row=4, column=0, padx=5, pady=5)
    commitment_label = tk.Label(t_personal_labelframe,
                                     text=y_personal_info[username]['Commitment'],
                                     font=('tkDefault', 15))
    commitment_label.grid(row=4, column=1, padx=5, pady=5)

    # Commitment type entry
    t_commitmentEntry = ttk.Combobox(t_personal_labelframe,
                                          values=['Full time', 'Part time', 'Occasional'],
                                          state='readonly')
    t_commitmentEntry.grid(row=4, column=2, padx=5, pady=5, sticky='ew')

    # Work type label
    work_type = tk.Label(t_personal_labelframe, text='Work type: ', font=('tkDefault', 15))
    work_type.grid(row=5, column=0, padx=5, pady=5)
    work_type_label = tk.Label(t_personal_labelframe,
                                    text=y_personal_info[username]['Work Type'],
                                    font=('tkDefault', 15))
    work_type_label.grid(row=5, column=1, padx=5, pady=5)

    # Work type entry
    t_worktypeEntry = ttk.Combobox(t_personal_labelframe, values=['Medical Aid', 'Food counselling'])
    t_worktypeEntry.grid(row=5, column=2, padx=5, pady=5, sticky='ew')

    # Store details box
    t_store_details = tk.Button(t_personal_labelframe, text='Store details', command=lambda: [store_details_callback(t_personal_nameEntry, t_personal_emailEntry, t_phonenumberEntry, t_commitmentEntry, t_worktypeEntry), t_back_to_details],
                                     height=1, width=20)
    t_store_details.grid(row=6, column=1, padx=5, pady=5)

    # Back to details page
    t_back_to_details = tk.Button(t_personal_labelframe, text='Back to volunteer details', command=t_personal_information_base)
    t_back_to_details.grid(row=6, column=2, padx=5, pady=5)

    back_to_summary = tk.Button(t_personal_labelframe, text='Back to Home',
                                     command=back_button_to_volunteer_main)
    back_to_summary.grid(row=6, column=0, padx=5, pady=5)

    for i in range(7):
        t_personal_frame.grid_rowconfigure(i, weight=1)
    t_personal_frame.grid_columnconfigure(0, weight=1)


    def new_refugee(window, y_camp_info, refugee_info, back_button_to_volunteer_main, store_details_callback):
        for i in window.winfo_children():
            i.grid_forget()
        # Main frame for this whole page
        refugeeframe = tk.Frame(window)
        refugeeframe.grid()
        crisis_df = pd.read_csv('crisis_events.csv')
        camp_IDs = list(crisis_df['Camp ID'])

        # Title for the page
        refugee_title = tk.Label(refugeeframe, text='Create Refugee Profile', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=1, pady=30)

        # Label frame for this page that then stores all of the labels and entries
        refugee_labelframe = tk.LabelFrame(refugeeframe)
        refugee_labelframe.grid(row=1, column=1)

        # Camp ID
        t_camp_ID_label = tk.Label(refugee_labelframe, text='Camp ID', font=('TkinterDefault', 15))
        t_camp_ID_label.grid(row=3, column=3)
        t_camp_IDbox = ttk.Combobox(refugee_labelframe, values=camp_IDs)
        t_camp_IDbox.grid(row=3, column=4, padx=5)

        # Refugee name
        name_label = tk.Label(refugee_labelframe, text='Name', font=('TkinterDefault', 15))
        name_label.grid(row=5, column=3, padx=5)
        name_entry = tk.Entry(refugee_labelframe)
        name_entry.grid(row=5, column=4, padx=5)

        # Family members
        family_label = tk.Label(refugee_labelframe, text='Enter total number of family members',
                                font=('TkinterDefault', 15))
        family_label.grid(row=7, column=3, padx=5)
        family_labelbox = ttk.Spinbox(refugee_labelframe, from_=0, to=20, style='info.TSpinbox')
        family_labelbox.grid(row=7, column=4, padx=5)

        # Medical conditions, we need to add dictionaries and everything for this
        medical_conditionslabel = tk.Label(refugee_labelframe,
                                           text='Enter any medical condition(s) for each family member. If none, please enter \"none\"',
                                           font=("TkinterDefault", 15))
        medical_conditionslabel.grid(row=9, column=3, padx=5)
        t_medical_conditionsEntry = tk.Entry(refugee_labelframe)
        t_medical_conditionsEntry.grid(row=9, column=4, padx=5)

        # Languages spoken by refugees
        languages_spokenlabel = tk.Label(refugee_labelframe, text='Please select main language spoken in the family',
                                         font=('TkinterDefault', 15))
        languages_spokenlabel.grid(row=11, column=3, padx=5)
        t_languages_spokenEntry = ttk.Combobox(refugee_labelframe,
                                               values='English Chinese Hindi Spanish French Arabic Bengali Portuguese Russian Urdu Indonesian German Swahili Marathi Tamil Telugu Turkish Vietnamese Korean Italian Thai Gujarati Persian Polish Pashto Kannada Ukrainian Somali Kurdish')
        t_languages_spokenEntry.grid(row=11, column=4, padx=5)

        # secondlanguage entry box
        second_languagelabel = tk.Label(refugee_labelframe,
                                        text='Please enter any other languages spoken by each family member. If none, please enter \'none\'',
                                        font=('TkinterDefault', 15))
        second_languagelabel.grid(row=13, column=3, padx=5)
        t_second_languageEntry = tk.Entry(refugee_labelframe)
        t_second_languageEntry.grid(row=13, column=4, padx=5)

        na_store_details = tk.Button(refugee_labelframe, text="Store refugee info", command=lambda: [
            store_details_callback(t_camp_IDbox, family_labelbox, t_medical_conditionsEntry, t_languages_spokenEntry,
                                   t_second_languageEntry, name_entry), back_button_to_volunteer_main], height=1,
                                     width=20)
        na_store_details.grid(row=15, column=3)

        # Back button
        t_back_button = tk.Button(refugee_labelframe, text='Back to Home', command=back_button_to_volunteer_main)
        t_back_button.grid(row=17, column=3, padx=5, pady=10)

        for i in range(11):
            t_personal_frame.grid_rowconfigure(i, weight=1)
        t_personal_frame.grid_columnconfigure(0, weight=1)

    return t_personal_nameEntry, t_personal_emailEntry,t_phonenumberEntry, t_commitmentEntry, t_worktypeEntry



def store_personal_details(username, y_personal_info, t_personal_nameEntry, t_personal_emailEntry, t_phonenumberEntry, t_commitmentEntry, t_worktypeEntry):
    try:
        # Update self.y_personal_info dictionary
        if t_personal_nameEntry.get() == '':
            name = y_personal_info[username]['name']
        else:
            name = t_personal_nameEntry.get()
        if t_personal_emailEntry.get() == '':
            email = y_personal_info[username]['Email Address']
        else:
            email = t_personal_emailEntry.get()
        if t_phonenumberEntry.get() == '':
            phone = int(y_personal_info[username]['Phone Number'])
        else:
            phone = t_phonenumberEntry.get()
        if t_commitmentEntry.get() == '':
            commitment = y_personal_info[username]['Commitment']
        else:
            commitment = t_commitmentEntry.get()
        if t_worktypeEntry.get() == '':
            work = y_personal_info[username]['Work Type']
        else:
            work = t_worktypeEntry.get()
        # If entered non-alpha characters, raise error
        if re.search(r'^[A-Za-z]', name):
                y_personal_info[username]['name'] = name.strip()
        else:
            raise invalid_name
        # If entered non-number characters, raise error
        if re.search(r'^[0-9]+', phone):
            y_personal_info[username]['Phone Number'] = str(phone)
        else:
            raise invalid_phone_number
        # Make sure they include correct email format
        if re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
            y_personal_info[username]['Email Address'] = email
        else:
            raise invalid_email

        y_personal_info[username]['Work Type'] = work
        y_personal_info[username]['Commitment'] = commitment
        new_data = pd.DataFrame.from_dict(y_personal_info, orient='index')
        new_data.index.name = 'Username'
        new_data.to_csv('volunteer_info.csv')

        tk.messagebox.showinfo(title='Saved', message='Details have been saved\n '
                                                      'Please click "Back to Volunteer Details" to view updated details')




    except(invalid_email):
        tk.messagebox.showinfo(title='Invalid Email', message='Please enter a valid email address')
    except(invalid_phone_number):
        tk.messagebox.showinfo(title='Invalid Phone Number',
                                       message='Please enter a valid phone number')
    except(invalid_name):
         tk.messagebox.showinfo(title='Invalid Name', message='Please enter a valid name')

            
        # Go back to the details page
        #personal_information()
    except FileNotFoundError:
        y_personal_info = {
            'volunteer1': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': False, 'Deleted': False},
           'volunteer2': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': False, 'Deleted': False},
            'volunteer3': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': True, 'Deleted': False},
            'volunteer4': {'password': '111', 'name': '', 'Email Address': '', 'Phone Number': '', 'Commitment': '',
                           'Work Type': '', 'Deactivated': False, 'Deleted': False}
            }

        df = pd.DataFrame.from_dict(y_personal_info, orient='index')
        df.index.name = 'Username'
        df.to_csv('volunteer_info.csv', index='Username')
        y_personal_info = pd.read_csv('volunteer_info.csv')



