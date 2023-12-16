import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd

class taken_ID(Exception):
    pass
class none_selected(Exception):
    pass
def edit_camp_details(window, y_camp_info, camp_id, back_button_to_volunteer_main):
    try:
        #print(camp_id)
        '''for i in window.winfo_children():
            i.grid_forget()

        t_edit_campframe = tk.Frame(window)
        t_edit_campframe.grid()'''

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

        t_select_camp_title = tk.Label(t_edit_campframe, text='Select camp ID', font=('TKDefault', 25), fg='white')
        # t_select_camp_title.grid(row=0, column=1)
        t_select_camp_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
        t_select_camp_title.configure(background="grey")

        camp_ID_listbox = tk.Listbox(t_edit_campframe, selectmode=tk.SINGLE)
        # camp_ID_listbox.grid(row=1, column=1, padx=5, pady=5)
        camp_ID_listbox.grid(row=1, column=4, padx=5, pady=5)

        # Button Frame:
        btn_frame = tk.Frame(t_edit_campframe)
        btn_frame.grid(row=2, column=4, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # BUTTONS:
        t_save_changes = tk.Button(btn_frame, text='Add/Remove Refugees',
                                   command=lambda: edit_refugee_no(crisis_df, camp_ID_listbox.get(tk.ACTIVE)))
        t_save_changes.grid(row=0, column=2, padx=5, pady=10)

        t_back_button = tk.Button(btn_frame, text='Back to Home', command=back_button_to_volunteer_main)
        t_back_button.grid(row=0, column=1, padx=5, pady=10)

        change_camp_ID_button = tk.Button(btn_frame, text='Change camp ID',
                                          command=lambda: edit_camp_id(crisis_df, camp_ID_listbox.get(tk.ACTIVE),
                                                                       camp_ID_listbox))
        change_camp_ID_button.grid(row=0, column=3, padx=5, pady=10)

        try:
        # Access the Camp_ID's
            crisis_df = pd.read_csv("crisis_events.csv", header=0)
            crisis_df = crisis_df.fillna(0)
            camp_ID_choices = crisis_df['Camp ID'].tolist()
            if camp_id in camp_ID_choices:
                camp_ID_listbox.insert(tk.END, camp_id)
            else:
                camp_ID_listbox.insert(tk.END, "No camp assigned")


        except FileNotFoundError:
            camp_ID_choices = []
            tk.messagebox.showwarning("No data found",
                                      "There is a problem accessing the database\n\nThe file may be missing or corrupted")
            crisis_df = None



        '''# Button Frame:
        btn_frame = tk.Frame(t_edit_campframe)
        btn_frame.grid(row=2, column=4, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # BUTTONS:
        t_save_changes = tk.Button(btn_frame, text='Add/Remove Refugees', command=lambda: edit_refugee_no(crisis_df, camp_ID_listbox.get(tk.ACTIVE)))
        t_save_changes.grid(row=0, column=2, padx=5, pady=10)

        t_back_button = tk.Button(btn_frame, text='Back to Home', command=back_button_to_volunteer_main)
        t_back_button.grid(row=0, column=1, padx=5, pady=10)

        change_camp_ID_button = tk.Button(btn_frame, text='Change camp ID', command=lambda: edit_camp_id(crisis_df, camp_ID_listbox.get(tk.ACTIVE), camp_ID_listbox))
        change_camp_ID_button.grid(row=0, column=3, padx=5, pady=10)'''

    except (ValueError, TypeError):
        tk.messagebox.showwarning(message="Please enter an integer value")
    except taken_ID:
        tk.messagebox.showwarning(message="ID already exists, Please choose a different ID")



def edit_refugee_no(df, selected_camp_id):
    try:
        # Convert selected_camp_id to string if it's not
        selected_camp_id_str = str(selected_camp_id)

        if selected_camp_id_str and selected_camp_id_str.isdigit():
            # Find the current capacity; if not found, default to 0
            current_capacity = df.loc[df["Camp ID"] == int(selected_camp_id_str), 'Capacity'].values
            current_capacity = current_capacity[0] if len(current_capacity) > 0 else 0

            new_capacity = simpledialog.askinteger("Add/Remove refugees",
                                                   f"Current total Refugees for Camp ID {selected_camp_id_str}: {current_capacity}"
                                                   f"\nHow many refugees would you like to add/remove?",
                                                   initialvalue=0)

            if isinstance(new_capacity, int):
                # Update the DataFrame with the new value
                df.loc[df["Camp ID"] == int(selected_camp_id_str), 'Capacity'] += new_capacity
                df.to_csv('crisis_events.csv', index=False)
            else:
                raise ValueError
        else:
            raise none_selected
    except none_selected:
        messagebox.showwarning(title="Camp ID not selected", message="Please select a camp ID")
    except ValueError:
        messagebox.showwarning(title="Invalid Entry", message="Please enter a valid number")


def edit_camp_id(df, selected_camp_id, listbox):
    # Convert selected_camp_id to string if it's not
    selected_camp_id_str = str(selected_camp_id)
    try:
        if selected_camp_id_str and selected_camp_id_str.isdigit():
            new_id = simpledialog.askstring("Change camp ID", "Enter new camp ID - using only numbers (5 characters ONLY)")

            if new_id and new_id.isnumeric() and len(new_id) == 5:
                if int(new_id) not in df['Camp ID'].values:
                    df.loc[df['Camp ID'] == int(selected_camp_id_str), 'Camp ID'] = int(new_id)
                    listbox.delete(0, tk.END)
                    listbox.insert(tk.END, new_id)
                    df.to_csv('crisis_events.csv', index=False)

                    # Update Camp ID in other CSV files
                    update_camp_id_in_other_csvs(int(selected_camp_id_str), int(new_id))
                else:
                    raise taken_ID
            else:
                raise ValueError
        else:
            raise none_selected
    except taken_ID:
        messagebox.showwarning("Error", "ID is already taken")
    except ValueError:
        messagebox.showwarning("Invalid ID", "Please enter a valid ID")
    except none_selected:
        messagebox.showwarning("Camp ID not selected", "Please select a camp ID")


def update_camp_id_in_other_csvs(old_id, new_id):
    for filename in ["volunteer_info.csv", "refugee_info.csv"]:
        try:
            df = pd.read_csv(filename)
            if 'Camp ID' in df.columns:
                df['Camp ID'] = df['Camp ID'].replace(old_id, new_id)
                df.to_csv(filename, index=False)
        except Exception as e:
            messagebox.showwarning("Error", f"Error updating {filename}: {e}")


