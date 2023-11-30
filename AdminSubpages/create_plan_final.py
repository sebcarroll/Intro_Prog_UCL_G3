from tkinter import *

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class t_no_text(Exception):
    pass

class AdminPage(t_no_text):
    def __init__(self):
        self.window = tk.Tk()
        self.day_combobox = None
        self.month_combobox = None
        self.year_combobox = None
        self.selected_date = None
        self.new_plan()

    def new_plan(self):
        for i in self.window.winfo_children():
            i.destroy()

        new_plan_frame = tk.Frame(self.window)
        new_plan_frame.grid()

        def open_calendar():
            calendar_window = tk.Toplevel()
            calendar_window.title("Calendar Humanitarian Crisis")

            def is_valid_date(day, month, year):
                try:
                    weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                    date_str = f"{day} {month} {year}"
                    selected_date = datetime.strptime(date_str, "%d %B %Y").date()
                    current_date = datetime.now().date()

                    # Check if the selected date is in the past
                    if selected_date > current_date:
                        raise ValueError("Selected date must be in the past.")

                    return True
                except ValueError as e:
                    messagebox.showerror("Invalid Date", str(e))
                    return False

            def get_selected_date():
                day = day_combobox.get()
                month = month_combobox.get()
                year = year_combobox.get()
                calendar_window.destroy()

                if is_valid_date(day, month, year):
                    selected_date = f"{day} {month} {year}"
                    messagebox.showinfo("Selected Date", f"Start date of event: {selected_date}")
                    self.selected_date = selected_date
                else:
                    messagebox.showerror("Invalid Date", "Please select a valid date.")

            current_date = datetime.now()
            current_year = current_date.year
            current_month = current_date.strftime("%B")
            current_day = current_date.day

            day_label = ttk.Label(calendar_window, text="Day:")
            day_label.grid(row=0, column=0)
            day_combobox = ttk.Combobox(calendar_window, values=list(range(1, 32)))
            day_combobox.grid(row=0, column=1)
            day_combobox.set(current_day)

            month_label = ttk.Label(calendar_window, text="Month:")
            month_label.grid(row=0, column=2)
            month_combobox = ttk.Combobox(calendar_window,
                                          values=["January", "February", "March", "April", "May", "June", "July",
                                                  "August", "September", "October", "November", "December"])
            month_combobox.grid(row=0, column=3)
            month_combobox.set(current_month)

            year_label = ttk.Label(calendar_window, text="Year:")
            year_label.grid(row=0, column=4)
            year_combobox = ttk.Combobox(calendar_window, values=list(range(current_year, current_year - 2, -1)))
            year_combobox.grid(row=0, column=5)
            year_combobox.set(current_year)

            get_date_button = ttk.Button(calendar_window, text="Select date", command=get_selected_date)
            get_date_button.grid(row=1, column=0, columnspan=6, pady=10)

            button_close = ttk.Button(
                calendar_window,
                text="Close window",
                command=calendar_window.destroy)
            button_close.place(x=75, y=75)

        button_open = ttk.Button(
            new_plan_frame,
            text="Select Date",
            command=open_calendar)
        button_open.place(x=475, y=130)

        refugee_title = tk.Label(new_plan_frame, text='Create New Plan', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=3, pady=30)

        camp_ID_label = tk.Label(new_plan_frame, text='New Camp ID', font=('TkinterDefault', 15))
        camp_ID_label.grid(row=3, column=3)

        def randnum(event):
            import random
            value = random.randint(10000, 99999)
            print(value)
            updateDisplay(value)

        def updateDisplay(myString):
            displayVariable.set(myString)

        button_1 = Button(new_plan_frame, text="Generate Camp ID")
        button_1.bind("<Button-1>", randnum)
        button_1.grid(row=3, column=4,padx=5)
        displayVariable = StringVar()
        displayLabel = Label(new_plan_frame, textvariable=displayVariable)
        displayLabel.grid(row=3, column=4, padx=5)



        start_date_label = tk.Label(new_plan_frame, text="Please press button to select start date", font=("TkinterDefault", 15))
        start_date_label.grid(row=5, column=3)

        crisis_type_label = tk.Label(new_plan_frame, text='Crisis Type', font=('TkinterDefault', 15))
        crisis_type_label.grid(row=7, column=3, padx=5)
        crisis_type = ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]
        self.crisis_type_combobox = ttk.Combobox(new_plan_frame, values=crisis_type)
        self.crisis_type_combobox.grid(row=7, column=4, padx=5)

        other_crisis_label = tk.Label(new_plan_frame, text='If crisis type not in list, please enter here', font=('TkinterDefault', 15))
        other_crisis_label.grid(row=9, column=3, padx=5)
        self.other_crisis_label_Entry = tk.Entry(new_plan_frame)
        self.other_crisis_label_Entry.grid(row=9, column=4, padx=5)
        self.other_crisis_label_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        description_label = tk.Label(new_plan_frame, text='Description', font=('TkinterDefault', 15))
        description_label.grid(row=11, column=3, padx=5)
        self.description_label_Entry = tk.Entry(new_plan_frame)
        self.description_label_Entry.grid(row=11, column=4, padx=5)
        self.description_label_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        country_label = tk.Label(new_plan_frame, text='Country of crisis', font=('TkinterDefault', 15))
        country_label.grid(row=13, column=3, padx=5)
        self.country_Entry = ttk.Combobox(new_plan_frame, values=[
            "Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan", "Democratic Republic of the Congo",
            "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic", "Libya",
            "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon", "Zimbabwe", "Eritrea",
            "North Korea", "Eswatini", "Zambia", "Malawi"])
        self.country_Entry.grid(row=13, column=4, padx=5)

        other_country_label = tk.Label(new_plan_frame, text='If country not in list, please enter here', font=('TkinterDefault', 15))
        other_country_label.grid(row=15, column=3, padx=5)
        self.other_country_Entry = tk.Entry(new_plan_frame)
        self.other_country_Entry.grid(row=15, column=4, padx=5)
        self.other_country_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        save_plan_button = tk.Button(new_plan_frame, text="Save plan", command=self.plan_dict, height=1, width=20)
        save_plan_button.grid(row=19, column=3)

        back_button = tk.Button(new_plan_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=19, column=1, padx=5, pady=10)

        self.window.mainloop()

    def character_limit(self):
        from tkinter import END
        if len(self.description_label_Entry.get()) > 100:
            self.description_label_Entry.delete(100, END)

    def plan_dict(self):
        self.events_dict = {}
        self.events_nested_dict = {}
        self.camp_ID = self.camp_IDbox.get()
        crisis_type = self.crisis_type_combobox.get()
        other_crisis = self.other_crisis_label_Entry.get()
        description = self.description_label_Entry.get()
        country = self.country_Entry.get()
        other_country = self.other_country_Entry.get()
        day = str(self.day_combobox.get())
        month = str(self.month_combobox.get())
        year = str(self.year_combobox.get())

        self.events_dict[self.camp_ID] = {
            'New Camp ID': self.camp_ID,
            'Crisis type': crisis_type,
            'Other crisis type': other_crisis,
            'Description': description,
            'Country': country,
            'Other Country': other_country,
            'Day': day,
            'Month': month,
            'Year': year
        }

        if crisis_type not in ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]:
            self.events_dict[self.camp_ID]['Crisis type'] = ""

        if country not in ["Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan",
                           "Democratic Republic of the Congo",
                           "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic",
                           "Libya",
                           "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon",
                           "Zimbabwe", "Eritrea",
                           "North Korea", "Eswatini", "Zambia", "Malawi"]:
            self.events_dict[self.camp_ID]["Country"] = ""

        print(self.events_dict)

    def back_button_to_admin_main(self):
        pass

AdminPage()


