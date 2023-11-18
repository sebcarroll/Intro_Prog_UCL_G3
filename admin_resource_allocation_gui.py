import tkinter as tk
from tkinter import ttk, Listbox
from general_functions import create_listbox_with_label
from general_functions import check_input_valid
from general_functions import get_selected_listbox_value

"""root = tk.Tk()
window = root
root.geometry('750x600')"""


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

medicine_amount_refugee = [0, 1, 2, 3, 4, 5, 6, 7]
medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(root, "Number of Health Supplies Provided per Refugee Weekly: ", 6, 0, medicine_amount_refugee)

estimated_delivery_time_options = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
estimated_delivery_time_listbox, estimated_delivery_time_scrollbar = create_listbox_with_label(root, "Estimated Resource Delivery Time (weeks): ", 7, 0, estimated_delivery_time_options)

message_label = tk.Label(window, text="")
submit_button_row = 8
submit_button_column = 0
submit_column_span = 2

def admin_resource_submit():

    camp_id = get_selected_listbox_value(camp_id_listbox)
    check_input_valid(camp_id,window, message_label, submit_button_row,submit_button_column,submit_column_span)

    no_weeks_aid = no_weeks_aid_entry.get()
    check_input_valid(no_weeks_aid, window, message_label, submit_button_row, submit_button_column,submit_column_span)

    total_food_supplied = total_food_supplied_entry.get()
    check_input_valid(total_food_supplied, window, message_label, submit_button_row, submit_button_column, submit_column_span)

    total_medicine_supplied = total_medicine_supplied_entry.get()
    check_input_valid(total_medicine_supplied, window, message_label, submit_button_row, submit_button_column,submit_column_span )

    no_refugees = no_refugees_entry.get() # Will need to come from the volunteer.
    check_input_valid(no_refugees, window, message_label, submit_button_row, submit_button_column, submit_column_span)

    week_food_per_refugee = get_selected_listbox_value(food_amount_refugee_listbox)
    check_input_valid(week_food_per_refugee, window, message_label, submit_button_row, submit_button_column, submit_column_span)

    week_medicine_per_refugee = get_selected_listbox_value(medicine_amount_refugee_listbox)
    check_input_valid(week_medicine_per_refugee, window, message_label, submit_button_row, submit_button_column, submit_column_span)

    delivery_time_weeks = get_selected_listbox_value(estimated_delivery_time_listbox)
    check_input_valid(delivery_time_weeks, window, message_label, submit_button_row, submit_button_column, submit_column_span)


submit_button = ttk.Button(root, text="Submit", command=admin_resource_submit)

submit_button.grid(row=8, column=0, columnspan=2)


root.mainloop()