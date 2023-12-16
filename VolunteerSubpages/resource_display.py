import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


def resource_display(window, camp_id, back_button_to_volunteer_main):
    # for i in window.winfo_children():
    #     i.grid_forget()
    # resources_frame = tk.Frame(window)
    # resources_frame.grid()
    for i in window.winfo_children():
        i.grid_forget()
    for i in range(9):
        window.grid_columnconfigure(i, weight=1)
    resources_frame = tk.Frame(window)
    resources_frame.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
    for i in range(9):
        resources_frame.grid_columnconfigure(i, weight=1)
    for i in range(8):
        resources_frame.grid_rowconfigure(i, weight=1)

    '''try:
        crisis_df = pd.read_csv('crisis_events.csv')
    except:
        # Create an empty DataFrame with the expected columns
        # columns = ['Camp ID', 'Meals(T)', 'Medicine(T)', 'Duration', 'Capacity', 'Meals/w', 'Medicine/w']
        # crisis_df = pd.DataFrame(columns=columns)
        messagebox.showwarning("No data found",
                               "There is a problem accessing the database\n\nThe file may be missing or corrupted")'''

    # Title
    resources_title = tk.Label(resources_frame, text='Allocated Resources', font=('TKDefault', 25), fg='white')
    resources_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
    resources_title.configure(background="grey")

    # GIVES THE LEFT FRAME
    availability_frame = tk.Frame(resources_frame)
    availability_frame.grid(row=2, column=0, padx=10, pady=5, columnspan=9)

    columns = ['Camp ID', 'Capacity', 'Meals(T)', 'Medicine(T)', 'Meals/w', 'Medicine/w', 'Delivery Time(d)']
    tree = ttk.Treeview(resources_frame, columns=columns, show='headings', height=5)
    tree.grid(row=1, column=0, columnspan=9, sticky="ew", padx=10, pady=5)

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


    view_button = tk.Button(resources_frame, text='View', command=lambda: view_csv_data_entry(tree))
    view_button.grid(row=4, column=0, padx=5, pady=10, columnspan=9)

    t_back_button = tk.Button(resources_frame, text='Back to Home', command=back_button_to_volunteer_main)
    t_back_button.grid(row=5, column=0, padx=5, pady=10, columnspan=9)

    try:
        crisis_df = pd.read_csv('crisis_events.csv')
        # Filter resources for the camp that the volunteer belongs to
        resources_df = crisis_df[crisis_df['Camp ID'] == camp_id].loc[:, ['Camp ID', 'Meals(T)', 'Medicine(T)', 'Duration', 'Capacity',
                                                                                            'Meals/w', 'Medicine/w']]

        # resources_df = crisis_df.loc[:, ['Camp ID', 'Meals(T)', 'Medicine(T)', 'Duration', 'Capacity',
        #                                  'Meals/w', 'Medicine/w']]

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

        available_meals = tk.Label(availability_frame, text='Meals Left:', font=('Helvetica', 12))
        available_meals.grid(row=0, column=0)

        available_meals_number = tk.Label(availability_frame, text=f"{leftover_meals}", font=('Helvetica', 12))
        available_meals_number.grid(row=0, column=20)

        available_meds = tk.Label(availability_frame, text=f"Medicine Left", font=('Helvetica', 12))
        available_meds.grid(row=5, column=0)

        available_meds_number = tk.Label(availability_frame, text=f"{leftover_medicine}", font=('Helvetica', 12))
        available_meds_number.grid(row=5, column=20)

        '''# GIVES THE RIGHT FRAME
        resources_df_frame = tk.Frame(resources_frame)
        resources_df_frame.grid(row=2, column=1, padx=10, pady=5)'''

        '''tree.heading('Camp ID', text='Camp ID')
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
        tree.column('Delivery Time(d)', anchor="center", width=125)'''

        for _, row in resources_df.iterrows():
            tree.insert('', tk.END, values=row.tolist())

        '''scrollbar = ttk.Scrollbar(resources_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=2, sticky='ns')'''

    except:
        # Create an empty DataFrame with the expected columns
        columns = ['Camp ID', 'Meals(T)', 'Medicine(T)', 'Duration', 'Capacity', 'Meals/w', 'Medicine/w']
        crisis_df = pd.DataFrame(columns=columns)
        messagebox.showwarning("No data found",
                               "There is a problem accessing the database\n\nThe file may be missing or corrupted")

def view_csv_data_entry(tree):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showinfo("No selection", "Please select a plan to view")
        return

    plan_details = tree.item(selected_item, 'values')

    # Attributes from the treeview
    column_attributes = tree['columns']
    treeview_width = len(column_attributes)

    # Open pop up edit window
    view_plan_window = tk.Toplevel()
    view_plan_window.title("View Plan")
    view_plan_window.grab_set()

    # Create a label and entry for each plan attribute using column attributes
    for i in range(treeview_width):
        att = column_attributes[i]
        value = plan_details[i]

        label = tk.Label(view_plan_window, text=f"{att}:")
        label.grid(row=i, column=0)

        current_camp_info = tk.Label(view_plan_window, textvariable=tk.StringVar(view_plan_window, value=value))
        current_camp_info.grid(row=i, column=1)

    # Close button
    close_button = tk.Button(view_plan_window, text="Close",command=view_plan_window.destroy)
    close_button.grid(row=len(plan_details) + 1, column=1)
