import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_selected_date():
    day = day_combobox.get()
    month = month_combobox.get()
    year = year_combobox.get()
    selected_date = f"{day} {month} {year}"
    messagebox.showinfo("Selected Date", f"You selected: {selected_date}")

root = tk.Tk()
root.title("Custom Date Input Example")

# Days
day_label = ttk.Label(root, text="Day:")
day_label.grid(row=0, column=0)
day_combobox = ttk.Combobox(root, values=list(range(1, 32)))
day_combobox.grid(row=0, column=1)
day_combobox.set(1)  # Default to the 1st day

# Months
month_label = ttk.Label(root, text="Month:")
month_label.grid(row=0, column=2)
month_combobox = ttk.Combobox(root, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
month_combobox.grid(row=0, column=3)
month_combobox.set("January")  # Default to January

# Years
year_label = ttk.Label(root, text="Year:")
year_label.grid(row=0, column=4)
year_combobox = ttk.Combobox(root, values=list(range(2020, 2025)))
year_combobox.grid(row=0, column=5)
year_combobox.set(2023)  # Default to the current year

# Button to get the selected date
get_date_button = ttk.Button(root, text="Get Selected Date", command=get_selected_date)
get_date_button.grid(row=1, column=0, columnspan=6, pady=10)

root.mainloop()