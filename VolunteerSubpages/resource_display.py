import tkinter as tk
from tkinter import ttk
import pandas as pd


def resource_display(window, back_button_to_volunteer_main):
    for i in window.winfo_children():
        i.grid_forget()
    resources_frame = tk.Frame(window)
    resources_frame.grid()

    crisis_df = pd.read_csv('crisis_events.csv')

    resources_df = crisis_df.loc[:, ['Camp ID', 'Meals(T)', 'Medicine(T)', 'Duration', 'Capacity',
                                     'Meals/w', 'Medicine/w']]

    resources_df = resources_df.fillna(0)

    # Convert float columns to integers
    float_columns = ['Meals(T)', 'Medicine(T)', 'Duration', 'Capacity', 'Meals/w', 'Medicine/w']
    for col in float_columns:
        resources_df[col] = resources_df[col].astype(int)

    columns = ['Camp ID', 'Capacity', 'Meals(T)', 'Medicine(T)', 'Meals/w', 'Medicine/w', 'Delivery Time(d)']

    total_meals = 100000000
    total_medicine = 100000000
    meals_used = resources_df['Meals(T)'].sum()
    medicine_used = resources_df['Medicine(T)'].sum()
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
    tree.heading('Capacity', text='Capacity')
    tree.heading('Meals(T)', text='Meals')
    tree.heading('Medicine(T)', text='Medicine')
    tree.heading('Meals/w', text='Weekly meals per refugee')
    tree.heading('Medicine/w', text='Weekly medication per refugee')
    tree.heading('Delivery Time(d)', text='Delivery Time(d)')


    tree.column('Camp ID', anchor="center", width=80)
    tree.column('Capacity', anchor="center", width=105)
    tree.column('Meals(T)', anchor="center", width=100)
    tree.column('Medicine(T)', anchor="center", width=125)
    tree.column('Meals/w', anchor="center", width=150)
    tree.column('Medicine/w', anchor="center", width=175)
    tree.column('Delivery Time(d)', anchor="center", width=125)


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

