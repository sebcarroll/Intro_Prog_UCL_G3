import tkinter as tk
from tkinter import ttk
import pickle


def new_plan(window, y_camp_info, back_button_to_admin_main, store_plan_details_callback):
    for i in window.winfo_children():
        i.grid_forget()
    # Main frame for this whole page
    new_plan_frame = tk.Frame(window)
    new_plan_frame.grid()

    # Title for the page
    refugee_title = tk.Label(new_plan_frame, text='Create New Plan', font=('TkinterDefault', 30))
    refugee_title.grid(row=0, column=1, pady=30)

    # Label frame for this page that then stores all of the labels and entries
    new_plan_labelframe = tk.LabelFrame(new_plan_frame)
    new_plan_labelframe.grid(row=1, column=1)

    # Camp ID
    t_camp_ID_label = tk.Label(new_plan_labelframe, text='Camp ID', font=('TkinterDefault', 15))
    t_camp_ID_label.grid(row=3, column=3)
    t_camp_IDbox = ttk.Combobox(new_plan_labelframe, values=y_camp_info['Syria']['ID'])
    t_camp_IDbox.grid(row=3, column=4, padx=5)

    # Family members
    family_label = tk.Label(new_plan_labelframe, text='Enter total number of family members', font=('TkinterDefault', 15))
    family_label.grid(row=5, column=3, padx=5)
    family_labelbox = ttk.Spinbox(new_plan_labelframe, from_=0, to=20, style='info.TSpinbox')
    family_labelbox.grid(row=5, column=4, padx=5)

    # Medical conditions, we need to add dictionaries and everything for this
    medical_conditionslabel = tk.Label(new_plan_labelframe, text='Enter any medical condition(s) for each family member. If none, please enter \"none\"', font=("TkinterDefault", 15))
    medical_conditionslabel.grid(row=7, column=3, padx=5)
    t_medical_conditionsEntry = tk.Entry(new_plan_labelframe)
    t_medical_conditionsEntry.grid(row=7, column=4, padx=5)

    # Languages spoken by refugees
    languages_spokenlabel = tk.Label(new_plan_labelframe, text='Please select main language spoken in the family', font=('TkinterDefault', 15))
    languages_spokenlabel.grid(row=9, column=3, padx=5)
    t_languages_spokenEntry = ttk.Combobox(new_plan_labelframe,
                                                values='English Chinese Hindi Spanish French Arabic Bengali Portuguese Russian Urdu Indonesian German Swahili Marathi Tamil Telugu Turkish Vietnamese Korean Italian Thai Gujarati Persian Polish Pashto Kannada Ukrainian Somali Kurdish')
    t_languages_spokenEntry.grid(row=9, column=4, padx=5)

    # secondlanguage entry box
    second_languagelabel = tk.Label(new_plan_labelframe,
                                         text='Please enter any other languages spoken by each family member. If none, please enter \'none\'',
                                         font=('TkinterDefault', 15))
    second_languagelabel.grid(row=11, column=3, padx=5)
    t_second_languageEntry = tk.Entry(new_plan_labelframe)
    t_second_languageEntry.grid(row=11, column=4, padx=5)



    na_store_details = tk.Button(new_plan_labelframe, text="Store refugee info", command=lambda: store_plan_details_callback(t_camp_IDbox, family_labelbox, t_medical_conditionsEntry, t_languages_spokenEntry, t_second_languageEntry), height=1, width=20)
    na_store_details.grid(row=17, column=3)

    na_save_changes = tk.Button(new_plan_labelframe, text='Save changes', command='Store in dictionary')
    na_save_changes.grid(row=13, column=1, padx=5, pady=10)

    # Back button
    t_back_button = tk.Button(new_plan_labelframe, text='Back to Home', command=back_button_to_admin_main)
    t_back_button.grid(row=13, column=3, padx=5, pady=10)

    return t_camp_IDbox, family_labelbox, t_medical_conditionsEntry, t_languages_spokenEntry, t_second_languageEntry


def na_refugee_info_dict(na_refugee_info, t_camp_IDbox, family_labelbox, t_medical_conditionsEntry, t_languages_spokenEntry, t_second_languageEntry):
    try:
        # Update self.t_create_refugee dictionary
        with open('refugee.pickle', 'wb') as file:
            camp_ID = t_camp_IDbox.get()
            family_members = family_labelbox.get()
            medical_conditions = t_medical_conditionsEntry.get()
            languages_spoken = t_languages_spokenEntry.get()
            second_language = t_second_languageEntry.get()
            na_refugee_info['refugee1']['Camp ID'] = camp_ID
            na_refugee_info['refugee1']['Medical Conditions'] = medical_conditions
            na_refugee_info['refugee1']['Languages Spoken'] = languages_spoken
            na_refugee_info['refugee1']['Second Language'] = second_language
            na_refugee_info['refugee1']['Family Members'] = family_members

            pickle.dump(na_refugee_info, file)

    except FileNotFoundError:
        pass