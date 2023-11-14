import tkinter as tk
from tkinter import ttk
from admin_resource_allocation_functions import admin_resource_submit


root = tk.Tk()
root.geometry('750x600')

tk.Label(root, text="Camp ID:").grid(row=0, column=0)
camp_id_entry = tk.Entry(root)
camp_id_entry.grid(row=0, column=1)

tk.Label(root, text="Number of Weeks of Aid:").grid(row=0, column=0)
no_weeks_aid_entry = tk.Entry(root)
no_weeks_aid_entry.grid(row=0, column=1)

tk.Label(root, text="Total Food Supplied to Camp:").grid(row=1, column=0)
total_food_supplied_entry = tk.Entry(root)
total_food_supplied_entry.grid(row=1, column=1)

tk.Label(root, text="Total Medicine Supplied to Camp:").grid(row=2, column=0)
total_medicine_supplied_entry = tk.Entry(root)
total_medicine_supplied_entry.grid(row=2, column=1)

tk.Label(root, text="Number of Refugees:").grid(row=3, column=0)
no_refugees_entry = tk.Entry(root)
no_refugees_entry.grid(row=3, column=1)

tk.Label(root, text="Weekly Food Amount Provided per Refugee:").grid(row=4, column=0)
week_food_per_refugee_entry = tk.Entry(root)
week_food_per_refugee_entry.grid(row=4, column=1)

tk.Label(root, text="Weekly Medicine Amount Provided per Refugee:").grid(row=5, column=0)
week_medicine_per_refugee_entry = tk.Entry(root)
week_medicine_per_refugee_entry.grid(row=5, column=1)

tk.Label(root, text="Estimated Resource Delivery Time to Camp:").grid(row=6, column=0)
delivery_time_weeks_entry = tk.Entry(root)
delivery_time_weeks_entry.grid(row=6, column=1)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=admin_resource_submit)
submit_button.grid(row=7, column=0, columnspan=2)

# Running the application
root.mainloop()