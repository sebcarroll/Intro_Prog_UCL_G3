import tkinter as tk
from tkinter import ttk
import pandas as pd

def label_sufficient(value):
    if value == 0:
        return 'Sufficient'
    elif value < 0:
        return 'Excess'
    else:
        return value

def resource_display(window, back_button_to_volunteer_main):
    for i in window.winfo_children():
        i.grid_forget()
    resources_frame = tk.Frame(window)
    resources_frame.grid()

    crisis_df = pd.read_csv('crisis_events.csv')

    crisis_df['weeks_food_supply'] = crisis_df['Total Meals'] / (crisis_df['Number of Refugees'] * crisis_df['Meals /week'])
    crisis_df['weeks_med_supply'] = crisis_df['Total Medicine'] / (crisis_df['Number of Refugees'] * crisis_df['Medicine /week'])

    crisis_df['Meals req'] = ((crisis_df['Crisis Length'] - crisis_df['weeks_food_supply']) *
                              crisis_df['Meals /week'] * crisis_df['Number of Refugees'])


    crisis_df['Medicine req'] = ((crisis_df['Crisis Length'] - crisis_df['weeks_med_supply'])
                                 * crisis_df['Medicine /week'] * crisis_df['Number of Refugees'])

    crisis_df['Medicine req'] = crisis_df['Medicine req'].apply(label_sufficient)
    crisis_df['Meals req'] = crisis_df['Meals req'].apply(label_sufficient)


    print(crisis_df)

    print(crisis_df)



    resources_df = crisis_df.loc[:, ['Camp ID', 'Total Meals', 'Total Medicine', 'Crisis Length', 'Number of Refugees',
                                     'Meals req', 'Medicine req']]
    resources_df = resources_df.fillna(0)
    columns = ['Camp ID', 'Number of Refugees', 'Total Meals', 'Total Medicine', 'Meals req', 'Meds req']

    total_meals = 100000000
    total_medicine = 100000000
    meals_used = resources_df['Total Meals'].sum()
    medicine_used = resources_df['Total Medicine'].sum()
    leftover_meals = total_meals - meals_used
    leftover_medicine = total_medicine - medicine_used

    # GIVES THE LEFT FRAME
    availability_frame = tk.Frame(resources_frame, width=150, height=400)
    availability_frame.grid(row=4, column=0, padx=10, pady=5)

    available_meals = tk.Label(availability_frame, text='Meals Left:', font=('Helvetica', 12))
    available_meals.grid(row=0, column=0)

    available_meals_number = tk.Label(availability_frame, text=f"{leftover_meals}", font=('Helvetica', 12))
    available_meals_number.grid(row=0, column=20)

    available_meds = tk.Label(availability_frame, text=f"Medicine Left", font=('Helvetica', 12))
    available_meds.grid(row=5, column=0)

    available_meds_number = tk.Label(availability_frame, text=f"{leftover_medicine}", font=('Helvetica', 12))
    available_meds_number.grid(row=5, column=20)

    # GIVES THE RIGHT FRAME
    resources_df_frame = tk.Frame(resources_frame, width=150, height=400)
    resources_df_frame.grid(row=4, column=5, padx=10, pady=5)

    tree = ttk.Treeview(resources_df_frame, columns=columns, show='headings')

    tree.heading('Camp ID', text='Camp ID')
    tree.heading('Number of Refugees', text='Refugee no.')
    tree.heading('Total Meals', text='Meals')
    tree.heading('Total Medicine', text='Medicine')
    tree.heading('Meals req', text='Meals required')
    tree.heading('Meds req', text='Meds required')

    tree.column('Camp ID', width=80)
    tree.column('Number of Refugees', width=100)
    tree.column('Total Meals', width=80)
    tree.column('Total Medicine', width=100)
    tree.column('Meals req', width=100)
    tree.column('Meds req', width=100)

    for _, row in resources_df.iterrows():
        tree.insert('', tk.END, values=row.tolist())

    scrollbar = ttk.Scrollbar(resources_df_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky='ns')
    tree.grid(row=0, column=0, sticky='nsew')

    # Title
    resources_title = tk.Label(resources_frame, text='Allocated Resources', font=('TkDefaultFont', 20))
    resources_title.grid(row=0, column=5, columnspan=2)


    t_back_button = tk.Button(resources_frame, text='Back to Home', command=back_button_to_volunteer_main)
    t_back_button.grid(row=20, column=0, padx=5, pady=10, columnspan=2)

