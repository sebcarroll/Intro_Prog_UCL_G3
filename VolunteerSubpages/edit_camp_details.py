import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd

def edit_camp_details(window, y_camp_info, back_button_to_volunteer_main):
    try:
        for i in window.winfo_children():
            i.grid_forget()

        t_edit_campframe = tk.Frame(window)
        t_edit_campframe.grid()

        # Access the Camp_ID's
        crisis_df = pd.read_csv("crisis_events.csv", header=0)
        crisis_df.set_index('New Camp ID')
        crisis_df = crisis_df.fillna(0)
        camp_ID_choices = crisis_df.iloc[:, 0]
        print(crisis_df)

        t_select_camp_title = tk.Label(t_edit_campframe, text='Select camp ID', font=('Arial Bold', 30), pady=30)
        t_select_camp_title.grid(row=0, column=15)

        camp_ID_listbox = tk.Listbox(t_edit_campframe, selectmode=tk.SINGLE)
        for camp_id in camp_ID_choices:
            camp_ID_listbox.insert(tk.END, camp_id)
        camp_ID_listbox.grid(row=1, column=15, padx=5, pady=5)

        # BUTTONS:
        # Save changes button, need to add this to a dictionary.
        t_save_changes = tk.Button(t_edit_campframe, text='Select Camp ID', command=lambda: edit_refugee_no(crisis_df, camp_ID_listbox.get(tk.ACTIVE)))
        t_save_changes.grid(row=7, column=1, padx=5, pady=10)

        # Back button
        t_back_button = tk.Button(t_edit_campframe, text='Back to Home', command=back_button_to_volunteer_main)
        t_back_button.grid(row=7, column=0, padx=5, pady=10)

    except ValueError:
        messagebox.showwarning(message="Please enter an integer value")

def edit_refugee_no(df, selected_camp_id):
    if selected_camp_id:
        current_capacity = df.loc[df["New Camp ID"] == selected_camp_id, 'Number of Refugees'].values[0]
        new_capacity = simpledialog.askinteger("Add/Remove refugees", f"Current total Capacity for Camp ID {selected_camp_id}: {current_capacity}"
                                                                      f"\nHow many refugees would you like to add/remove?", initialvalue=1)


        if new_capacity is not None:
            # Update the DataFrame with the new value
            df.loc[df["New Camp ID"] == selected_camp_id, 'Number of Refugees'] += new_capacity
            df.set_index('New Camp ID')
            df.to_csv('crisis_events.csv', index=False)


        else:
            raise ValueError
    else:
        raise ValueError

