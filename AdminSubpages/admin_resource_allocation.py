
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import general_functions as gf
from resource_allocation_csv_creation import update_crisis_events
import csv

class AdminResourceAllocation:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main
        self.resource_allocation_variables = []
        self.all_camp_data = {}
        self.camp_ids = [] # CGH: Seb I put this in for the case when there is no file found
        self.number_of_actual_refugees = 0
    def read_crisis_events_csv(self):
        self.camp_ids_from_csv = []
        try:
            with open('crisis_events.csv', 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    if row[7] == "Active":
                        self.camp_ids_from_csv.append(row[0])
        except FileNotFoundError:
            print("Error: 'crisis_events.csv' file not found.")
        self.camp_ids = list(self.camp_ids_from_csv)

    def create_gui_resource_allocation(self, window):
        self.read_crisis_events_csv()
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()

        # Title
        title = tk.Label(self.window, text='Resource Allocation', font=('TkDefault', 35))
        title.grid(row=0, column=0, pady=30)

        # Resource Frame
        resource_frame = tk.Frame(self.window)
        resource_frame.grid(row=1, column=0, padx=5, pady=5)

        # Creating list of CAMP IDs
        camp_ID_label = tk.Label(resource_frame, text='Camp ID: ')
        camp_ID_label.grid(row=1, column=0, padx=5, pady=5)
        self.camp_ID_box = ttk.Combobox(resource_frame, values= self.camp_ids)
        self.camp_ID_box.grid(row=1, column=1, padx=5, pady=5)
        self.camp_ID_box.bind('<<ComboboxSelected>>', self.update_number_of_refugees)

        # self.camp_id_listbox, self.camp_id_scrollbar = create_listbox_with_label(resource_frame, "Camp ID:", 1, 0,
        #                                                                              self.camp_ids)
        # self.camp_id_listbox.grid(padx=5, pady=5)

        # Label for displaying number of refugees
        refugee_label = tk.Label(resource_frame, text="Current No. Refugees at camp: ")
        refugee_label.grid(row=2, column=0, padx=5, pady=5)
        self.refugee_count = tk.Label(resource_frame, text="")
        self.refugee_count.grid(row=2, column=1, padx=5, pady=5)

        # Bind the event handler to the listbox
        # self.camp_id_listbox.bind('<<ListboxSelect>>', update_number_of_refugees)

        tk.Label(resource_frame, text='Camp Estimated Refugee Carrying Capacity: ').grid(row=3, column=0, padx=5, pady=5)
        no_refugees_entry = tk.Entry(resource_frame)
        no_refugees_entry.grid(row=3, column=1)

        tk.Label(resource_frame, text="Number of Weeks of Aid: ").grid(row=4, column=0, padx=5, pady=5)
        self.no_weeks_aid_var = tk.StringVar()
        self.no_weeks_aid_entry = tk.Entry(resource_frame, textvariable=self.no_weeks_aid_var)
        self.no_weeks_aid_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(resource_frame, text="Total Food Supplied to Camp: ").grid(row=5, column=0, padx=5, pady=5)
        total_food_supplied_entry = tk.Entry(resource_frame)
        total_food_supplied_entry.grid(row=5, column=1, padx=5, pady=5)

        recommended_food_label = tk.Label(resource_frame, text="Minimum Food Amount Required (given current no. of refugees): ")
        recommended_food_label.grid(row=6, column=0, padx=5, pady=5)
        self.recommended_food_count = tk.Label(resource_frame, text="")
        self.recommended_food_count.grid(row=6, column=1, padx=5, pady=5)


        tk.Label(resource_frame, text="Total Medicine Supplied to Camp: ").grid(row=7, column=0, padx=5, pady=5)
        total_medicine_supplied_entry = tk.Entry(resource_frame)
        total_medicine_supplied_entry.grid(row=7, column=1, padx=5, pady=5)

        recommended_medicine_label = tk.Label(resource_frame, text="Minimum Medicine Required (given current no. of refugees): ")
        recommended_medicine_label.grid(row=8, column=0, padx=5, pady=5)
        self.recommended_medicine_count = tk.Label(resource_frame, text="")
        self.recommended_medicine_count.grid(row=8, column=1, padx=5, pady=5)

        # gf.food_amount_refugee_listbox, gf.food_amount_refugee_scrollbar = create_listbox_with_label(self.window, "Number of Weekly Meals Provided per Refugee: ", 5, 0, food_amount_refugee)
        # self.food_amount_refugee_listbox, self.food_amount_refugee_scrollbar = create_listbox_with_label(resource_frame,
        # Food label and spinbox
        food_label = tk.Label(resource_frame, text='Number of Weekly Meals Provided per Refugee: ')
        food_label.grid(row=9, column=0, padx=5, pady=5)
        self.food_box = tk.Spinbox(resource_frame, from_=0, to=28, increment=7)
        self.food_box.grid(row=9, column=1, padx=5, pady=5)


       # medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(resource_frame,

                                                                                                  #    "Number of Health Supplies Provided per Refugee Weekly: ",                                                                                       #    8,                                                                                         #   medicine_amount_refugee)
        medicine_label = tk.Label(resource_frame, text='Number of Health Supplies per Refugee per Week: ')
        medicine_label.grid(row=10, column=0, padx=5, pady=5)
        self.medicine_box = tk.Spinbox(resource_frame, from_=0, to=7)
        self.medicine_box.grid(row=10, column=1, padx=5, pady=5)
       # estimated_delivery_time_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        # estimated_delivery_time_listbox, estimated_delivery_time_scrollbar = create_listbox_with_label(self.window,"Estimated Resource Delivery Time (weeks): ",7, 0, estimated_delivery_time_options)

        # self.estimated_delivery_time_listbox, self.estimated_delivery_time_scrollbar = create_listbox_with_label(
        #     resource_frame, "Estimated Resource Delivery Time (days): ", 9, 0, estimated_delivery_time_options)

        estimated_delivery_label = tk.Label(resource_frame, text='Estimated Resource Delivery Time (days): ')
        estimated_delivery_label.grid(row=11, column=0, padx=5, pady=5)
        self.estimated_delivery_box = tk.Spinbox(resource_frame, from_=0, to=14)
        self.estimated_delivery_box.grid(row=11, column=1, padx=5, pady=5)
        submit_button = ttk.Button(resource_frame, text="Submit",
                                   command=lambda: self.resource_allocation(self.camp_ID_box, no_refugees_entry,
                                                                            self.no_weeks_aid_entry,
                                                                            total_food_supplied_entry,
                                                                            total_medicine_supplied_entry,
                                                                            self.food_box,
                                                                            self.medicine_box,
                                                                            self.estimated_delivery_box,
                                                                            self.camp_ids))

        submit_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=13, column=0, padx=5, pady=10)
        self.setup_callback()
        # Event handler function to update number of refugees
    def update_number_of_refugees(self, event):
        selected_camp_id = self.camp_ID_box.get()
        print(selected_camp_id)
        try:
            with open('refugee_info.csv', 'r') as file:
                    csv_reader = csv.reader(file)
                    next(csv_reader)
                    for row in csv_reader:
                        if int(selected_camp_id) == int(float(row[1])):
                            self.number_of_actual_refugees = self.number_of_actual_refugees + 1
        except FileNotFoundError:
            print("Error: 'refugee_info.csv' file not found.")
        self.refugee_count.config(text=str(self.number_of_actual_refugees))
        return self.number_of_actual_refugees

        # Bind the event handler to the listbox
        # self.camp_id_listbox.bind('<<ListboxSelect>>', update_number_of_refugees)

    def setup_callback(self):
        self.no_weeks_aid_var.trace("w", self.on_weeks_of_aid_change)

    def on_weeks_of_aid_change(self, *args):
        self.give_minimum_recommended_amount_based_on_current_refugees()

    def give_minimum_recommended_amount_based_on_current_refugees(self):
        print("function_running")
        no_weeks_aid = self.no_weeks_aid_var.get()
        camp_ID = self.camp_ID_box.get()
        print(f"Number of weeks of aid: {no_weeks_aid}")
        if no_weeks_aid.isdigit():
            no_weeks_aid = int(no_weeks_aid)
            self.minimum_amount_of_food = self.number_of_actual_refugees * 7 * no_weeks_aid
            self.minimum_amount_of_medicine = self.number_of_actual_refugees * 1 * no_weeks_aid
            print(f"Calculated food: {self.minimum_amount_of_food}, medicine: {self.minimum_amount_of_medicine}")
            self.recommended_food_count.config(text=str(self.minimum_amount_of_food))
            self.recommended_medicine_count.config(text=str(self.minimum_amount_of_medicine))
        else:
            print("Invalid input for weeks of aid.")

    def turn_data_into_valid_form(self, camp_ID_box, no_refugees_entry, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry,  food_box, medicine_box, estimated_delivery_box, camp_ids):
            '''
            '''
            message_label = tk.Label(self.window, text="")
            submit_button_row = 9
            submit_button_column = 0
            submit_column_span = 2

            camp_id = self.camp_ID_box.get()
            no_refugees = no_refugees_entry.get()
            no_weeks_aid = self.no_weeks_aid_entry.get()
            total_food_supplied = total_food_supplied_entry.get()
            total_medicine_supplied = total_medicine_supplied_entry.get()
            week_food_per_refugee = self.food_box.get()
            week_medicine_per_refugee = self.medicine_box.get()
            delivery_time_weeks = self.estimated_delivery_box.get()

            if self.check_input_valid(camp_id) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Please select a valid Camp ID.')
                print(f"Not valid {camp_id}")

            if self.check_input_valid(no_refugees) == False or self.check_is_numeric(no_refugees) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Invalid camp carrying capacity estimate given.')
                print(no_refugees)

            if self.check_input_valid(no_weeks_aid) == False or self.check_is_numeric(no_weeks_aid) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Invalid estimated time length for aid given.')
                print(f"Not valid {no_weeks_aid}")


            if self.check_input_valid(total_food_supplied) == False or self.check_is_numeric(total_food_supplied) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Invalid Food Total Given.')
                print(f" Not valid {total_food_supplied}")

            if self.check_input_valid(total_medicine_supplied) == False or self.check_is_numeric(total_medicine_supplied) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Invalid Medicine Total Given')
                print(total_medicine_supplied)

            if self.check_input_valid(week_food_per_refugee) == False or self.check_is_numeric(week_food_per_refugee) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Invalid weekly food allocation given.')
                print(week_food_per_refugee)

            if self.check_input_valid(week_medicine_per_refugee) == False or self.check_is_numeric(week_medicine_per_refugee) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Invalid weekly medicine allocation given.')
                print(week_medicine_per_refugee)

            if self.check_input_valid(delivery_time_weeks) == False or self.check_is_numeric(delivery_time_weeks) == False:
                tk.messagebox.showinfo(title='Invalid Entry', message='Invalid estimated delivery time given.')
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
        tk.messagebox.showinfo(title='Details saved', message='Details have been saved')


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


    def resource_allocation(self, camp_ID_box, no_refugees_entry, no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry,
                             food_box, medicine_box,
                            estimated_delivery_box, camp_ids):
        '''
        This function enables the administrator to allocate resources to a camp and will notify the administrator
        if the resources provided to the camp are not adequate to cover the total period in which aid is provided.

        '''
        try:
            print("Resource allocation function entered into.")

            (camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks) = self.turn_data_into_valid_form(self.camp_ID_box, no_refugees_entry, self.no_weeks_aid_entry, total_food_supplied_entry, total_medicine_supplied_entry, self.food_box, self.medicine_box, self.estimated_delivery_box, camp_ids)
            print("Data Converted.")

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
                additional_resources_message += f"Recommended: {additional_food_needed} additional units of food needed at camp {camp_id} to cover the aid duration period.\n"

            weeks_of_medicine_supply = float(total_medicine_supplied_float) / (no_refugees_int * week_medicine_per_refugee_float)
            if weeks_of_medicine_supply < no_weeks_aid_float:
                additional_medicine_needed = (no_weeks_aid_float - weeks_of_medicine_supply) * (week_medicine_per_refugee_float * no_refugees_int)
                additional_resources_message += f" Recommended: {additional_medicine_needed} additional units of medicine needed at camp {camp_id} to cover the aid duration period.\n"

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
    label.grid(row=row_num, column=column_num, padx=5, pady=5)

    scrollbar = tk.Scrollbar(widget)
    scrollbar.grid(row=row_num, column=column_num+2, sticky='ns', padx=5, pady=5)

    listbox = tk.Listbox(widget, yscrollcommand=scrollbar.set, height=1, exportselection=0)
    listbox.grid(row=row_num, column=column_num+1, padx=5, pady=5)
    listbox.bind('<<ListboxSelect>>', lambda event: gf.get_selected_listbox_value(event, listbox, list_of_options))

    scrollbar.config(command=listbox.yview)

    for item in list_of_options:
        listbox.insert(tk.END, item)

    return listbox, scrollbar

