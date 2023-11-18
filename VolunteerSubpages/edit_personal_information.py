import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import re
#from VolunteerSubpages.personal_information import personal_information

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
    t_personal_labelframe.grid(row=3, column=3)

    personal_title = tk.Label(t_personal_frame, text='Edit details', font=('Arial Bold', 30))
    personal_title.grid(row=0, column=3, pady=30)

    #  Currently set name and current title
    current_title = tk.Label(t_personal_labelframe, text='Current details', font=('tkDefault', 20))
    current_title.grid(row=4, column=2)

    preset_name = tk.Label(t_personal_labelframe, text=y_personal_info[username]['name'],
                                font=('tkDefault', 15))
    preset_name.grid(row=5, column=2, padx=5)

    # Edit column title
    edit_title = tk.Label(t_personal_labelframe, text='Edit', font=('tkDefault', 20))
    edit_title.grid(row=4, column=3, padx=5)

    # Name entry box
    t_personal_nameEntry = tk.Entry(t_personal_labelframe, text='name')
    t_personal_nameEntry.grid(row=5, column=3)

    # Email header/label
    # t_personal_email = tk.Label(t_personal_labelframe, text=' Edit Email address')
    # Current email
    personal_email = tk.Label(t_personal_labelframe,
                                   text=y_personal_info[username]['Email Address'],
                                   font=('tkDefault', 15))
    personal_email.grid(row=7, column=2, padx=5)

    # Email entry box
    t_personal_emailEntry = tk.Entry(t_personal_labelframe)
    t_personal_emailEntry.grid(row=7, column=3)
    # t_phonenumber = tk.Label(t_personal_labelframe, text='Edit Phone number')

    # Phone number Entry and label
    phone_number = tk.Label(t_personal_labelframe,
                                 text=y_personal_info[username]['Phone Number'],
                                 font=('tkDefault', 15))
    phone_number.grid(row=9, column=2, padx=5)
    t_phonenumberEntry = tk.Entry(t_personal_labelframe)
    t_phonenumberEntry.grid(row=9, column=3)

    # Commitment label
    commitment_label = tk.Label(t_personal_labelframe,
                                     text=y_personal_info[username]['Commitment'],
                                     font=('tkDefault', 15))
    commitment_label.grid(row=11, column=2, padx=5)

    # Commitment type entry
    t_commitmentEntry = ttk.Combobox(t_personal_labelframe,
                                          values=['Full time', 'Part time', 'Occasional'],
                                          state='readonly')
    t_commitmentEntry.grid(row=11, column=3)

    # Work type label
    work_type_label = tk.Label(t_personal_labelframe,
                                    text=y_personal_info[username]['Work Type'],
                                    font=('tkDefault', 15))
    work_type_label.grid(row=13, column=2, padx=5)

    # Work type entry
    t_worktypeEntry = ttk.Combobox(t_personal_labelframe, values=['Medical Aid', 'Food counselling'])
    t_worktypeEntry.grid(row=13, column=3)

    # Store details box
    t_store_details = tk.Button(t_personal_frame, text='Store details', command=lambda: store_details_callback(t_personal_nameEntry, t_personal_emailEntry, t_phonenumberEntry, t_commitmentEntry, t_worktypeEntry),
                                     height=1, width=20)
    t_store_details.grid(row=17, column=3)

    # Back to details page
    t_back_to_details = tk.Button(t_personal_frame, text='Back to volunteer details', command=t_personal_information_base)
    t_back_to_details.grid(row=17, column=1)

    back_to_summary = tk.Button(t_personal_frame, text='Back to Home',
                                     command=back_button_to_volunteer_main)
    back_to_summary.grid(row=17, column=5)

    return t_personal_nameEntry, t_personal_emailEntry,t_phonenumberEntry, t_commitmentEntry, t_worktypeEntry



def store_personal_details(username, y_personal_info, t_personal_nameEntry, t_personal_emailEntry, t_phonenumberEntry, t_commitmentEntry, t_worktypeEntry):
    try:
        # Update y_personal_info dictionary
        with open('data.pickle', 'wb') as file:
            name = t_personal_nameEntry.get()
            email = t_personal_emailEntry.get()
            phone = t_phonenumberEntry.get()
            commitment = t_commitmentEntry.get()
            work = t_worktypeEntry.get()

            try:
                # If entered non-alpha characters, raise error
                if re.search(r'^[A-Za-z]', name):
                    y_personal_info[username]['name'] = name.strip()
                else:
                    raise invalid_name

                # If entered non-number characters, raise error
                if re.search(r'^[0-9]+', phone):
                    y_personal_info[username]['Phone Number'] = phone
                else:
                    raise invalid_phone_number
                # Make sure they include correct email format
                if re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
                    y_personal_info[username]['Email Address'] = email
                else:
                    raise invalid_email

                y_personal_info[username]['Work Type'] = work
                y_personal_info[username]['Commitment'] = commitment

            except(invalid_email):
                tk.messagebox.showinfo(title='Invalid Email', message='Please enter a valid email address')
            except(invalid_phone_number):
                tk.messagebox.showinfo(title='Invalid Phone Number',
                                       message='Please enter a valid phone number')
            except(invalid_name):
                tk.messagebox.showinfo(title='Invalid Name', message='Please enter a valid name')

            pickle.dump(y_personal_info, file)
        # Go back to the details page
        #personal_information()
    except FileNotFoundError:
        pass