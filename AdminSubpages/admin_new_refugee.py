import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import csv

def new_refugee(window, y_camp_info, refugee_info, back_button_to_volunteer_main, store_details_callback):
    for i in window.winfo_children():
        i.grid_forget()
    # Main frame for this whole page
    refugeeframe = tk.Frame(window)
    refugeeframe.grid()

    try:
        crisis_df = pd.read_csv('crisis_events.csv')
        active_crisis_df = crisis_df[crisis_df['Status'] != 'Inactive']
        camp_IDs = list(active_crisis_df['Camp ID'])
    except:
        camp_IDs = []

    # Title for the page
    refugee_title = tk.Label(refugeeframe, text='Create Refugee Profile', font=('TkinterDefault', 30))
    refugee_title.grid(row=0, column=0, pady=30)

    # Label frame for this page that then stores all of the labels and entries
    refugee_labelframe = tk.LabelFrame(refugeeframe)
    refugee_labelframe.grid(row=1, column=0)

    # Camp ID
    t_camp_ID_label = tk.Label(refugee_labelframe, text='Camp ID', font=('TkinterDefault', 15))
    t_camp_ID_label.grid(row=2, column=0)
    t_camp_IDbox = ttk.Combobox(refugee_labelframe, values=camp_IDs)
    t_camp_IDbox.grid(row=2, column=1, padx=5, pady=5)

    # Refugee name
    name_label = tk.Label(refugee_labelframe, text='Family Name', font=('TkinterDefault', 15))
    name_label.grid(row=3, column=0, padx=5, pady=5)
    name_entry = tk.Entry(refugee_labelframe)
    name_entry.grid(row=3, column=1, padx=5, pady=5)

    # Family members
    family_label = tk.Label(refugee_labelframe, text='Enter total number of family members',
                            font=('TkinterDefault', 15))
    family_label.grid(row=4, column=0, padx=5, pady=5)
    family_labelbox = ttk.Spinbox(refugee_labelframe, from_=0, to=20, style='info.TSpinbox')
    family_labelbox.grid(row=4, column=1, padx=5, pady=5)

    # Medical conditions, we need to add dictionaries and everything for this
    medical_conditionslabel = tk.Label(refugee_labelframe,
                                       text='Enter any medical condition(s) for each family member',
                                       font=("TkinterDefault", 15))
    medical_conditionslabel.grid(row=5, column=0, padx=5, pady=5)
    t_medical_conditionsEntry = tk.Entry(refugee_labelframe)
    t_medical_conditionsEntry.grid(row=5, column=1, padx=5, pady=5)

    # Languages spoken by refugees
    languages_spokenlabel = tk.Label(refugee_labelframe, text='Please select main language spoken in the family',
                                     font=('TkinterDefault', 15))
    languages_spokenlabel.grid(row=6, column=0, padx=5, pady=5)
    t_languages_spokenEntry = ttk.Combobox(refugee_labelframe,
                                           values='English Chinese Hindi Spanish French Arabic Bengali Portuguese Russian Urdu Indonesian German Swahili Marathi Tamil Telugu Turkish Vietnamese Korean Italian Thai Gujarati Persian Polish Pashto Kannada Ukrainian Somali Kurdish')
    t_languages_spokenEntry.grid(row=6, column=1, padx=5, pady=5)

    # secondlanguage entry box
    second_languagelabel = tk.Label(refugee_labelframe,
                                    text='Please enter any other languages spoken by each family member',
                                    font=('TkinterDefault', 15))
    second_languagelabel.grid(row=7, column=0, padx=5, pady=5)
    t_second_languageEntry = tk.Entry(refugee_labelframe)
    t_second_languageEntry.grid(row=7, column=1, padx=5, pady=5)

    na_store_details = tk.Button(refugee_labelframe, text="Store refugee info", command=lambda: [
        store_details_callback(t_camp_IDbox, family_labelbox, t_medical_conditionsEntry, t_languages_spokenEntry,
                               t_second_languageEntry, name_entry), back_button_to_volunteer_main], height=1, width=20)
    na_store_details.grid(row=8, column=1, pady=5)

    # Back button
    t_back_button = tk.Button(refugee_labelframe, text='Back to Home', command=back_button_to_volunteer_main)
    t_back_button.grid(row=9, column=0, padx=5, pady=10)

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
    print(f"Total refugees counted: {number_of_refugees_actual}")

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