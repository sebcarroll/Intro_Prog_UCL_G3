import tkinter as tk
import pandas as pd

def create_listbox_with_label(widget, text_label, row_num, column_num, list_of_options):
    '''
    Creates a labelled listbox with a scrollbar and binds the selection event to an action.

    :param widget: The window in which the listbox is to be contained.
    :param text_label: The name of the label that you want the list box to have
    :param row_num: The relative position vertically that you want the list box and label to be displayed in.
    :param column_num: The relative position horizontally that you want the list box and label to be displayed in.
    :param list_of_options: The list containing the options available to the user to be selected.
    :return: listbox and scrollbar widgets
    '''
    label = tk.Label(widget, text=text_label)
    label.grid(row=row_num, column=column_num)

    scrollbar = tk.Scrollbar(widget)
    scrollbar.grid(row=row_num, column=column_num+2, sticky='ns')

    listbox = tk.Listbox(widget, yscrollcommand=scrollbar.set, height=1, exportselection=0)
    listbox.grid(row=row_num, column=column_num+1)
    listbox.bind('<<ListboxSelect>>', lambda event: get_selected_listbox_value(event, listbox, list_of_options))

    scrollbar.config(command=listbox.yview)

    for item in list_of_options:
        listbox.insert(tk.END, item)

    return listbox, scrollbar

def get_selected_listbox_value(event, listbox, list):
    '''
    Returns the selected value within a listbox so that the selected value can be saved as a variable for further use. If no input provided, it will use the first option given in the list of options as a default.
    :param event: A variable that is passed to the function when a binding event takes place.
    :param listbox: The listbox that the value to be saved is coming from.
    :param list: The list of options from which the option is selected. If no option selected, then the first option is selected as default
    :return:
    '''
    #print(f"Current listbox selection indices: {listbox.curselection()}")
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_value = listbox.get(selected_indices[0])
        #print(f"Selected value: {selected_value}")
        return selected_value
    else:
        default_value = list[0]
        #print("No selection made. Using the default value.")
        return default_value

def check_input_valid(variable, window, message_label, submit_button_row_num, submit_button_column_num, column_span):
    '''
    Checks the input field to ensure that empty inputs are rejected.
    Reloads the Tkinter window and displays a message if the input is invalid.

    :param variable: The input that is put into the input field and is being checked.
    :param window: The window in Tkinter that the variable is being inputted into.
    :param message_label: The label widget that will display the message requiring the entry of a non-blank input.
    :return:
    '''
    if variable == None:
        message_label.config(text="Please insert a valid input.")
        window.update()
        message_label.grid(row=submit_button_row_num + 1, column=submit_button_column_num, columnspan= column_span)
        return False
    elif variable == "":
        message_label.config(text="Please insert a valid input.")
        window.update()
        message_label.grid(row=submit_button_row_num + 1, column=submit_button_column_num, columnspan=column_span)
        return False
    else:
        message_label.config(text="")
        message_label.grid(row=submit_button_row_num + 1, column=submit_button_column_num, columnspan= column_span)
        return True
        return variable

def check_is_numeric(variable, window, message_label, submit_button_row_num, submit_button_column_num, column_span):
    try:
        float(variable)
        return True
    except ValueError:
        message_label.config(text="Please insert a valid numeric input.")
        window.update()
        message_label.grid(row=submit_button_row_num + 1, column=submit_button_column_num, columnspan=column_span)
        return False


# The following is used in Admin View Summaries for Edit Plan

def validate_data(edited_data, original_data, row_index_in_treeview):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    validated_data = []

    for i, att in enumerate(original_data.columns):
        value = edited_data[i]

        if att == 'Camp ID':
            if value.isdigit() and len(value) == 5:
                validated_data.append(value)
            else:
                validated_data.append(original_data.at[row_index_in_treeview, att])
        elif att == 'Month':
            if value in months:
                validated_data.append(value)
            else:
                validated_data.append(original_data.at[row_index_in_treeview, att])
        elif att == 'Day':
            if value.isdigit() and 1 <= int(value) <= 31:
                validated_data.append(int(value))
            else:
                validated_data.append(original_data.at[row_index_in_treeview, att])
        elif att == 'Year':
            if value.isdigit() and 2023 <= int(value) <= 2030:
                validated_data.append(int(value))
            else:
                validated_data.append(original_data.at[row_index_in_treeview, att])
        # No negative numbers!
        elif att in ['Capacity', 'Duration', 'Meals(T)', 'Medicine(T)', 'Meals/w', 'Medicine/w', 'Delivery Time(d)', 'Refugees']:
            if value.isdigit() and int(value) > 0:
                validated_data.append(value)
            else:
                validated_data.append(original_data.at[row_index_in_treeview, att])
        # Cannot change these regardless of user input
        elif att in ['Status', 'End Date']:
            validated_data.append(original_data.at[row_index_in_treeview, att])
        else:
            validated_data.append(value)

    return validated_data
