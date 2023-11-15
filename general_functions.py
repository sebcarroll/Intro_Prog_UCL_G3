import tkinter as tk

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


def check_input_valid(variable, window, message_label, submit_button_row_num, submit_button_column_num):
    '''
    Checks the input field to ensure that empty inputs are rejected.
    Reloads the Tkinter window and displays a message if the input is invalid.

    :param variable: The input that is put into the input field and is being checked.
    :param window: The window in Tkinter that the variable is being inputted into.
    :param message_label: The label widget that will display the message requiring the entry of a non-blank input.
    :return:
    '''
    if variable == None :
        message_label.config(text="Please insert a valid input.")
        window.update()
        message_label.grid(row=submit_button_row_num + 1, column=submit_button_column_num, columnspan=2)
        return False
    elif variable.strip() == '':
        message_label.config(text="Please insert a valid input.")
        window.update()
        message_label.grid(row=submit_button_row_num + 1, column=submit_button_column_num, columnspan=2)
    else:
        message_label.config(text="")
        message_label.grid(row=submit_button_row_num + 1, column=submit_button_column_num, columnspan=2)
        return True