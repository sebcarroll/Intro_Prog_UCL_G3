import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv

class t_no_text(Exception):
    pass

class invalid_date(Exception):
    pass

class option_no_exist(Exception):
    pass

class date_not_in_past(Exception):
    pass


class AdminCreatePlan:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main
        self.day_combobox = None
        self.month_combobox = None
        self.year_combobox = None
        self.selected_date = None

        self.days = list(range(1, 32))
        self.months = ["January", "February", "March", "April", "May", "June", "July",
                       "August", "September", "October", "November", "December"]

        #self.new_plan_frame = None

    def create_plan_gui(self, window):
        for i in self.window.winfo_children():
            i.grid_forget()
        for i in range(9):
            self.window.grid_columnconfigure(i, weight=1)
        new_plan_frame = tk.Frame(self.window)
        new_plan_frame.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
        for i in range(9):
            new_plan_frame.grid_columnconfigure(i, weight=1)
        for i in range(9):
            new_plan_frame.grid_rowconfigure(i, weight=1)

        self.day_combobox = None
        self.month_combobox = None
        self.year_combobox = None

        current_date = datetime.now()
        self.current_year = current_date.year
        current_month = current_date.strftime("%B")
        current_day = current_date.day

        # TITLE
        refugee_title = tk.Label(new_plan_frame, text='Create New Crisis Event', font=('TKDefault', 25), fg='white')
        refugee_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
        refugee_title.configure(background="grey")

        # NEW CAMP INFO
        country_label = tk.Label(new_plan_frame, text='Country of crisis', font=('TkinterDefault', 15))
        country_label.grid(row=2, column=2, padx=5)
        self.country_Entry = ttk.Combobox(new_plan_frame, values=[
            "Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan", "Democratic Republic of the Congo",
            "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic", "Libya",
            "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon", "Zimbabwe", "Eritrea",
            "North Korea", "Eswatini", "Zambia", "Malawi"])
        self.country_Entry.grid(row=2, column=3, padx=5)

        crisis_type_label = tk.Label(new_plan_frame, text='Crisis Type', font=('TkinterDefault', 15))
        crisis_type_label.grid(row=3, column=2, padx=5)
        crisis_type = ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]
        self.crisis_type_combobox = ttk.Combobox(new_plan_frame, values=crisis_type)
        self.crisis_type_combobox.grid(row=3, column=3, padx=5)

        description_label = tk.Label(new_plan_frame, text='Description (max 100 characters)',
                                     font=('TkinterDefault', 15))
        description_label.grid(row=4, column=2, padx=5)
        self.description_label_Entry = tk.Text(new_plan_frame, height=7, width=20, font=("TkinterDefault", 10))
        self.description_label_Entry.grid(row=4, column=3, padx=5)
        self.description_label_Entry.bind('<KeyRelease>', lambda event: self.character_lim())


        # Date
        start_date_label = tk.Label(new_plan_frame, text="Please select the start date below",
                                    font=("TkinterDefault", 15))
        start_date_label.grid(row=6, column=2)

        day_label = ttk.Label(new_plan_frame, text="Day:")
        day_label.grid(row=7, column=2, sticky='s')
        self.day_combobox = ttk.Combobox(new_plan_frame, values=self.days)
        self.day_combobox.grid(row=7, column=3, sticky='s')
        self.day_combobox.set(current_day)

        month_label = ttk.Label(new_plan_frame, text="Month:")
        month_label.grid(row=8, column=2)
        self.month_combobox = ttk.Combobox(new_plan_frame,
                                           values=self.months)
        self.month_combobox.grid(row=8, column=3)
        self.month_combobox.set(current_month)

        year_label = ttk.Label(new_plan_frame, text="Year:")
        year_label.grid(row=9, column=2, sticky='n')
        self.year_combobox = ttk.Combobox(new_plan_frame, values=list(range(self.current_year, self.current_year - 2, -1)))
        self.year_combobox.grid(row=9, column=3, sticky='n', pady=(0,20))
        self.year_combobox.set(self.current_year)



        # Buttons
        self.save_plan_button = tk.Button(new_plan_frame, text="Save plan", command=self.plan_dict, height=1, width=20)
        self.save_plan_button.grid(row=19, column=3, pady=40)

        back_button = tk.Button(new_plan_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=19, column=2, padx=5, pady=40)

    def character_lim(self):
        if len(self.description_label_Entry.get("1.0", tk.END)) > 100:
            messagebox.showerror('Error', 'Description must contain less than 100 characters')
            self.description_label_Entry.delete("1.0", tk.END)

    def plan_dict(self):
        try:
            crisis_type = self.crisis_type_combobox.get()
            description = self.description_label_Entry.get("1.0", "end-1c").strip()

            if description == "":
                description = "No description"

            country = self.country_Entry.get()

            selected_day = int(self.day_combobox.get())
            selected_month = self.month_combobox.get()
            selected_year = int(self.year_combobox.get())

            if (
                    selected_day in self.days
                    and selected_month in self.months
                    and selected_year in range(self.current_year, self.current_year - 2, -1)
            ):

                day = str(selected_day)
                month = str(selected_month)
                year = str(selected_year)

                new_camp_id = self.generate_camp_id()
                date_str = f"{selected_day} {selected_month} {selected_year}"
                selected_date = datetime.strptime(date_str, "%d %B %Y").date()
                current_date = datetime.now().date()
                if selected_date > current_date:
                    raise date_not_in_past
            # return True

            else:
                raise invalid_date

            if not datetime(year=selected_year,month = self.months.index(selected_month)+1,day=selected_day):
                raise invalid_date


            status = "Active"
            end_date = "0000-00-00 00:00:00"

            self.events_dict = {
                'Camp ID': new_camp_id,
                'Crisis Type': crisis_type,
                'Description': description,
                'Country': country,
                'Day': day,
                'Month': month,
                'Year': year,
                'Status': status,
                'End Date': end_date
            }


            if crisis_type not in ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]:
                raise option_no_exist

            if country not in ["Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan",
                               "Democratic Republic of the Congo",
                               "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic",
                               "Libya",
                               "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon",
                               "Zimbabwe", "Eritrea",
                               "North Korea", "Eswatini", "Zambia", "Malawi"]:

                raise option_no_exist

            print(self.events_dict)
            tkinter.messagebox.showinfo(title="Plan created", message=f"Plan successfully created - Camp ID is {self.generate_camp_id()}")
            self.save_to_csv()
            #self.save_plan_button.config(state=tk.DISABLED)
            #self.save_plan_button.destroy()

            self.clear_entry(self.crisis_type_combobox)
            self.clear_entry(self.description_label_Entry)
            self.clear_entry(self.country_Entry)


        except option_no_exist:
            tk.messagebox.showinfo(title="Option does not exist", message="Please make sure you've selected valid options")
        except (invalid_date, ValueError):
            tk.messagebox.showinfo(title="Invalid valid date", message="Please enter a valid date")
        except(date_not_in_past):
            tk.messagebox.showinfo(title='Date not in past', message='Please select a date in the past')

    def generate_camp_id(self):
        import random
        value = random.randint(10000, 99999)
        print(value)
        return value

    def save_to_csv(self):

        header = ["Camp ID",
                  "Crisis Type",
                  "Description",
                  "Country",
                  "Day",
                  "Month",
                  "Year", 
                  "Status",
                  "End Date",
                  "Capacity",
                  "Duration",
                  "Meals(T)",
                  "Medicine(T)",
                  "Meals/w",
                  "Medicine/w",
                  "Delivery Time(d)",
                  "Refugees"
                  ]

        for key in header:
            if key not in self.events_dict:
                self.events_dict[key] = ""

        data = [self.events_dict]

        with open("crisis_events.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def clear_entry(entry):
        #entry.delete(0, tk.END)
        if isinstance(entry, tk.Entry):
            entry.delete(0, tk.END)
        elif isinstance(entry, ttk.Combobox):
            entry.set('')
        elif isinstance(entry, tk.Text):
            entry.delete("1.0", tk.END)
