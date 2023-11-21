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
