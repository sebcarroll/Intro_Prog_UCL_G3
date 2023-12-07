import tkinter as tk
from tkinter import ttk, Listbox
import csv
import general_functions as gf
from resource_allocation_csv_creation import update_crisis_events

class AdminResourceAllocation:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main
        self.resource_allocation_variables = []
        self.all_camp_data = {}
        self.camp_ids_from_csv = []
        self.camp_ids = [] # CGH: Seb I put this in for the case when there is no file found
        try:
            with open('crisis_events.csv', 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    self.camp_ids_from_csv.append(row[0])
            self.camp_ids = self.camp_ids_from_csv
        except FileNotFoundError:
            print("Error: 'crisis_events.csv' file not found.")

    def create_gui_resource_allocation(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        # If you want some formatting in a separate frame:
        resource_frame = tk.Frame(self.window)
        resource_frame.grid()
        camp_id_listbox: Listbox
        self.camp_id_listbox, self.camp_id_scrollbar = create_listbox_with_label(self.window, "Camp ID:", 0, 0, self.camp_ids)

        tk.Label(self.window, text="Number of Weeks of Aid:").grid(row=1, column=0)
        no_weeks_aid_entry = tk.Entry(self.window)
        no_weeks_aid_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Total Food Supplied to Camp:").grid(row=2, column=0)
        total_food_supplied_entry = tk.Entry(self.window)
        total_food_supplied_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Total Medicine Supplied to Camp:").grid(row=3, column=0)
        total_medicine_supplied_entry = tk.Entry(self.window)
        total_medicine_supplied_entry.grid(row=3, column=1)

        tk.Label(self.window, text="Estimated Number of Refugees at camp:").grid(row=4, column=0)
        number_of_refugees_actual = 0
        with open('refugee_info.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if self.camp_id_listbox == row[1]:
                    number_of_refugees_actual = number_of_refugees_actual + 1
                else:
                    pass
        tk.Label(self.window, text = f"Camp currently has {number_of_refugees_actual} registered refugees.").grid(row=5, column=0)
        no_refugees_entry = tk.Entry(self.window)
        no_refugees_entry.grid(row=4, column=1)

        food_amount_refugee = [7, 14, 21, 28]
        #gf.food_amount_refugee_listbox, gf.food_amount_refugee_scrollbar = create_listbox_with_label(self.window, "Number of Weekly Meals Provided per Refugee: ", 5, 0, food_amount_refugee)
        self.food_amount_refugee_listbox, self.food_amount_refugee_scrollbar = create_listbox_with_label(self.window,"Number of Weekly Meals Provided per Refugee: ",6, 0,food_amount_refugee)
        medicine_amount_refugee = [1, 2, 3, 4, 5, 6, 7]
        medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(self.window, "Number of Health Supplies Provided per Refugee Weekly: ", 7, 0, medicine_amount_refugee)

        estimated_delivery_time_options = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
        #estimated_delivery_time_listbox, estimated_delivery_time_scrollbar = create_listbox_with_label(self.window,"Estimated Resource Delivery Time (weeks): ",7, 0, estimated_delivery_time_options)

        self.estimated_delivery_time_listbox, self.estimated_delivery_time_scrollbar = create_listbox_with_label(self.window, "Estimated Resource Delivery Time (weeks): ", 8, 0, estimated_delivery_time_options)

        submit_button = ttk.Button(self.window, text="Submit", command=lambda: self.resource_allocation(self.camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry, no_refugees_entry, self.food_amount_refugee_listbox, medicine_amount_refugee_listbox, self.estimated_delivery_time_listbox, self.camp_ids, food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options))

        submit_button.grid(row=9, column=0, columnspan=2)

        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=17, column=1, padx=5, pady=10)

    def turn_data_into_valid_form(self, camp_id_listbox,no_refugees_entry, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry,  food_amount_refugee_listbox, medicine_amount_refugee_listbox, estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options):

            '''
            '''
            message_label = tk.Label(self.window, text="")
            submit_button_row = 8
            submit_button_column = 0
            submit_column_span = 2

            camp_id = self.get_selected_listbox_value(None, camp_id_listbox, self.camp_ids)
            no_refugees = no_refugees_entry.get()
            print(f" no_refugees_entry.get(): {no_refugees_entry}, {no_refugees}")
            no_weeks_aid = no_weeks_aid_entry.get()
            print(f"No_weeks_aid_entry.get() value = {no_weeks_aid_entry}, {no_weeks_aid}")
            total_food_supplied = total_food_supplied_entry.get()
            print(f"total_food_supplied_entry.get() = {total_food_supplied_entry}, {total_food_supplied}")
            total_medicine_supplied = total_medicine_supplied_entry.get()
            print(f"total_medicine_supplied_entry.get() value: {total_medicine_supplied_entry}, {total_medicine_supplied} ")
            week_food_per_refugee = self.get_selected_listbox_value(None, food_amount_refugee_listbox, food_amount_refugee)
            week_medicine_per_refugee = self.get_selected_listbox_value(None, medicine_amount_refugee_listbox,
                                                                   medicine_amount_refugee)
            delivery_time_weeks = self.get_selected_listbox_value(None, estimated_delivery_time_listbox,
                                                             estimated_delivery_time_options)

            if self.check_input_valid(camp_id) == False:
                message_label.config(text="Invalid camp ID.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(f"Not valid {camp_id}")

            if self.check_input_valid(no_weeks_aid) == False or self.check_is_numeric(no_weeks_aid) == False:
                message_label.config(text="Invalid Number of Weeks given.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(f"Not valid {no_weeks_aid}")


            if self.check_input_valid(total_food_supplied) == False or self.check_is_numeric(total_food_supplied) == False:
                message_label.config(text="Invalid Food Total given.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(f" Not valid {total_food_supplied}")

            if self.check_input_valid(total_medicine_supplied) == False or self.check_is_numeric(total_medicine_supplied) == False:
                message_label.config(text="Invalid Medicine Total given.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(total_medicine_supplied)

            if self.check_input_valid(no_refugees) == False or self.check_is_numeric(no_refugees) == False:
                message_label.config(text="Invalid Number of Refugees given.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(no_refugees)

            if self.check_input_valid(week_food_per_refugee) == False or self.check_is_numeric(week_food_per_refugee) == False:
                message_label.config(text="Invalid refugee weekly food allocation given.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(week_food_per_refugee)

            if self.check_input_valid(week_medicine_per_refugee) == False or self.check_is_numeric(week_medicine_per_refugee) == False:
                message_label.config(text="Invalid refugee weekly medicine allocation given.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(week_medicine_per_refugee)

            if self.check_input_valid(delivery_time_weeks) == False or self.check_is_numeric(delivery_time_weeks) == False:
                message_label.config(text="Invalid estimated delivery time given.")
                message_label.grid(row=submit_button_row + 1, column=submit_button_column, columnspan=submit_column_span,
                                   sticky='W')
                print(delivery_time_weeks)
            return camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied, week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks

    def check_input_valid(self, variable):
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

    def get_selected_listbox_value(self, event, listbox, list):
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

    def check_is_numeric(self, variable):
        try:
            float(variable)
            return float(variable) > 0
        except ValueError:
            return False

    def on_confirm_action(self, camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks):
        '''
        Upon confirmation of the users choices, this function turns the data into a valid form for saving, saves the values to a dictionary, then saves the data to a larger dictionary as well as to a pickle.
        :param camp_id: The id of the camp that the data is relevant to.
        :param no_weeks_aid: The number of weeks that the resources have been allocated to.
        :param total_food_supplied: The total amount of food supplied to the camp.
        :param total_medicine_supplied: The total amount of medicine supplied to the camp.
        :param no_refugees: The total number of refugees that are housed within the camp.
        :param week_food_per_refugee: The weekly allocation of food provided to each refugee.
        :param week_medicine_per_refugee: The weekly allocation of medicine provided to each refugee.
        :param delivery_time_weeks: The estimated delivery time for the supplies once ordered.
        '''
      # self.turn_data_into_valid_form(camp_id_listbox, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry, no_refugees_entry, food_amount_refugee_listbox, medicine_amount_refugee_listbox, estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee, estimated_delivery_time_options)
        self.create_resource_allocation_list(camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks)
        update_crisis_events(camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks)
        print(self.resource_allocation_variables)
        print("Values Submitted and Saved")


    def confirmation_before_submission(self, message_to_be_displayed, callback):
        '''
        Makes a new branch
        '''
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


    def resource_allocation(self, camp_id_listbox, no_refugees_entry, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry,
                            food_amount_refugee_listbox, medicine_amount_refugee_listbox,
                            estimated_delivery_time_listbox, camp_ids, food_amount_refugee, medicine_amount_refugee,
                            estimated_delivery_time_options):
        '''
        This function enables the administrator to allocate resources to a camp and will notify the administrator
        if the resources provided to the camp are not adequate to cover the total period in which aid is provided.

        '''
        try:
            print("Resource allocation function entered into.")

            (camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks) = self.turn_data_into_valid_form(
                camp_id_listbox, no_refugees_entry, no_weeks_aid_entry,
                total_food_supplied_entry, total_medicine_supplied_entry,
                food_amount_refugee_listbox, medicine_amount_refugee_listbox,
                estimated_delivery_time_listbox, camp_ids, food_amount_refugee,
                medicine_amount_refugee, estimated_delivery_time_options
            )

            print("Data Converted.")
            camp_id_type = type(camp_id)
            print(f"Camp ID variable type: {camp_id_type}")
            no_refugees_int = int(no_refugees)
            print(f"Number of refugees: {no_refugees_int}")
            no_weeks_aid_float = float(no_weeks_aid)
            print(f"Number of weeks of aid being supplied: {no_weeks_aid_float}")
            total_food_supplied_float = float(total_food_supplied)
            print(total_food_supplied_entry)
            print(total_food_supplied)
            print(f"Total food supplied: {total_food_supplied_float}")
            total_medicine_supplied_float = float(total_medicine_supplied)
            print(f"Total medicine supplied: {total_medicine_supplied_float}")
            week_food_per_refugee_float = float(week_food_per_refugee)
            print(f"Weekly food allocation: {week_food_per_refugee_float}")
            week_medicine_per_refugee_float = float(week_medicine_per_refugee)
            print(f"Weekly medicine allocation: {week_medicine_per_refugee_float}")
            print("Data for if statements now in float/int form.")
            weeks_of_food_supply = total_food_supplied_float / (no_refugees_int * week_food_per_refugee_float)
            print(f"Number of weeks of food supply: {weeks_of_food_supply}")
            additional_resources_message = ""
            if weeks_of_food_supply < no_weeks_aid_float:
                additional_food_needed = (no_weeks_aid_float - weeks_of_food_supply) * (week_food_per_refugee_float * no_refugees_int)
                additional_resources_message += f"{additional_food_needed} additional units of food needed at camp {camp_id} to cover the aid duration period.\n"

            weeks_of_medicine_supply = float(total_medicine_supplied_float) / (no_refugees_int * week_medicine_per_refugee_float)
            if weeks_of_medicine_supply < no_weeks_aid_float:
                additional_medicine_needed = (no_weeks_aid_float - weeks_of_medicine_supply) * (week_medicine_per_refugee_float * no_refugees_int)
                additional_resources_message += f"{additional_medicine_needed} additional units of medicine needed at camp {camp_id} to cover the aid duration period.\n"

            if additional_resources_message:
                print("Running Confirmation before submission")
                self.confirmation_before_submission(additional_resources_message, lambda: self.on_confirm_action(camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks))
            else:
                print("Running on_confirm_action, no issues reported in terms of supply given versus aid.")
                self.on_confirm_action(camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks)
        except Exception as e:
            print(f"An error occurred: {e}")


    def create_resource_allocation_list(self, camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks):
        self.resource_allocation_variables = [
            camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
            week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks
        ]
        return self.resource_allocation_variables

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
    listbox.bind('<<ListboxSelect>>', lambda event: gf.get_selected_listbox_value(event, listbox, list_of_options))

    scrollbar.config(command=listbox.yview)

    for item in list_of_options:
        listbox.insert(tk.END, item)

    return listbox, scrollbar

