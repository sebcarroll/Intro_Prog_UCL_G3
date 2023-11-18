import tkinter as tk
from tkinter import ttk
import pickle


def new_plan(window, back_button_to_admin_main):
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
    camp_ID_label = tk.Label(new_plan_labelframe, text='New Camp ID', font=('TkinterDefault', 15))
    camp_ID_label.grid(row=3, column=3)
    id_not_taken = ['1','2','3','4','5']
    camp_IDbox = ttk.Combobox(new_plan_labelframe, values=id_not_taken)
    camp_IDbox.grid(row=3, column=4, padx=5)

    # Crisis Type
    crisis_type_label = tk.Label(new_plan_labelframe, text='Crisis Type', font=('TkinterDefault', 15))
    crisis_type_label.grid(row=5, column=3, padx=5)
    crisis_type = ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]
    crisis_type_labelbox = ttk.Spinbox(new_plan_labelframe, values=crisis_type, style='info.TSpinbox')
    crisis_type_labelbox.grid(row=5, column=4, padx=5)

    # Description of Crisis:
    description_label = tk.Label(new_plan_labelframe, text='Description', font=('TkinterDefault', 15))
    description_label.grid(row=7, column=3, padx=5)
    description_label_Entry = tk.Text(new_plan_labelframe, height=10, width=40)
    description_label_Entry.grid(row=7, column=4, padx=5)

    # Country of Crisis:
    country_label = tk.Label(new_plan_labelframe, text='Country of crisis', font=('TkinterDefault', 15))
    country_label.grid(row=9, column=3, padx=5)
    country_Entry = ttk.Combobox(new_plan_labelframe, values=susceptible_countries)
    country_Entry.grid(row=9, column=4, padx=5)

    # Name of Admin Creator
    created_by_label = tk.Label(new_plan_labelframe, text='Enter your name', font=("TkinterDefault", 15))
    created_by_label.grid(row=11, column=3, padx=5)
    created_by_Entry = tk.Entry(new_plan_labelframe)
    created_by_Entry.grid(row=11, column=4, padx=5)


    # Buttons:
    # Save
    save_plan_button = tk.Button(new_plan_labelframe, text="Save plan", command=store_plan_details, height=1, width=20)
    save_plan_button.grid(row=17, column=3)
    # Back button
    back_button = tk.Button(new_plan_labelframe, text='Back to Home', command=back_button_to_admin_main)
    back_button.grid(row=17, column=1, padx=5, pady=10)


def store_plan_details():
    #write function to store pickle - use append to document
    pass

susceptible_countries = [
    "Afghanistan",
    "Syria",
    "Yemen",
    "South Sudan",
    "Somalia",
    "Sudan",
    "Democratic Republic of the Congo",
    "Venezuela",
    "Iraq",
    "Nigeria",
    "Ethiopia",
    "Myanmar",
    "Haiti",
    "Central African Republic",
    "Libya",
    "Chad",
    "Mali",
    "Niger",
    "Cameroon",
    "Ukraine",
    "Pakistan",
    "Bangladesh",
    "Lebanon",
    "Zimbabwe",
    "Eritrea",
    "North Korea",
    "Eswatini",
    "Zambia",
    "Malawi",
]