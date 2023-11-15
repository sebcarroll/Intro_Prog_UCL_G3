import tkinter as tk
from tkinter import ttk
from admin_resource_allocation_functions import admin_resource_submit

def create_listbox_with_label(widget, text_label, num_rows, num_columns, item_list):
    tk.Label(widget, text=text_label).grid(row=num_rows, column=num_columns)

    scrollbar = tk.Scrollbar(widget)
    scrollbar.grid(row=num_rows, column=num_columns+2, sticky='ns')

    listbox = tk.Listbox(widget, yscrollcommand=scrollbar.set, height=1)
    listbox.grid(row=num_rows, column=num_columns+1)

    scrollbar.config(command=listbox.yview)

    for item in item_list:
        listbox.insert(tk.END, item)

    return listbox, scrollbar

root = tk.Tk()
root.geometry('750x600')

camp_ids = ["Camp_1", "Camp_2", "Camp_3", "Camp_4"]
camp_id_listbox, camp_id_scrollbar = create_listbox_with_label(root, "Camp ID:", 0, 0, camp_ids)


tk.Label(root, text="Number of Weeks of Aid:").grid(row=1, column=0)
no_weeks_aid_entry = tk.Entry(root)
no_weeks_aid_entry.grid(row=2, column=1)

tk.Label(root, text="Total Food Supplied to Camp:").grid(row=2, column=0)
total_food_supplied_entry = tk.Entry(root)
total_food_supplied_entry.grid(row=1, column=1)

tk.Label(root, text="Total Medicine Supplied to Camp:").grid(row=3, column=0)
total_medicine_supplied_entry = tk.Entry(root)
total_medicine_supplied_entry.grid(row=2, column=1)

tk.Label(root, text="Number of Refugees:").grid(row=4, column=0)
no_refugees_entry = tk.Entry(root)
no_refugees_entry.grid(row=3, column=1)

food_amount_refugee = ["7", "14", "21", "28"]
food_amount_refugee_listbox, food_amount_refugee_scrollbar = create_listbox_with_label(root, "Individual Refugee Weekly Food Allocation: ", 5, 0, food_amount_refugee)

medicine_amount_refugee = ["0", "1", "2", "3", "4", "5", "6", "7"]
medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(root, "Individual Refugee Weekly Medicine Allocation: ", 6, 0, medicine_amount_refugee)


# Label
tk.Label(root, text="Estimated Resource Delivery Time to Camp:").grid(row=7, column=0)

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=7, column=2, sticky='ns')

# Listbox with scrollbar
delivery_time_weeks_listbox = tk.Listbox(root, yscrollcommand=scrollbar.set, height=1)
delivery_time_weeks_listbox.grid(row=7, column=1)

# Configure scrollbar
scrollbar.config(command=delivery_time_weeks_listbox.yview)

# Example items for the Listbox
times = ["1 week", "2 weeks", "3 weeks", "4 weeks", "5 weeks", "6 weeks", "7 weeks", "8 weeks", "9 weeks", "10 weeks"]
for time in times:
    delivery_time_weeks_listbox.insert(tk.END, time)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=admin_resource_submit)
submit_button.grid(row=8, column=0, columnspan=2)

# Running the application
root.mainloop()