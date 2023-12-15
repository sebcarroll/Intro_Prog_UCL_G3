import tkinter as tk
from tkinter import ttk
import pandas as pd
import datetime as dt
from tkinter import messagebox

class AdminEndEvent:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main

    def create_gui_end_event(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        for i in range(9):
            self.window.grid_columnconfigure(i, weight=1)
        end_plan_frame = tk.Frame(self.window)
        end_plan_frame.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
        for i in range(9):
            end_plan_frame.grid_columnconfigure(i, weight=1)
        for i in range(9):
            end_plan_frame.grid_rowconfigure(i, weight=1)

        # Labels
        end_plan_title = tk.Label(end_plan_frame, text="End Plan", font=('TKDefault', 25))
        end_plan_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)

        self.end_plan_tree = ttk.Treeview(end_plan_frame, height=15)
        self.end_plan_tree.grid(row=1, column=0, columnspan=9, sticky="ew", padx=10, pady=5)



        # Button Frame:
        btn_frame = tk.Frame(end_plan_frame)
        btn_frame.grid(row=2, column=4, pady=10)
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(2, weight=1)

        # Buttons
        end_event_btn = tk.Button(btn_frame, text="End Event", command=lambda: self.deactivate_csv_data_entry(self.end_plan_tree, csv_file))
        end_event_btn.grid(row=0, column=0, padx=20, pady=(50,10))

        # Back button
        back_button = tk.Button(btn_frame, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=2, column=0, padx=5, pady=40)



        # CSV data
        csv_file = "crisis_events.csv"
        # csv_data = self.load_csv_data(csv_file)
        try:
            self.upload_csv_data(self.end_plan_tree, csv_file)
        except:
            messagebox.showwarning("No data found",
                                   "There is a problem accessing the database\n\nThe file may be missing or corrupted")
            self.back_button_to_admin_main()

    def upload_csv_data(self, tree, filename):
        data = pd.read_csv(filename)
        selected_attributes = ['Camp ID', 'Crisis Type', 'Description', 'Country', 'Day', 'Month', 'Year', 'Status', 'End Date', 'Refugees']
        data = data[selected_attributes]
        # Only want to see 'Active' plans:
        data = data[data['Status'] != 'Inactive']

        # The following block will convert floats to integers for the GUI to remove the ".0"
        # columns with float numbers
        float_columns = data.select_dtypes(include=['float']).columns
        # Convert floats to integers for display in treeview
        for col in float_columns:
            data[col] = data[col].fillna(0).astype(int)

        tree.delete(*tree.get_children())
        tree['columns'] = selected_attributes[0:7] + ['Refugees']
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        # Manual column width for all headers - used to be just the date here (see docstring below)
        tree.column("Camp ID", width=2, anchor=tk.CENTER)
        tree.column("Crisis Type", width=50, anchor=tk.CENTER)
        tree.column("Description", width=400, anchor=tk.CENTER)
        tree.column("Country", width=50, anchor=tk.CENTER)
        tree.column("Day", width=1, anchor=tk.CENTER)
        tree.column("Month", width=4, anchor=tk.CENTER)
        tree.column("Year", width=1, anchor=tk.CENTER)
        tree.column("Refugees", width=50, anchor=tk.CENTER)

        for col in selected_attributes[0:7] + ['Refugees']:
            # added condition based on date attributes
            '''if col != "Day" and col != "Month" and col != "Year" and col != "Camp ID":
                tree.column(col, anchor=tk.CENTER, width=80)'''
            tree.heading(col, text=col, anchor=tk.CENTER)

        for index, row in data.iterrows():
            #row_vals = row[selected_attributes[0:7]]
            tree.insert("", tk.END, values=list(row[selected_attributes[0:7] + ['Refugees']]), iid=str(index))


    def deactivate_csv_data_entry(self, tree, filename):
        selected_item = self.end_plan_tree.focus()
        if not selected_item:
            messagebox.showinfo("No selection", "Please select to end a plan")
            return
        if messagebox.askokcancel("End plan?", "Are you sure you want to deactivate this plan?"
                                               "\n\nAccess to this plan will be restricted to 'View Summaries'"
                                               "\nYour plan will have a status of 'Inactive'"
                                  ):
            selected_item = tree.selection()
            if selected_item:
                # Get index of the selected row
                index = int(selected_item[0])

                data = pd.read_csv(filename)

                current_datetime = dt.datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

                # Load current csv data, remove selected row, then save back to csv as an inactive plan
                if index < len(data):
                    data.at[index, 'Status'] = 'Inactive'  # update status to Inactive
                    data.at[index, 'End Date'] = formatted_datetime  # update end date attribute to datetime now

                    # Save updated data back to the csv file
                    data.to_csv(filename, index=False)

                    # Remove selected row from treeview
                    tree.delete(selected_item)

                # Refresh treeview
                #self.upload_csv_data(tree, filename)

