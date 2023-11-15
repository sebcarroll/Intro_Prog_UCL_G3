import tkinter as tk
from tkinter import ttk
def create_listbox_with_label(widget, text_label, row_num, column_num, list_of_options):
    '''
    Creates a labelled listbox so that only a select number of options are available for input by the user.

    :param widget: The window in which the listbox is to be contained.
    :param text_label: The name of the label that you want the list box to have
    :param row_num: The relative position vertically that you want the list box and label to be displayed in.
    :param column_num: The relative position horizontally that you want the list box and label to be displayed in.
    :param list_of_options: The list containing the options available to the user to be selected.
    :return:
    '''
    tk.Label(widget, text=text_label).grid(row=row_num, column=column_num)

    scrollbar = tk.Scrollbar(widget)
    scrollbar.grid(row=row_num, column=column_num+2, sticky='ns')

    listbox = tk.Listbox(widget, yscrollcommand=scrollbar.set, height=1)
    listbox.grid(row=row_num, column=column_num+1)

    scrollbar.config(command=listbox.yview)

    for item in list_of_options:
        listbox.insert(tk.END, item)

    return listbox, scrollbar
def get_selected_listbox_value(listbox):
    '''
    Returns the selected value within a listbox so that the selected value can be saved as a variable for further use.

    :param listbox: The listbox that the value to be saved is coming from
    :return:
    '''
    selected_indices = listbox.curselection()
    if selected_indices:
        return listbox.get(selected_indices[0])
    return None  # Return None or a default value if no item is selected
