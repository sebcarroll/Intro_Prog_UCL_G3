import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv

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

        self.day_combobox = None
        self.month_combobox = None
        self.year_combobox = None

        def open_calendar():
            calendar_window = tk.Toplevel()
            calendar_window.title("Calendar Humanitarian Crisis")

            def is_valid_date(day, month, year):
                try:
                    date_str = f"{day} {month} {year}"
                    selected_date = datetime.strptime(date_str, "%d %B %Y").date()
                    current_date = datetime.now().date()

                    if selected_date > current_date:
                        raise ValueError("Selected date must be in the past.")

                    return True
                except ValueError as e:
                    messagebox.showerror("Invalid Date", str(e))
                    return False

            def get_selected_date():
                day = self.day_combobox.get()
                month = self.month_combobox.get()
                year = self.year_combobox.get()

                if day and month and year:
                    if is_valid_date(day, month, year):
                        selected_date = f"{day} {month} {year}"
                        # calendar_window.destroy()
                    else:
                        messagebox.showerror("Invalid Date", "Please select a valid date.")
                else:
                    messagebox.showerror("Invalid Date", "Please select a valid date.")

            current_date = datetime.now()
            current_year = current_date.year
            current_month = current_date.strftime("%B")
            current_day = current_date.day

            day_label = ttk.Label(calendar_window, text="Day:")
            day_label.grid(row=0, column=0)
            self.day_combobox = ttk.Combobox(calendar_window, values=list(range(1, 32)))
            self.day_combobox.grid(row=0, column=1)
            self.day_combobox.set(current_day)

            month_label = ttk.Label(calendar_window, text="Month:")
            month_label.grid(row=0, column=2)
            self.month_combobox = ttk.Combobox(calendar_window,
                                               values=["January", "February", "March", "April", "May", "June", "July",
                                                       "August", "September", "October", "November", "December"])
            self.month_combobox.grid(row=0, column=3)
            self.month_combobox.set(current_month)

            year_label = ttk.Label(calendar_window, text="Year:")
            year_label.grid(row=0, column=4)
            self.year_combobox = ttk.Combobox(calendar_window, values=list(range(current_year, current_year - 2, -1)))
            self.year_combobox.grid(row=0, column=5)
            self.year_combobox.set(current_year)

            get_date_button = ttk.Button(calendar_window, text="save date", command=get_selected_date)
            get_date_button.grid(row=1, column=0, columnspan=6, pady=10)

            # button_close = ttk.Button(
            #     calendar_window,
            #     text="Close window",
            #     command=calendar_window.destroy)
            # button_close.place(x=75, y=75)

        button_open = ttk.Button(
            new_plan_frame,
            text="Select Date",
            command=open_calendar)
        button_open.place(x=475, y=185)

        refugee_title = tk.Label(new_plan_frame, text='Log New Crisis Event', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=3, pady=30)

        def randnum(event):
            import random
            value = random.randint(10000, 99999)
            print(value)
            displayVariable.set(f"Generated Camp ID: {value}")
            camp_ID_generator_button.destroy()

        camp_ID_generator_button = tk.Button(new_plan_frame, text="Generate Camp ID")
        camp_ID_generator_button.bind("<Button-1>", randnum)
        camp_ID_generator_button.grid(row=15, column=3, padx=5)

        displayVariable = tk.StringVar()
        displayLabel = tk.Label(new_plan_frame, textvariable=displayVariable)
        displayLabel.grid(row=15, column=4, padx=5)

        start_date_label = tk.Label(new_plan_frame, text="Please press the button to select the start date", font=("TkinterDefault", 15))
        start_date_label.grid(row=13, column=3)

        crisis_type_label = tk.Label(new_plan_frame, text='Crisis Type', font=('TkinterDefault', 15))
        crisis_type_label.grid(row=7, column=3, padx=5)
        crisis_type = ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]
        self.crisis_type_combobox = ttk.Combobox(new_plan_frame, values=crisis_type)
        self.crisis_type_combobox.grid(row=7, column=4, padx=5)

        description_label = tk.Label(new_plan_frame, text='Description', font=('TkinterDefault', 15))
        description_label.grid(row=11, column=3, padx=5)
        self.description_label_Entry = tk.Entry(new_plan_frame)
        self.description_label_Entry.grid(row=11, column=4, padx=5)
        self.description_label_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        country_label = tk.Label(new_plan_frame, text='Country of crisis', font=('TkinterDefault', 15))
        country_label.grid(row=1, column=3, padx=5)
        self.country_Entry = ttk.Combobox(new_plan_frame, values=[
            "Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan", "Democratic Republic of the Congo",
            "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic", "Libya",
            "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon", "Zimbabwe", "Eritrea",
            "North Korea", "Eswatini", "Zambia", "Malawi"])
        self.country_Entry.grid(row=1, column=4, padx=5)

        save_plan_button = tk.Button(new_plan_frame, text="Save plan", command=self.plan_dict, height=1, width=20)
        save_plan_button.grid(row=19, column=3)

        back_button = tk.Button(new_plan_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=19, column=1, padx=5, pady=10)

        self.window.mainloop()

    def character_limit(self):
        if len(self.description_label_Entry.get()) > 100:
            self.description_label_Entry.delete(100, tk.END)

    def plan_dict(self):
        try:
            crisis_type = self.crisis_type_combobox.get()
            description = self.description_label_Entry.get()
            country = self.country_Entry.get()

            if self.day_combobox is not None and self.month_combobox is not None and self.year_combobox is not None:
                day = str(self.day_combobox.get())
                month = str(self.month_combobox.get())
                year = str(self.year_combobox.get())
            else:
                raise ValueError("Please select a valid date.")

            new_camp_id = self.generate_camp_id()

            self.events_dict = {
                'New Camp ID': new_camp_id,
                'Crisis type': crisis_type,
                'Description': description,
                'Country': country,
                'Day': day,
                'Month': month,
                'Year': year
            }

            if crisis_type not in ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]:
                self.events_dict['Crisis type'] = ""

            if country not in ["Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan",
                               "Democratic Republic of the Congo",
                               "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic",
                               "Libya",
                               "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon",
                               "Zimbabwe", "Eritrea",
                               "North Korea", "Eswatini", "Zambia", "Malawi"]:
                self.events_dict["Country"] = ""

            print(self.events_dict)

            self.save_to_csv()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_camp_id(self):
        import random
        value = random.randint(10000, 99999)
        print(value)
        return value

    def save_to_csv(self):
        header = ["New Camp ID", "Crisis type", "Description", "Country", "Day", "Month", "Year"]
        data = [self.events_dict]

        with open("crisis_events.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(data)

    def back_button_to_admin_main(self):
        pass

AdminPage()
