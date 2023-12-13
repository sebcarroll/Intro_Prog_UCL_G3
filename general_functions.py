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
    print(f"Current listbox selection indices: {listbox.curselection()}")
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_value = listbox.get(selected_indices[0])
        print(f"Selected value: {selected_value}")
        return selected_value
    else:
        default_value = list[0]
        print("No selection made. Using the default value.")
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


'''def validate_and_convert_data(input_data, original_data, row_index):
    # List of valid months
    valid_months = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']

    validated_data = []

    for i, col_name in enumerate(original_data.columns):
        value = input_data[i]

        if col_name == 'Camp ID':
            validated_data.append(value if value.isdigit() and len(value) == 5 else original_data.at[row_index, 'Camp ID'])

        elif col_name == 'Crisis Type' or col_name == 'Description' or col_name == 'Country':
            validated_data.append(value)

        elif col_name == 'Day':
            validated_data.append(int(value) if value.isdigit() and 1 <= int(value) <= 31 else original_data.at[row_index, 'Day'])

        elif col_name == 'Month':
            validated_data.append(value if value in valid_months else original_data.at[row_index, 'Month'])

        elif col_name == 'Year':
            validated_data.append(int(value) if value.isdigit() and 2023 <= int(value) <= 2030 else original_data.at[row_index, 'Year'])

        elif col_name == 'Status' or col_name == 'End Date':
            validated_data.append(original_data.at[row_index, col_name])  # These fields cannot change

        elif col_name in ['Number of Refugees', 'Crisis Length', 'Total Meals', 'Total Medicine', 'Meals/week', 'Medicine/week', 'Delivery Time (days)', 'Current No. of Refugees']:
            validated_data.append(int(value) if value.isdigit() else original_data.at[row_index, col_name])

        else:
            validated_data.append(value)  # Default case for any other column

    #return validated_data


    casted_values = []
    for i, col_name in enumerate(original_data.columns):
        validated_value = validated_data[i]
        col_type = original_data[col_name].dtype

        if pd.api.types.is_integer_dtype(col_type):
            # Convert to integer if possible
            try:
                casted_value = int(validated_value) if validated_value else original_data.at[row_index, col_name]
            except ValueError:
                casted_value = original_data.at[row_index, col_name]

        elif pd.api.types.is_float_dtype(col_type):
            # Convert to float if possible
            try:
                casted_value = float(validated_value) if validated_value else original_data.at[row_index, col_name]
            except ValueError:
                casted_value = original_data.at[row_index, col_name]

        else:
            # Use the string value as it is for other types
            casted_value = validated_value if validated_value else original_data.at[row_index, col_name]

        casted_values.append(casted_value)

    return casted_values'''

def validate_data(input_data, original_data, row_index):
    valid_months = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']

    validated_data = []
    for i, col_name in enumerate(original_data.columns):
        value = input_data[i]

        # Apply validation rules based on column name
        if col_name == 'Camp ID':
            value = value if value.isdigit() and len(value) == 5 else original_data.at[row_index, col_name]
        elif col_name == 'Month':
            value = value if value in valid_months else original_data.at[row_index, col_name]
        elif col_name == 'Day':
            value = value if value.isdigit() and 1 <= int(value) <= 31 else original_data.at[row_index, col_name]
        elif col_name == 'Year':
            value = value if value.isdigit() and 2023 <= int(value) <= 2030 else original_data.at[row_index, col_name]
        elif col_name in ['Status', 'End Date']:
            value = original_data.at[row_index, col_name]
        else:
            value = value

        validated_data.append(value)
    return validated_data

def cast_data(validated_data, original_data):
    casted_values = []
    for i, col_name in enumerate(original_data.columns):
        value = validated_data[i]
        col_type = original_data[col_name].dtype

        if pd.api.types.is_integer_dtype(col_type):
            try:
                # Attempt to cast to integer, if possible
                value = int(value)
            except (ValueError, TypeError):
                # If casting fails, keep the validated value
                pass
        elif pd.api.types.is_float_dtype(col_type):
            try:
                # Attempt to cast to float, if possible
                value = float(value)
            except (ValueError, TypeError):
                # If casting fails, keep the validated value
                pass

        casted_values.append(value)
    return casted_values