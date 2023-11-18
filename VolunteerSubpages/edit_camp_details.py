import tkinter as tk
from tkinter import ttk


def edit_camp_details(window, y_camp_info, back_button_to_volunteer_main):
    for i in window.winfo_children():
        i.grid_forget()
    t_edit_campframe = tk.Frame(window)
    t_edit_campframe.grid()

    t_edit_camp_title = tk.Label(t_edit_campframe, text='Edit camp', font=('Arial Bold', 30), pady=30)
    t_edit_camp_title.grid(row=0, column=1)

    # Sub-label
    t_camp_labelframe = tk.LabelFrame(t_edit_campframe)
    t_camp_labelframe.grid(row=1, column=1)

    # Camp ID box and label
    t_camp_ID_label = tk.Label(t_camp_labelframe, text='Camp ID')
    t_camp_ID_label.grid(row=3, column=3)
    t_camp_ID_box = ttk.Combobox(t_camp_labelframe, values=y_camp_info['Syria']['ID'])
    t_camp_ID_box.grid(row=3, column=4, padx=5)
    # Capacity for new refugees box and label
    t_camp_capacity = tk.Label(t_camp_labelframe, text='Capacity for new refugees:')
    # NOTE need to add current number here next to it so Ying add that in with dictionary or however.
    t_camp_capacity.grid(row=4, column=3, padx=5)
    t_camp_campacitybox = ttk.Spinbox(t_camp_labelframe, from_=0, to=1000, style='info.TSpinbox')
    t_camp_campacitybox.grid(row=4, column=4, padx=5)

    # BUTTONS:
    # Save changes button, need to add this to a dictionary.
    t_save_changes = tk.Button(t_edit_campframe, text='Save changes', command='Store in dictionary')
    t_save_changes.grid(row=7, column=1, padx=5, pady=10)
    # Back button
    t_back_button = tk.Button(t_edit_campframe, text='Back to Home',
                                   command=back_button_to_volunteer_main)
    t_back_button.grid(row=7, column=0, padx=5, pady=10)