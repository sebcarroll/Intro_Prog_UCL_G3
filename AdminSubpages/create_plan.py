import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class AdminPage:

    def __init__(self):
        self.window = tk.Tk()
        self.new_plan()

    def new_plan(self):
        for i in self.window.winfo_children():
            i.destroy()

        new_plan_frame = tk.Frame(self.window)
        new_plan_frame.grid()

        def new_window():
            new_window = tk.Toplevel()
            new_window.title("Calendar Humanitarian Crisis")
            # new_window = tk.Toplevel()
            # new_window.title('start date window')
            # new_window.config(width=300, height=200)

            # add functions for the date
            def is_valid_date(day, month, year):
                try:
                    date_str = f"{day} {month} {year}"
                    selected_date = datetime.strptime(date_str, "%d %B %Y").date()
                    current_date = datetime.now().date()
                    return selected_date >= current_date
                    return True
                except ValueError:
                    return False

            def get_selected_date():
                day = self.day_combobox.get()
                month = self.month_combobox.get()
                year = self.year_combobox.get()
                new_window.destroy()

                if is_valid_date(day, month, year):
                    selected_date = f"{day} {month} {year}"
                    messagebox.showinfo("Selected Date", f"start date of event: {selected_date}")
                else:
                    messagebox.showerror("Invalid Date", "Please select a valid date.")



            current_date = datetime.now()
            current_year = current_date.year
            current_month = current_date.strftime("%B")
            current_day = current_date.day

            day_label = ttk.Label(new_window, text="Day:")
            day_label.grid(row=0, column=0)
            self.day_combobox = ttk.Combobox(new_window, values=list(range(1, 32)))
            self.day_combobox.grid(row=0, column=1)
            self.day_combobox.set(current_day)

            month_label = ttk.Label(new_window, text="Month:")
            month_label.grid(row=0, column=2)
            self.month_combobox = ttk.Combobox(new_window,
                                          values=["January", "February", "March", "April", "May", "June", "July",
                                                  "August", "September", "October", "November", "December"])
            self.month_combobox.grid(row=0, column=3)
            self.month_combobox.set(current_month)

            year_label = ttk.Label(new_window, text="Year:")
            year_label.grid(row=0, column=4)
            self.year_combobox = ttk.Combobox(new_window, values=list(range(current_year, current_year + 5)))
            self.year_combobox.grid(row=0, column=5)
            self.year_combobox.set(current_year)

            get_date_button = ttk.Button(new_window, text="select date", command=get_selected_date)
            get_date_button.grid(row=1, column=0, columnspan=6, pady=10)


            # Create a button to destroy this window
            button_close = ttk.Button(
                new_window,
                text="Close window",
                command=new_window.destroy)
            button_close.place(x=75, y=75)

        button_open = ttk.Button(
            new_plan_frame,
            text="Open select date page",
            command=new_window)

        button_open.place(x=100, y=100)

        refugee_title = tk.Label(new_plan_frame, text='Create New Plan', font=('TkinterDefault', 30))
        refugee_title.grid(row=0, column=1, pady=30)

        camp_ID_label = tk.Label(new_plan_frame, text='New Camp ID', font=('TkinterDefault', 15))
        camp_ID_label.grid(row=3, column=3)
        self.camp_IDbox = tk.Entry(new_plan_frame)
        self.camp_IDbox.grid(row=3, column=4, padx=5)

        crisis_type_label = tk.Label(new_plan_frame, text='Crisis Type', font=('TkinterDefault', 15))
        crisis_type_label.grid(row=5, column=3, padx=5)
        crisis_type = ["War", "Environmental", "Supply Shortage", "Political unrest", "Displacement", "Other"]
        self.crisis_type_combobox = ttk.Combobox(new_plan_frame, values=crisis_type)
        self.crisis_type_combobox.grid(row=5, column=4, padx=5)

        other_crisis_label = tk.Label(new_plan_frame, text='If crisis type not in list, please enter here', font=('TkinterDefault', 15))
        other_crisis_label.grid(row=7, column=3, padx=5)
        self.other_crisis_label_Entry = tk.Entry(new_plan_frame)
        self.other_crisis_label_Entry.grid(row=7, column=4, padx=5)
        self.other_crisis_label_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        description_label = tk.Label(new_plan_frame, text='Description', font=('TkinterDefault', 15))
        description_label.grid(row=9, column=3, padx=5)
        self.description_label_Entry = tk.Entry(new_plan_frame)
        self.description_label_Entry.grid(row=9, column=4, padx=5)
        self.description_label_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        country_label = tk.Label(new_plan_frame, text='Country of crisis', font=('TkinterDefault', 15))
        country_label.grid(row=11, column=3, padx=5)
        self.country_Entry = ttk.Combobox(new_plan_frame, values=[
            "Afghanistan", "Syria", "Yemen", "South Sudan", "Somalia", "Sudan", "Democratic Republic of the Congo",
            "Venezuela", "Iraq", "Nigeria", "Ethiopia", "Myanmar", "Haiti", "Central African Republic", "Libya",
            "Chad", "Mali", "Niger", "Cameroon", "Ukraine", "Pakistan", "Bangladesh", "Lebanon", "Zimbabwe", "Eritrea",
            "North Korea", "Eswatini", "Zambia", "Malawi"])
        self.country_Entry.grid(row=11, column=4, padx=5)

        other_country_label = tk.Label(new_plan_frame, text='If country not in list, please enter here', font=('TkinterDefault', 15))
        other_country_label.grid(row=13, column=3, padx=5)
        self.other_country_Entry = tk.Entry(new_plan_frame)
        self.other_country_Entry.grid(row=13, column=4, padx=5)
        self.other_country_Entry.bind('<KeyRelease>', lambda event: self.character_limit())

        created_by_label = tk.Label(new_plan_frame, text='Enter your name', font=("TkinterDefault", 15))
        created_by_label.grid(row=15, column=3, padx=5)
        self.created_by_Entry = tk.Entry(new_plan_frame)
        self.created_by_Entry.grid(row=15, column=4, padx=5)

        save_plan_button = tk.Button(new_plan_frame, text="Save plan", command=self.plan_dict, height=1, width=20)
        save_plan_button.grid(row=17, column=3)

        back_button = tk.Button(new_plan_frame, text='Back to Home', command="back_button_to_admin_main")
        back_button.grid(row=17, column=1, padx=5, pady=10)

        self.window.mainloop()

    def character_limit(self):
        from tkinter import END
        if len(self.description_label_Entry.get()) > 100:
            self.description_label_Entry.delete(100, END)

    def plan_dict(self):
        self.events_dict = {}
        self.events_nested_dict = {}
        self.events_dict[self.camp_IDbox] = {'New Camp ID': "", "Crisis type": "", "Other crisis type": "", "Description": "", "Country": "", "Other Country": "", "Name": "", "Start date": ""}
        camp_ID = self.camp_IDbox.get()
        crisis_type = self.crisis_type_combobox.get()
        other_crisis = self.other_crisis_label_Entry.get()
        description = self.description_label_Entry.get()
        country = self.country_Entry.get()
        other_country = self.other_country_Entry.get()
        admin_name = self.created_by_Entry.get()
        start_day = self.day_combobox.get()
        self.events_dict[self.camp_IDbox]['New Camp ID'] = camp_ID
        self.events_dict[self.camp_IDbox]['Crisis type'] = crisis_type
        self.events_dict[self.camp_IDbox]['Other crisis type'] = other_crisis
        self.events_dict[self.camp_IDbox]['Description'] = description
        self.events_dict[self.camp_IDbox]["Country"] = country
        self.events_dict[self.camp_IDbox]["Other Country"] = other_country
        self.events_dict[self.camp_IDbox]["Name"] = admin_name
        print(self.events_dict)

AdminPage()
