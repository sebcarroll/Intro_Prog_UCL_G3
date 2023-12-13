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

        new_plan_frame = tk.Frame(self.window)
        new_plan_frame.grid(row=0, column=0)

        self.day_combobox = None
        self.month_combobox = None
        self.year_combobox = None

        # def open_calendar():
        #     calendar_window = tk.Toplevel()
        #     calendar_window.title("Calendar Humanitarian Crisis")

        # def is_valid_date(day, month, year):
        #     try:
        #         date_str = f"{day} {month} {year}"
        #         selected_date = datetime.strptime(date_str, "%d %B %Y").date()
        #         current_date = datetime.now().date()
        #
        #         if selected_date > current_date:
        #             raise ValueError("Selected date must be in the past.")
        #         return True
        #
        #     except ValueError as e:
        #         messagebox.showerror("Invalid Date", str(e))
        #         return False


            #     else:
            #         messagebox.showerror("Invalid Date", "Please select a valid date.")
            # else:
            # messagebox.showerror("Invalid Date", "Please select a valid date.")




        #
        # def get_selected_date():
        #     day = self.day_combobox.get()
        #     month = self.month_combobox.get()
        #     year = self.year_combobox.get()


        current_date = datetime.now()
        self.current_year = current_date.year
        current_month = current_date.strftime("%B")
        current_day = current_date.day


        day_label = ttk.Label(new_plan_frame, text="Day:")
        day_label.grid(row=14, column=3)
        self.day_combobox = ttk.Combobox(new_plan_frame, values=self.days)
        self.day_combobox.grid(row=14, column=4)
        self.day_combobox.set(current_day)

        month_label = ttk.Label(new_plan_frame, text="Month:")
        month_label.grid(row=15, column=3)
        self.month_combobox = ttk.Combobox(new_plan_frame,
                                           values=self.months)
        self.month_combobox.grid(row=15, column=4)
        self.month_combobox.set(current_month)

        year_label = ttk.Label(new_plan_frame, text="Year:")
        year_label.grid(row=16, column=3)
        self.year_combobox = ttk.Combobox(new_plan_frame, values=list(range(self.current_year, self.current_year - 2, -1)))
        self.year_combobox.grid(row=16, column=4)
        self.year_combobox.set(self.current_year)



        refugee_title = tk.Label(new_plan_frame, text='Log New Crisis Event', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=3, pady=30)

        # def randnum(self):
        #     import random
        #     value = random.randint(10000, 99999)
        #     print(value)
        #     displayVariable.set(f"Generated Camp ID: {value}")
        #     camp_ID_generator_button.destroy()
        #     return value



        # camp_ID_generator_button = tk.Button(new_plan_frame, text="Generate Camp ID")
        # camp_ID_generator_button.bind("<Button-1>", generate_camp_id)
        # camp_ID_generator_button.grid(row=17, column=3, padx=5)
        #
        # displayVariable = tk.StringVar()
        # displayLabel = tk.Label(new_plan_frame, textvariable=displayVariable)
        # displayLabel.grid(row=17, column=4, padx=5)

        start_date_label = tk.Label(new_plan_frame, text="Please select the start date below", font=("TkinterDefault", 15))
        start_date_label.grid(row=13, column=3)

        crisis_type_label = tk.Label(new_plan_frame, text='Crisis Type', font=('TkinterDefault', 15))
        crisis_type_label.grid(row=7, column=3, padx=5)
        crisis_type = ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]
        self.crisis_type_combobox = ttk.Combobox(new_plan_frame, values=crisis_type)
        self.crisis_type_combobox.grid(row=7, column=4, padx=5)

        description_label = tk.Label(new_plan_frame, text='Description (max 100 characters)', font=('TkinterDefault', 15))
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
    
        self.save_plan_button = tk.Button(new_plan_frame, text="Save plan", command=self.plan_dict
                                     , height=1, width=20)
        self.save_plan_button.grid(row=19, column=3)

        back_button = tk.Button(new_plan_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=19, column=1, padx=5, pady=10)



    def character_limit(self):
        if len(self.description_label_Entry.get()) > 100:
            self.description_label_Entry.delete(100, tk.END)

    def plan_dict(self):
        try:
            crisis_type = self.crisis_type_combobox.get()

            description = self.description_label_Entry.get()
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
            self.save_plan_button.config(state=tk.DISABLED)
            self.save_plan_button.destroy()

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
                  "Refugee Capacity",
                  "Duration",
                  "Meals(Total)",
                  "Medicine(Total)",
                  "Meals/w",
                  "Medicine/w",
                  "Delivery Time(d)",
                  "Refugee Count"
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

