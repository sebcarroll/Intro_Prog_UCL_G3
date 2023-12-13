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

        elif att in ['Status', 'End Date']:
            validated_data.append(original_data.at[row_index_in_treeview, att])

        # elif att == 'extra attribute here!':
        #     if value.isdigit() and len(value) == 5:
        #         validated_data.append(value)
        #     else:
        #         validated_data.append(original_data.at[row_index_in_treeview, att])

        else:
            validated_data.append(value)

    return validated_data






# GUI Functions:

import tkinter as tk
import pandas as pd
import csv

# Function to create a pie chart for the status of crises
def create_pie_chart(window, x_position, y_position):
    # Read data from CSV file
    active_count = 0
    inactive_count = 0

    with open('crisis_events.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            status = row['Status']
            if status.lower() == 'active':
                active_count += 1
            elif status.lower() == 'inactive':
                inactive_count += 1

    # Calculate percentage
    total = active_count + inactive_count
    active_percentage = (active_count / total) * 360
    inactive_percentage = (inactive_count / total) * 360

    # Create a pie chart using canvas
    canvas = tk.Canvas(window, width=200, height=200)
    canvas.place(x=x_position, y=y_position)

    # Draw active and inactive slices
    canvas.create_arc(50, 50, 150, 150, start=0, extent=active_percentage, fill='green', outline='white')
    canvas.create_arc(50, 50, 150, 150, start=active_percentage, extent=inactive_percentage, fill='red', outline='white')

    # Add legend
    legend_labels_crisis_status = ['Active Crisis', 'Inactive Crisis']
    legend_colors_crisis_status = ['green', 'red']
    for i, label in enumerate(legend_labels_crisis_status):
        canvas.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=legend_colors_crisis_status[i], outline='white')
        canvas.create_text(40, 20 + i * 20, text=label, anchor=tk.W, fill='white')

# Function to create a pie chart for crisis types
def create_pie_chart_crisis_type(window, x_position, y_position):
    # Read data from CSV file
    crisis_type_counts = {'war': 0, 'environmental': 0, 'supply shortage': 0,
                          'political unrest': 0, 'displacement': 0, 'other': 0}

    with open('crisis_events.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            crisis_type = row['Crisis Type'].lower()
            if crisis_type in crisis_type_counts:
                crisis_type_counts[crisis_type] += 1

    # Calculate percentage
    total = sum(crisis_type_counts.values())
    start_angle = 0

    # Create a pie chart using canvas
    canvas = tk.Canvas(window, width=200, height=200)
    canvas.place(x=x_position, y=y_position)

    # Draw slices of pie chart
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    for i, (crisis_type, count) in enumerate(crisis_type_counts.items()):
        extent = (count / total) * 360
        canvas.create_arc(50, 50, 150, 150, start=start_angle, extent=extent, fill=colors[i], outline='white')
        start_angle += extent

    # Add legend
    canvas_legend = tk.Canvas(window, width=200, height=200)
    canvas_legend.place(x=x_position + 200, y=y_position)  # Adjust legend position as needed
    for i, (crisis_type, color) in enumerate(zip(crisis_type_counts.keys(), colors)):
        canvas_legend.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=color, outline='white')
        canvas_legend.create_text(40, 20 + i * 20, text=crisis_type.title(), anchor=tk.W, fill='white')



# Function to create a map and mark locations based on CSV data
def create_map(window, x_position, y_position):
    print("Creating map...")

    # Read data from CSV file for crisis event locations
    locations = read_location_data_from_csv('crisis_events.csv')
    print("Loaded locations:", locations)

    # Sample coordinates for countries (adjust as needed)
    country_coordinates = {
        'Nigeria': (50, 100),
        'Sudan': (100, 150),
        'South Sudan': (150, 200),
        'Somalia': (50, 250),
        'Yemen': (100, 50),
        'Afghanistan': (150, 100),
        'England': (200, 150),
    }

    # Load the world map image
    try:
        world_map_image = tk.PhotoImage(file='path/to/world_map.png')
        world_map_canvas = tk.Canvas(window, width=400, height=200)
        world_map_canvas.place(x=x_position, y=y_position)

        # Display the world map image on the canvas
        world_map_canvas.create_image(0, 0, anchor=tk.NW, image=world_map_image)

        # Mark the locations on the map
        for location in locations:
            country = location['country']
            if country in country_coordinates:
                x, y = country_coordinates[country]
                world_map_canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')
                world_map_canvas.create_text(x, y - 10, text=country, anchor=tk.CENTER)
    except Exception as e:
        print("Error loading map image:", e)

def read_location_data_from_csv(filename):
    data = pd.read_csv(filename)
    locations = []
    for index, row in data.iterrows():
        country = row['Country']
        if pd.notna(country):
            locations.append({'country': country})
    return locations


# Call the functions with position parameters and import the functions from gf
"""create_pie_chart(root, 100, 400)  # Specify the position
create_pie_chart_crisis_type(root, 400, 400)  # Specify the position
create_map(root, 700, 400)"""