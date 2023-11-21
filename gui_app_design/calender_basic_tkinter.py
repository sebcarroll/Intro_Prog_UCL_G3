import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def is_valid_date(day, month, year):
    try:
        date_str = f"{day} {month} {year}"
        selected_date= datetime.strptime(date_str, "%d %B %Y").date()
        current_date = datetime.now().date()
        return selected_date >= current_date
        return True
    except ValueError:
        return False


def get_selected_date():
    day = day_combobox.get()
    month = month_combobox.get()
    year = year_combobox.get()

    if is_valid_date(day, month, year):
        selected_date = f"{day} {month} {year}"
        messagebox.showinfo("Selected Date", f"start date of event: {selected_date}")
    else:
        messagebox.showerror("Invalid Date", "Please select a valid date.")

nawindow = tk.Tk()
nawindow.title("Calendar Humanitarian Crisis")


current_date = datetime.now()
current_year = current_date.year
current_month = current_date.strftime("%B")
current_day = current_date.day


day_label = ttk.Label(nawindow, text="Day:")
day_label.grid(row=0, column=0)
day_combobox = ttk.Combobox(nawindow, values=list(range(1, 32)))
day_combobox.grid(row=0, column=1)
day_combobox.set(current_day)


month_label = ttk.Label(nawindow, text="Month:")
month_label.grid(row=0, column=2)
month_combobox = ttk.Combobox(nawindow, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
month_combobox.grid(row=0, column=3)
month_combobox.set(current_month)


year_label = ttk.Label(nawindow, text="Year:")
year_label.grid(row=0, column=4)
year_combobox = ttk.Combobox(nawindow, values=list(range(current_year, current_year + 5)))
year_combobox.grid(row=0, column=5)
year_combobox.set(current_year)


get_date_button = ttk.Button(nawindow, text="select date", command=get_selected_date)
get_date_button.grid(row=1, column=0, columnspan=6, pady=10)

nawindow.mainloop()


current_date = datetime.now()
current_year = current_date.year
current_month = current_date.strftime("%B")
current_day = current_date.day
