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

        t_edit_campframe = tk.Frame(window)
        t_edit_campframe.grid()

        # Access the Camp_ID's
        crisis_df = pd.read_csv("crisis_events.csv", header=0)
        crisis_df = crisis_df.fillna(0)
        camp_ID_choices = crisis_df.iloc[:, 0]

        t_select_camp_title = tk.Label(t_edit_campframe, text='Select camp ID', font=('Arial Bold', 30), pady=30)
        t_select_camp_title.grid(row=0, column=1)

        camp_ID_listbox = tk.Listbox(t_edit_campframe, selectmode=tk.SINGLE)
        for camp_id in camp_ID_choices:
            camp_ID_listbox.insert(tk.END, camp_id)
        camp_ID_listbox.grid(row=1, column=1, padx=5, pady=5)

        # BUTTONS:
        # Save changes button, need to add this to a dictionary.
        t_save_changes = tk.Button(t_edit_campframe, text='Add/Remove Refugees', command=lambda: edit_refugee_no(crisis_df, camp_ID_listbox.get(tk.ACTIVE)))
        t_save_changes.grid(row=7, column=1, padx=5, pady=10)

        # Back button
        t_back_button = tk.Button(t_edit_campframe, text='Back to Home', command=back_button_to_admin_main)
        t_back_button.grid(row=7, column=0, padx=5, pady=10)

        change_camp_ID_button = tk.Button(t_edit_campframe, text='Change camp ID', command=lambda: edit_camp_id(crisis_df, camp_ID_listbox.get(tk.ACTIVE), camp_ID_listbox))
        change_camp_ID_button.grid(row=7, column=2, padx=5, pady=10)

    except (ValueError, TypeError):
        tk.messagebox.showwarning(message="Please enter an integer value")
    except taken_ID:
        tk.messagebox.showwarning(message="ID already exists, Please choose a different ID")

def edit_refugee_no(df, selected_camp_id):
    try:
        if selected_camp_id:
            current_capacity = df.loc[df["Camp ID"] == selected_camp_id, 'Capacity'].values[0]
            new_capacity = simpledialog.askinteger("Add/Remove refugees", f"Current total Capacity for Camp ID {selected_camp_id}: {current_capacity}"
                                                                          f"\nHow many refugees would you like to add/remove?", initialvalue=1)


            if type(new_capacity) == int:
                # Update the DataFrame with the new value
                df.loc[df["Camp ID"] == selected_camp_id, 'Capacity'] += new_capacity
                df.to_csv('crisis_events.csv', index=False)


            else:
                raise ValueError
        else:
            raise none_selected
    except none_selected:
        messagebox.showwarning(title="Camp ID not selected", message="Please select a camp ID")


def edit_camp_id(df, selected_camp_id, listbox):
    try:
        if selected_camp_id:
            # Ask the user for a new camp ID
            new_id = simpledialog.askstring("Change camp ID", prompt="Enter new camp ID - using only numbers (5 characters ONLY)")

            # Check if the new ID is not empty and is different from the current ID
            if new_id.isnumeric() and len(new_id) != 5:
                # Check if the new ID already exists in the DataFrame
                if new_id not in df['Camp ID'].values:
                    # Update the camp ID in the DataFrame
                    df.loc[df['Camp ID'] == selected_camp_id, 'Camp ID'] = new_id

                    # Convert the 'New Camp ID' column to a list
                    new_camp_ids = df['Camp ID'].tolist()

                    # Clear the listbox and insert the updated camp IDs
                    listbox.delete(0, tk.END)
                    for camp_id in new_camp_ids:
                        listbox.insert(tk.END, camp_id)

                    # Save the DataFrame to the CSV file
                    df.to_csv('crisis_events.csv', index=False)
                else:
                    raise taken_ID
            else:
                raise ValueError

    except taken_ID:
        messagebox.showwarning("Error", "ID is already taken")
    except ValueError:
        messagebox.showwarning("Invalid ID", message="Please enter a valid ID")