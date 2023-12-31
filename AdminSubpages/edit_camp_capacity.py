import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd

class taken_ID(Exception):
    pass
class none_selected(Exception):
    pass
def edit_camp_details(window, back_button_to_admin_main):
    try:
        for i in window.winfo_children():
            i.grid_forget()
        for i in range(9):
            window.grid_columnconfigure(i, weight=1)
        t_edit_campframe = tk.Frame(window)
        t_edit_campframe.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
        for i in range(9):
            t_edit_campframe.grid_columnconfigure(i, weight=1)
        for i in range(9):
            t_edit_campframe.grid_rowconfigure(i, weight=1)

        # Access the Camp_ID's
        crisis_df = pd.read_csv("crisis_events.csv", header=0)
        crisis_df = crisis_df.fillna(0)
        camp_ID_choices = crisis_df.iloc[:, 0]

        t_select_camp_title = tk.Label(t_edit_campframe, text='Select camp ID', font=('TKDefault', 25), fg='white')
        t_select_camp_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
        t_select_camp_title.configure(background="grey")

        camp_ID_listbox = tk.Listbox(t_edit_campframe, selectmode=tk.SINGLE)
        for camp_id in camp_ID_choices:
            camp_ID_listbox.insert(tk.END, camp_id)
        camp_ID_listbox.grid(row=1, column=4, padx=5, pady=5)


        # Button Frame:
        btn_frame = tk.Frame(t_edit_campframe)
        btn_frame.grid(row=2, column=4, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # BUTTONS:
        # Save changes button, need to add this to a dictionary.
        t_save_changes = tk.Button(btn_frame, text='Add/Remove Refugees', command=lambda: edit_refugee_no(crisis_df, camp_ID_listbox.get(tk.ACTIVE)))
        t_save_changes.grid(row=0, column=1, padx=5, pady=10)

        # Back button
        t_back_button = tk.Button(btn_frame, text='Back to Home', command=back_button_to_admin_main)
        t_back_button.grid(row=0, column=0, padx=5, pady=10)

        change_camp_ID_button = tk.Button(btn_frame, text='Change camp ID', command=lambda: edit_camp_id(crisis_df, camp_ID_listbox.get(tk.ACTIVE), camp_ID_listbox))
        change_camp_ID_button.grid(row=0, column=2, padx=5, pady=10)

    except (ValueError, TypeError):
        tk.messagebox.showwarning(message="Please enter an integer value")
    except taken_ID:
        tk.messagebox.showwarning(message="ID already exists, Please choose a different ID")
    except FileNotFoundError:
        messagebox.showwarning("No data found",
                               "There is a problem accessing the database\n\nThe file may be missing or corrupted")
        back_button_to_admin_main()

def edit_refugee_no(df, selected_camp_id):
    try:
        if selected_camp_id:
            current_capacity = df.loc[df["Camp ID"] == selected_camp_id, 'Capacity'].values[0]
            new_capacity = simpledialog.askinteger("Add/Remove refugees", f"Current total Capacity for Camp ID {selected_camp_id}: {current_capacity}"
                                                                          f"\nHow many refugees would you like to add/remove?", initialvalue=1)


            if isinstance(new_capacity, int):
                # Update the df with the new value
                df.loc[df["Camp ID"] == selected_camp_id, 'Capacity'] += new_capacity
                df.to_csv('crisis_events.csv', index=False)

            elif new_capacity is None:
                messagebox.showinfo("Operation Cancelled", "No changes have been made.")
                return

            else:
                raise ValueError("An integer value was not provided.")
        else:
            raise none_selected
    except none_selected:
        messagebox.showwarning(title="Camp ID not selected", message="Please select a camp ID")


def edit_camp_id(df, selected_camp_id, listbox):
    try:
        if selected_camp_id:
            new_id = simpledialog.askstring("Change camp ID",
                                            "Enter new camp ID - using only numbers (5 characters ONLY)")

            if new_id is None:
                messagebox.showinfo("Operation Cancelled", "No changes have been made.")
                return
            elif not new_id.isnumeric() or len(new_id) != 5:
                raise ValueError("Please enter a valid ID: a numeric value of 5 characters length.")

            if new_id in df['Camp ID'].values:
                raise taken_ID("ID is already taken by another camp.")

            # Update the camp ID in the df
            df['Camp ID'] = df['Camp ID'].astype(str)
            df.loc[df['Camp ID'] == selected_camp_id, 'Camp ID'] = new_id
            df.to_csv('crisis_events.csv', index=False)

            listbox.delete(0, tk.END)
            for camp_id in df['Camp ID']:
                listbox.insert(tk.END, camp_id)

        else:
            raise none_selected("No camp ID selected.")

    except taken_ID as e:
        messagebox.showwarning("Error", str(e))
    except ValueError as e:
        messagebox.showwarning("Invalid ID", str(e))
    except none_selected as e:
        messagebox.showwarning("Camp ID not selected", str(e))