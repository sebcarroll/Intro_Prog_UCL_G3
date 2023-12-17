import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import csv

def new_refugee(window, y_camp_info, refugee_info, back_button_to_volunteer_main, store_details_callback):
    for i in window.winfo_children():
        i.grid_forget()
    for i in range(9):
        window.grid_columnconfigure(i, weight=1)
    refugeeframe = tk.Frame(window)
    refugeeframe.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
    for i in range(9):
        refugeeframe.grid_columnconfigure(i, weight=1)
    for i in range(9):
        refugeeframe.grid_rowconfigure(i, weight=1)

    try:
        crisis_df = pd.read_csv('crisis_events.csv')
        active_crisis_df = crisis_df[crisis_df['Status'] != 'Inactive']
        camp_IDs = list(active_crisis_df['Camp ID'])
    except:
        camp_IDs = []

    # Title for the page
    refugee_title = tk.Label(refugeeframe, text='Create Refugee Profile', font=('TKDefault', 25), fg='white')
    refugee_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
    refugee_title.configure(background="grey")

    # Label frame for this page that then stores all of the labels and entries
    refugee_labelframe = tk.Frame(refugeeframe)
    refugee_labelframe.grid(row=1, column=4, pady=30, sticky="ew", columnspan=3)

    # Camp ID
    t_camp_ID_label = tk.Label(refugee_labelframe, text='Camp ID (This will be generated randomly on submission)', font=('TkinterDefault', 15))
    t_camp_ID_label.grid(row=2, column=0, padx=20)
    t_camp_IDbox = ttk.Combobox(refugee_labelframe, values=camp_IDs, state='readonly')
    t_camp_IDbox.grid(row=2, column=2, padx=5, pady=10)

    # Refugee name
    name_label = tk.Label(refugee_labelframe, text='Family Name', font=('TkinterDefault', 15))
    name_label.grid(row=3, column=0, padx=20, pady=10)
    name_entry = tk.Entry(refugee_labelframe)
    name_entry.grid(row=3, column=2, padx=5, pady=10)

    # Family members
    family_label = tk.Label(refugee_labelframe, text='Total number of family members',
                            font=('TkinterDefault', 15))
    family_label.grid(row=4, column=0, padx=20, pady=10)
    family_labelbox = ttk.Spinbox(refugee_labelframe, from_=1, to=20, style='info.TSpinbox')
    family_labelbox.grid(row=4, column=2, padx=5, pady=10)

    # Medical conditions, we need to add dictionaries and everything for this
    medical_conditionslabel = tk.Label(refugee_labelframe,
                                       text='Medical condition(s) for each family member',
                                       font=("TkinterDefault", 15))
    medical_conditionslabel.grid(row=5, column=0, padx=20, pady=10)
    t_medical_conditionsEntry = tk.Entry(refugee_labelframe)
    t_medical_conditionsEntry.grid(row=5, column=2, padx=5, pady=10)

    # Languages spoken by refugees
    languages_spokenlabel = tk.Label(refugee_labelframe, text='Main language(s) spoken in the family',
                                     font=('TkinterDefault', 15))
    languages_spokenlabel.grid(row=6, column=0, padx=20, pady=10)
    t_languages_spokenEntry = ttk.Combobox(refugee_labelframe,
                                           values='English Chinese Hindi Spanish French Arabic Bengali Portuguese Russian Urdu Indonesian German Swahili Marathi Tamil Telugu Turkish Vietnamese Korean Italian Thai Gujarati Persian Polish Pashto Kannada Ukrainian Somali Kurdish')
    t_languages_spokenEntry.grid(row=6, column=2, padx=5, pady=10)

    # secondlanguage entry box
    second_languagelabel = tk.Label(refugee_labelframe,
                                    text='Other language(s) spoken by family member(s)',
                                    font=('TkinterDefault', 15))
    second_languagelabel.grid(row=7, column=0, padx=20, pady=10)
    t_second_languageEntry = tk.Entry(refugee_labelframe)
    t_second_languageEntry.grid(row=7, column=2, padx=5, pady=10)

    na_store_details = tk.Button(refugee_labelframe, text="Store refugee info", command=lambda: [
        store_details_callback(t_camp_IDbox, family_labelbox, t_medical_conditionsEntry, t_languages_spokenEntry,
                               t_second_languageEntry, name_entry), back_button_to_volunteer_main], height=1, width=20)
    na_store_details.grid(row=9, column=2, pady=(50,20))

    # Back button
    t_back_button = tk.Button(refugee_labelframe, text='Back to Home', command=back_button_to_volunteer_main)
    t_back_button.grid(row=9, column=0, padx=5, pady=(50,20))

    for i in range(10):
        refugeeframe.grid_rowconfigure(i, weight=1)
    refugeeframe.grid_columnconfigure(0, weight=1)

    return t_camp_IDbox, name_entry, t_medical_conditionsEntry, t_languages_spokenEntry, t_second_languageEntry


def na_refugee_info_dict(refugee_info, t_camp_IDbox, family_labelbox, t_medical_conditionsEntry, t_languages_spokenEntry,
                               t_second_languageEntry, name_entry):
    try:
        # Update self.t_create_refugee dictionary
        refugee_info = pd.read_csv('refugee_info.csv', index_col='Name')


        camp_ID = int(t_camp_IDbox.get())
        name = name_entry.get()
        family_members = family_labelbox.get()
        medical_conditions = t_medical_conditionsEntry.get()
        languages_spoken = t_languages_spokenEntry.get()
        second_language = t_second_languageEntry.get()
        refugee_info.loc[name,'Camp ID'] = camp_ID
        camp_ID = int(camp_ID)
        refugee_info.loc[name,'Medical Conditions'] = medical_conditions
        refugee_info.loc[name, 'Languages Spoken'] = languages_spoken
        refugee_info.loc[name, 'Second Language'] = second_language
        refugee_info.loc[name, 'Family Members'] = family_members

        # new_refugee_info.index.name = 'Name'
        refugee_info.to_csv('refugee_info.csv')
        update_number_of_refugees(camp_ID)
        tk.messagebox.showinfo(title='Details saved', message='Details have been saved')

        clear_entry(name_entry)
        clear_entry(family_labelbox)
        clear_entry(t_medical_conditionsEntry)
        clear_entry(t_languages_spokenEntry)
        clear_entry(t_second_languageEntry)

    except FileNotFoundError:
        data = {'Name': [name], 'Camp ID': [camp_ID],
                'Medical Conditions': [medical_conditions],
                'Languages Spoken': [languages_spoken],
                'Second Language': [second_language],
                'Family Members': [family_members]}
        refugee_info = pd.DataFrame(data)
        refugee_info.set_index('Name', inplace=True)
        refugee_info.to_csv('refugee_info.csv')

def update_number_of_refugees(camp_ID):
    number_of_refugees_actual = 0
    with open('refugee_info.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row[1] == '':
                number_of_refugees_actual = 1
            elif camp_ID == int(float(row[1])):
                number_of_refugees_actual += 1
    #print(f"Total refugees counted: {number_of_refugees_actual}")

    header = []
    data = []

    with open('crisis_events.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = list(csv_reader)

    for row in data:
        if int(float(row[0])) == int(camp_ID):
            row[16] = str(number_of_refugees_actual)

    with open('crisis_events.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def clear_entry(entry):
    #entry.delete(0, tk.END)
    # clear different types of widgets entry, combobox and text boxes
    if isinstance(entry, tk.Entry):
        entry.delete(0, tk.END)
    elif isinstance(entry, ttk.Combobox):
        entry.set('')
    elif isinstance(entry, tk.Text):
        entry.delete("1.0", tk.END)