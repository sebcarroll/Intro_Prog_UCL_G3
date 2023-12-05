import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

class AdminEndEvent:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main


    def create_gui_end_event(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        end_plan_frame = tk.Frame(self.window)
        end_plan_frame.grid()

        # Labels
        end_plan_title = tk.Label(end_plan_frame, text="Admin End Plan", font=('Helvetica', 16))
        end_plan_title.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")

        end_plan_tree = ttk.Treeview(end_plan_frame)
        end_plan_tree.grid(row=3, column=0, columnspan=20, rowspan=1, sticky="ew")




        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Specify the relative path to the CSV file in the "AdminSubpages" subfolder
        csv_file_path = os.path.join(current_directory, "AdminSubpages", "example.csv")

        # Load the CSV file into a pandas DataFrame
        data = pd.read_csv(csv_file_path)


        # CSV data
        #csv_file = "example.csv"
        #csv_data = self.load_csv_data(csv_file)
        csv_data = pd.read_csv(csv_file_path)
        self.display_csv_data(end_plan_tree, csv_data)

        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=7, column=0, padx=5, pady=10)

        # Buttons
        end_event_btn = tk.Button(self.window, text="End Event", command=lambda: self.remove_selected_item(end_plan_tree, csv_file_path))
        end_event_btn.grid(row=8, column=0, padx=5, pady=10)


# do not use the following!!
    def load_csv_data(self, filename):
        data = pd.read_csv(filename)
        return data

    def display_csv_data(self, tree, data):
        tree.delete(*tree.get_children())
        tree['columns'] = list(data.columns)
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        for col in data.columns:
            tree.column(col, anchor=tk.CENTER, width=80)
            tree.heading(col, text=col, anchor=tk.CENTER)

        for index, row in data.iterrows():
            tree.insert("", tk.END, values=list(row), iid=str(index))

    def remove_selected_item(self, tree, filename):
        selected_item = tree.selection()
        if selected_item:
            # Get index of the selected row
            index = int(selected_item[0])

            # Load current CSV data, remove selected row, and save back to CSV
            data = self.load_csv_data(filename)
            data = data.drop(index)
            data.to_csv(filename, index=False)

            # Refresh the Treeview display
            self.display_csv_data(tree, data)

