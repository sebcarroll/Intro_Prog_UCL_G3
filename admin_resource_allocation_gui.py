import tkinter as tk
from tkinter import ttk
from admin_resource_allocation_functions import admin_resource_submit
from general_functions import create_listbox_with_label

root = tk.Tk()
root.geometry('750x600')
#Comes from list of IDs created by admin in camp creation
camp_ids = ["Camp_1", "Camp_2", "Camp_3", "Camp_4"]
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
medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(root, "Individual Refugee Weekly Medicine Allocation: ", 6, 0, medicine_amount_refugee)

estimated_delivery_time_options = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
estimated_delivery_time_listbox, estimated_delivery_time_scrollbar = create_listbox_with_label(root, "Estimated Resource Delivery Time (weeks): ", 7, 0, estimated_delivery_time_options)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=admin_resource_submit)
submit_button.grid(row=8, column=0, columnspan=2)

# Running the application
root.mainloop()