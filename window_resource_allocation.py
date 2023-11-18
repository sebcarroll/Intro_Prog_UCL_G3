import tkinter as tk
from tkinter import ttk, Listbox
from general_functions import create_listbox_with_label
from general_functions import check_input_valid
from general_functions import get_selected_listbox_value

class ResourceAllocation:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title('Allocate Resources')
        self.window.geometry('400x400')

        #Comes from list of IDs created by admin in camp creation
        camp_ids = ["Camp_1", "Camp_2", "Camp_3", "Camp_4"]
        camp_id_listbox: Listbox
        camp_id_listbox, camp_id_scrollbar = create_listbox_with_label(self.window, "Camp ID:", 0, 0, camp_ids)


        tk.Label(self.window, text="Number of Weeks of Aid:").grid(row=1, column=0)
        no_weeks_aid_entry = tk.Entry(self.window)
        no_weeks_aid_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Total Food Supplied to Camp:").grid(row=2, column=0)
        total_food_supplied_entry = tk.Entry(self.window)
        total_food_supplied_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Total Medicine Supplied to Camp:").grid(row=3, column=0)
        total_medicine_supplied_entry = tk.Entry(self.window)
        total_medicine_supplied_entry.grid(row=3, column=1)

        #This will eventually come from the number of refugees stored with the camp_id
        tk.Label(self.window, text="Number of Refugees:").grid(row=4, column=0)
        no_refugees_entry = tk.Entry(self.window)
        no_refugees_entry.grid(row=4, column=1)

        food_amount_refugee = [7, 14, 21, 28]
        food_amount_refugee_listbox, food_amount_refugee_scrollbar = create_listbox_with_label(self.window, "Number of Weekly Meals Provided per Refugee: ", 5, 0, food_amount_refugee)

        medicine_amount_refugee = [0, 1, 2, 3, 4, 5, 6, 7]
        medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(self.window, "Individual Refugee Weekly Medicine Allocation: ", 6, 0, medicine_amount_refugee)

        estimated_delivery_time_options = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
        estimated_delivery_time_listbox, estimated_delivery_time_scrollbar = create_listbox_with_label(self.window, "Estimated Resource Delivery Time (weeks): ", 7, 0, estimated_delivery_time_options)

        message_label = tk.Label(self.window, text="")
        submit_button_row = 8
        submit_button_column = 0

        submit_button = ttk.Button(self.window, text="Submit", command=self.admin_resource_submit)
        submit_button.grid(row=8, column=0, columnspan=2)

    def admin_resource_submit(self):

        camp_id = get_selected_listbox_value(camp_id_listbox)
        check_input_valid(camp_id, self.window, message_label, submit_button_row,submit_button_column)

        no_weeks_aid = no_weeks_aid_entry.get()
        check_input_valid(no_weeks_aid, self.window, message_label, submit_button_row, submit_button_column)

        total_food_supplied = total_food_supplied_entry.get()
        check_input_valid(total_food_supplied, self.window, message_label, submit_button_row, submit_button_column)

        total_medicine_supplied = total_medicine_supplied_entry.get()
        check_input_valid(total_medicine_supplied, self.window, message_label, submit_button_row, submit_button_column)

        no_refugees = no_refugees_entry.get() # Will need to come from the volunteer.
        check_input_valid(no_refugees, self.window, message_label, submit_button_row, submit_button_column)

        week_food_per_refugee = get_selected_listbox_value(food_amount_refugee_listbox)
        check_input_valid(week_food_per_refugee, self.window, message_label, submit_button_row, submit_button_column)

        week_medicine_per_refugee = get_selected_listbox_value(medicine_amount_refugee_listbox)
        check_input_valid(week_medicine_per_refugee, self.window, message_label, submit_button_row, submit_button_column)

        delivery_time_weeks = get_selected_listbox_value(estimated_delivery_time_listbox)
        check_input_valid(delivery_time_weeks, self.window, message_label, submit_button_row, submit_button_column)


