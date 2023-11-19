import tkinter as tk
from tkinter import ttk, Listbox
import pickle

all_camp_data = {}

root = tk.Tk()
window = root
root.geometry('750x600')
resource_allocation_variables = {}
message_label = tk.Label(window, text="")
submit_button_row = 8
submit_button_column = 0
submit_column_span = 2
def turn_data_into_valid_form(camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry, no_refugees_entry, food_amount_refugee_listbox, medicine_amount_refugee_listbox, estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options):

        camp_id = get_selected_listbox_value(None, camp_id_listbox, camp_ids)
        no_weeks_aid = no_weeks_aid_entry.get()
        total_food_supplied = total_food_supplied_entry.get()
        total_medicine_supplied = total_medicine_supplied_entry.get()
        no_refugees = no_refugees_entry.get()  # Will need to come from the volunteer.
        week_food_per_refugee = get_selected_listbox_value(None, food_amount_refugee_listbox, food_amount_refugee)
        week_medicine_per_refugee = get_selected_listbox_value(None, medicine_amount_refugee_listbox,
                                                               medicine_amount_refugee)
        delivery_time_weeks = get_selected_listbox_value(None, estimated_delivery_time_listbox,
                                                         estimated_delivery_time_options)

        if not check_input_valid(camp_id):
            message_label.config(text="Invalid camp ID.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(f"Not valid {camp_id}")

        if not check_input_valid(no_weeks_aid) and not check_is_numeric(no_weeks_aid):
            message_label.config(text="Invalid Number of Weeks given.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(f"Not valid {no_weeks_aid}")


        if not check_input_valid(total_food_supplied) and not check_is_numeric(total_food_supplied):
            message_label.config(text="Invalid Food Total given.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(f" Not valid {total_food_supplied}")

        if not check_input_valid(total_medicine_supplied) and not check_is_numeric(total_medicine_supplied):
            message_label.config(text="Invalid Medicine Total given.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(total_medicine_supplied)

        if not check_input_valid(no_refugees) and not check_is_numeric(no_refugees):
            message_label.config(text="Invalid Number of Refugees given.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(no_refugees)

        if not check_input_valid(week_food_per_refugee) and not check_is_numeric(week_food_per_refugee):
            message_label.config(text="Invalid refugee weekly food allocation given.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(week_food_per_refugee)

        if not check_input_valid(week_medicine_per_refugee) and not check_is_numeric(week_medicine_per_refugee):
            message_label.config(text="Invalid refugee weekly medicine allocation given.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(week_medicine_per_refugee)

        if not check_input_valid(delivery_time_weeks) and not check_is_numeric(delivery_time_weeks):
            message_label.config(text="Invalid estimated delivery time given.")
            message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                               sticky='W')
            print(delivery_time_weeks)
        return camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied, no_refugees, week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks


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

def check_input_valid(variable):
    '''
    Checks the input field to ensure that empty inputs are rejected.
    Reloads the Tkinter window and displays a message if the input is invalid.

    :param variable: The input that is put into the input field and is being checked.
    :return: True or False
    '''

    if variable is None or variable == "":
         return False
    else:
        return True

def get_selected_listbox_value(event, listbox, list):
    '''
    Returns the selected value within a listbox so that the selected value can be saved as a variable for further use. If no input provided, it will use the first option given in the list of options as a default.
    :param listbox: The listbox that the value to be saved is coming from
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

def check_is_numeric(variable):
    try:
        float(variable)
        return float(variable) > 0
    except ValueError:
        return False
def on_confirm_action(camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied, no_refugees,
                      week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks):
    turn_data_into_valid_form(camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry, no_refugees_entry, food_amount_refugee_listbox, medicine_amount_refugee_listbox, estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options)
    create_resource_allocation_dict(camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied,no_refugees, week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks)
    save_to_all_camp_data(camp_id, resource_allocation_variables)
    print(resource_allocation_variables)
    print("Values Submitted and Saved")


def confirmation_before_submission(message_to_be_displayed, callback):
    window = tk.Toplevel()
    label = tk.Label(window, text=message_to_be_displayed)
    label.pack(padx=20, pady=10)

    def yes_confirmed():
        window.destroy()
        callback()
        return True

    def no_confirmed():
        window.destroy()
        return False

    confirm_button = tk.Button(window, text="Confirm", command=yes_confirmed)
    confirm_button.pack(side=tk.LEFT, padx=10, pady=10)

    go_back_button = tk.Button(window, text="Go Back", command=no_confirmed)
    go_back_button.pack(side=tk.RIGHT, padx=10, pady=10)

    window.grab_set()
    window.wait_window()


def on_confirm_action(camp_id, no_weeks_aid, total_food_supplied,
                      total_medicine_supplied, no_refugees,
                      week_food_per_refugee, week_medicine_per_refugee,
                      delivery_time_weeks):
    turn_data_into_valid_form(camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry,
                              total_medicine_supplied_entry, no_refugees_entry, food_amount_refugee_listbox,
                              medicine_amount_refugee_listbox, estimated_delivery_time_listbox, camp_ids,
                              food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options)
    print("Data Validated in on_confirm_action.")
    new_resource_allocation_variables = create_resource_allocation_dict(camp_id, no_weeks_aid, total_food_supplied,
                                                                        total_medicine_supplied, no_refugees,
                                                                        week_food_per_refugee,
                                                                        week_medicine_per_refugee, delivery_time_weeks)

    print("resource_allocation_dict function run.")
    save_to_all_camp_data(camp_id, new_resource_allocation_variables)
    print(all_camp_data[f"camp_{camp_id}_data"])
    print("Values Submitted and Saved")


def resource_allocation(camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry,
                        no_refugees_entry, food_amount_refugee_listbox, medicine_amount_refugee_listbox,
                        estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee,
                        estimated_delivery_time_options):
    '''
    This function enables the administrator to allocate resources to a camp and will notify the administrator
    if the resources provided to the camp are not adequate to cover the total period in which aid is provided.

    '''
    try:
        print("Resource allocation function entered into.")

        (camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied, no_refugees,
         week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks) = turn_data_into_valid_form(camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry,no_refugees_entry, food_amount_refugee_listbox, medicine_amount_refugee_listbox, estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options)

        print("Data Converted.")

        total_food_supplied_float = float(total_food_supplied)
        total_medicine_supplied_float = float(total_medicine_supplied)
        no_refugees_int = int(no_refugees)
        week_food_per_refugee_float = float(week_food_per_refugee)
        week_medicine_per_refugee_float = float(week_medicine_per_refugee)
        no_weeks_aid_float = float(no_weeks_aid)
        print("Data for if statements now in float/int form.")
        weeks_of_food_supply = total_food_supplied_float / (no_refugees_int * week_food_per_refugee_float)
        additional_resources_message = ""
        if weeks_of_food_supply < no_weeks_aid_float:
            additional_food_needed = (no_weeks_aid_float - weeks_of_food_supply) * week_food_per_refugee_float * no_refugees_int
            additional_resources_message += f"{additional_food_needed} additional units of food needed at camp {camp_id} to cover the aid duration period.\n"

        weeks_of_medicine_supply = float(total_medicine_supplied_float) / (no_refugees_int * week_medicine_per_refugee_float)
        if weeks_of_medicine_supply < no_weeks_aid_float:
            additional_medicine_needed = (no_weeks_aid_float - weeks_of_medicine_supply) * week_medicine_per_refugee_float * no_refugees_int
            additional_resources_message += f"{additional_medicine_needed} additional units of medicine needed at camp {camp_id} to cover the aid duration period.\n"

        if additional_resources_message:
            print("Running Confirmation before submission")
            confirmation_before_submission(additional_resources_message, lambda: on_confirm_action(camp_id, no_weeks_aid, total_food_supplied,
                                                             total_medicine_supplied, no_refugees,
                                                             week_food_per_refugee, week_medicine_per_refugee,
                                                             delivery_time_weeks))
        else:
            ("Running on_confirm_action, no issues reported in terms of supply given versus aid.")
            on_confirm_action(camp_id, no_weeks_aid, total_food_supplied,
                      total_medicine_supplied, no_refugees,
                      week_food_per_refugee, week_medicine_per_refugee,
                      delivery_time_weeks)
    except Exception as e:
        print(f"An error occurred: {e}")


def create_resource_allocation_dict(camp_id, no_weeks_aid, total_food_supplied, total_medicine_supplied, no_refugees,
                                    week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks):
    resource_allocation_variables = {
        'camp_id': camp_id,
        'no_weeks_aid': no_weeks_aid,
        'total_food_supplied': total_food_supplied,
        'total_medicine_supplied': total_medicine_supplied,
        'no_refugees': no_refugees,
        'week_food_per_refugee': week_food_per_refugee,
        'week_medicine_per_refugee': week_medicine_per_refugee,
        'delivery_time_weeks': delivery_time_weeks
    }
    return resource_allocation_variables


def save_to_all_camp_data(camp_id, resource_allocation_variables):
    unique_name = f"camp_{camp_id}_data"
    all_camp_data[unique_name] = resource_allocation_variables

    with open(f'{camp_id}_resources.pkl', 'wb') as file:
        pickle.dump(resource_allocation_variables, file)
    print(f"Pickle created for {camp_id} resources.")

#Comes from list of IDs created by admin in camp creation
camp_ids = ["Camp_1", "Camp_2", "Camp_3", "Camp_4"]
camp_id_listbox: Listbox
camp_id_listbox, camp_id_scrollbar = create_listbox_with_label(root, "Camp ID:", 0, 0, camp_ids)

tk.Label(root, text="Number of Weeks of Aid:").grid(row=1, column=0)
no_weeks_aid_entry = tk.Entry(root)
no_weeks_aid_entry.grid(row=1, column=1)

tk.Label(root, text="Total Food Supplied to Camp:").grid(row=2, column=0)
total_food_supplied_entry = tk.Entry(root)
total_food_supplied_entry.grid(row=2, column=1)

tk.Label(root, text="Total Medicine Supplied to Camp:").grid(row=3, column=0)
total_medicine_supplied_entry = tk.Entry(root)
total_medicine_supplied_entry.grid(row=3, column=1)

#This will eventually come from the number of refugees stored with the camp_id
tk.Label(root, text="Number of Refugees:").grid(row=4, column=0)
no_refugees_entry = tk.Entry(root)
no_refugees_entry.grid(row=4, column=1)

food_amount_refugee = [7, 14, 21, 28]
food_amount_refugee_listbox, food_amount_refugee_scrollbar = create_listbox_with_label(root, "Number of Weekly Meals Provided per Refugee: ", 5, 0, food_amount_refugee)

medicine_amount_refugee = [1, 2, 3, 4, 5, 6, 7]
medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(root, "Number of Health Supplies Provided per Refugee Weekly: ", 6, 0, medicine_amount_refugee)

estimated_delivery_time_options = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
estimated_delivery_time_listbox, estimated_delivery_time_scrollbar = create_listbox_with_label(root, "Estimated Resource Delivery Time (weeks): ", 7, 0, estimated_delivery_time_options)

submit_button = ttk.Button(root, text="Submit", command=lambda: resource_allocation(camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry, no_refugees_entry, food_amount_refugee_listbox, medicine_amount_refugee_listbox, estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options))

submit_button.grid(row=8, column=0, columnspan=2)

root.mainloop()