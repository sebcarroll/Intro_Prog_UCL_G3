import tkinter as tk
from tkinter import ttk
import pandas as pd
import datetime as dt


class AdminEndEvent:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main

    def create_gui_end_event(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        end_plan_frame = tk.Frame(self.window)
        end_plan_frame.grid(sticky="nsew", padx=5, pady=5)
        end_plan_frame.grid_columnconfigure(0, weight=1)
        end_plan_frame.grid_rowconfigure(3, weight=1)

        # Labels
        end_plan_title = tk.Label(end_plan_frame, text="End Plan", font=('Helvetica', 16))
        end_plan_title.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew", pady=5, padx=5)

        end_plan_tree = ttk.Treeview(end_plan_frame)
        end_plan_tree.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        # CSV data
        csv_file = "crisis_events.csv"
        #csv_data = self.load_csv_data(csv_file)
        self.upload_csv_data(end_plan_tree, csv_file)

        # Buttons
        end_event_btn = tk.Button(self.window, text="End Event", command=lambda: self.deactivate_csv_data_entry(end_plan_tree, csv_file))
        end_event_btn.grid(row=6, column=0, padx=5, pady=10)

        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=8, column=0, padx=5, pady=10)


    def upload_csv_data(self, tree, filename):
        data = pd.read_csv(filename)
        selected_attributes = ['Camp ID', 'Crisis Type', 'Description', 'Country', 'Day', 'Month', 'Year', 'Status', 'End Date']
        data = data[selected_attributes]
        # Only want to see 'Active' plans:
        data = data[data['Status'] != 'Inactive']

        tree.delete(*tree.get_children())
        tree['columns'] = selected_attributes
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        # set size of column for date
        tree.column("Day", width=2, anchor=tk.CENTER)
        tree.column("Month", width=3, anchor=tk.CENTER)
        tree.column("Year", width=2, anchor=tk.CENTER)

        for col in selected_attributes:
            if col != "Day" and col != "Month" and col != "Year": #added condition based on attribute
                tree.column(col, anchor=tk.CENTER, width=80)
            tree.heading(col, text=col, anchor=tk.CENTER)

        for index, row in data.iterrows():
            tree.insert("", tk.END, values=list(row), iid=str(index))


    def deactivate_csv_data_entry(self, tree, filename):
        selected_item = tree.selection()
        if selected_item:
            # Get index of the selected row
            index = int(selected_item[0])

            data = pd.read_csv(filename)

            current_datetime = dt.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            # Load current CSV data, remove selected row, and save back to CSV
            if index < len(data):
                data.at[index, 'Status'] = 'Inactive'  # update status to Inactive
                data.at[index, 'End Date'] = formatted_datetime  # update status to datetime now

                # Save the updated data back to the CSV file
                data.to_csv(filename, index=False)

                # Remove the selected row from the Treeview
                tree.delete(selected_item)

            # Refresh the Treeview display
            #self.upload_csv_data(tree, filename)

