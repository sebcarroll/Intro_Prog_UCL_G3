import tkinter as tk
import csv
from tkinter import messagebox
import os
import pandas as pd

class NoDataError(Exception):
    pass
class SummaryCharts:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main


    def generate_charts_window(self):
        self.charts_window = tk.Toplevel(self.window)
        self.charts_window.title("View Charts")
        self.charts_window.geometry("800x400")

        self.charts_window.grab_set()

        # Call create gui functions to create the pie charts in the new window
        try:
            self.create_pie_chart_status(self.charts_window)
            self.create_bar_chart_crisis_type(self.charts_window)
        except NoDataError as e:
            messagebox.showerror("Error", f"Error: {e}")
            #print(f"Error: {e}")
    def create_pie_chart_status(self, window):
        active_count = 0
        inactive_count = 0

        with open('crisis_events.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                status = row['Status']
                if status.lower() == 'active':
                    active_count += 1
                elif status.lower() == 'inactive':
                    inactive_count += 1
        if active_count == 0 and inactive_count == 0:
            raise NoDataError("No data available in the CSV file for pie chart.")


        # Calculate percentage or ratio between the inactive and active plans
        total = active_count + inactive_count
        active_percentage = (active_count / total) * 360
        inactive_percentage = (inactive_count / total) * 360

        # Create pie chart using canvas
        canvas = tk.Canvas(window, width=200, height=200)
        # canvas.grid(row=17, column=0, padx=10, pady=5)
        canvas.pack()

        # Create canvas for pie chart labels
        canvas_legend_pie = tk.Canvas(window, width=200, height=200)
        canvas_legend_pie.place(x=50 ,y=75)

        # Active slice
        canvas.create_arc(50, 50, 150, 150, start=0, extent=active_percentage, fill='green', outline='white')
        # Inactive slice
        canvas.create_arc(50, 50, 150, 150, start=active_percentage, extent=inactive_percentage, fill='red',
                          outline='white')

        # Add colour legend
        legend_labels_crisis_status = ['Active Crisis', 'Inactive Crisis']
        legend_colors_crisis_status = ['green', 'red']

        for i, label in enumerate(legend_labels_crisis_status):
            # Draw legend rectangle
            canvas_legend_pie.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=legend_colors_crisis_status[i], outline='white')
            # Draw legend label
            canvas_legend_pie.create_text(40, 20 + i * 20, text=label, anchor=tk.W, fill='black')

    def create_bar_chart_crisis_type(self, window):
        war_count = 0
        environmental_count = 0
        supply_shortage_count = 0
        political_unrest_count = 0
        displacement_count = 0
        other_count = 0

        with open('crisis_events.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                status = row['Crisis Type']
                if status.lower() == 'war':
                    war_count += 1
                elif status.lower() == 'environmental':
                    environmental_count += 1
                elif status.lower() == 'political unrest':
                    political_unrest_count += 1
                elif status.lower() == 'displacement':
                    displacement_count += 1
                elif status.lower() == 'supply shortage':
                    supply_shortage_count += 1
                elif status.lower() == 'other':
                    other_count += 1

        if war_count == 0 and environmental_count == 0 and supply_shortage_count == 0 \
                and political_unrest_count == 0 and displacement_count == 0 and other_count == 0:
            raise NoDataError("No data available in the CSV file for bar chart.")

        # Calculate total count
        total = war_count + environmental_count + supply_shortage_count + political_unrest_count + displacement_count + other_count


        # # Calculate percentage
        # total = war_count + environmental_count + supply_shortage_count + political_unrest_count + displacement_count + other_count
        # war_percentage = (war_count / total) * 360
        # environmental_percentage = (environmental_count / total) * 360
        # supply_shortage_percentage = (supply_shortage_count / total) * 360
        # political_unrest_percentage = (political_unrest_count / total) * 360
        # displacement_percentage = (displacement_count / total) * 360
        # other_percentage = (other_count / total) * 360

        # Create a bar chart using canvas
        canvas = tk.Canvas(window, width=400, height=200)
        canvas.pack()

        # Create a canvas for the bar chart labels
        canvas_legend_bar = tk.Canvas(window, width=200, height=200)
        canvas_legend_bar.place(x=50 ,y=225)

        # Define bar width and gap
        bar_width = 40
        gap = 20

        # Calculate the x-coordinates for each bar
        x_war = 50
        x_environmental = x_war + bar_width + gap
        x_supply_shortage = x_environmental + bar_width + gap
        x_political_unrest = x_supply_shortage + bar_width + gap
        x_displacement = x_political_unrest + bar_width + gap
        x_other = x_displacement + bar_width + gap

        # Calculate the heights of each bar
        height_factor = 100
        height_war = war_count * height_factor / total
        height_environmental = environmental_count * height_factor / total
        height_supply_shortage = supply_shortage_count * height_factor / total
        height_political_unrest = political_unrest_count * height_factor / total
        height_displacement = displacement_count * height_factor / total
        height_other = other_count * height_factor / total

        # Draw rectangle shape for each bar
        canvas.create_rectangle(x_war, 150 - height_war, x_war + bar_width, 150, fill='red', outline='white')
        canvas.create_rectangle(x_environmental, 150 - height_environmental, x_environmental + bar_width, 150, fill='blue', outline='white')
        canvas.create_rectangle(x_supply_shortage, 150 - height_supply_shortage, x_supply_shortage + bar_width, 150, fill='green', outline='white')
        canvas.create_rectangle(x_political_unrest, 150 - height_political_unrest, x_political_unrest + bar_width, 150, fill='yellow', outline='white')
        canvas.create_rectangle(x_displacement, 150 - height_displacement, x_displacement + bar_width, 150, fill='purple', outline='white')
        canvas.create_rectangle(x_other, 150 - height_other, x_other + bar_width, 150, fill='orange', outline='white')

        # # Draw slices of the pie chart
        # canvas.create_arc(50, 50, 150, 150, start=0, extent=war_percentage, fill='red', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage, extent=environmental_percentage, fill='blue', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage, extent=supply_shortage_percentage, fill='green', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage, extent=political_unrest_percentage, fill='yellow', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage + political_unrest_percentage, extent=displacement_percentage, fill='purple', outline='white')
        # canvas.create_arc(50, 50, 150, 150, start=war_percentage + environmental_percentage + supply_shortage_percentage + political_unrest_percentage + displacement_percentage, extent=other_percentage, fill='orange', outline='white')

        # Add legend (key)
        legend_labels_crisis_type = ['War', 'Environmental', 'Supply Shortage', 'Political Unrest', 'Displacement', 'Other']
        legend_colors_crisis_type = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

        for i, label in enumerate(legend_labels_crisis_type):
            # Draw legend rectangle
            canvas_legend_bar.create_rectangle(10, 10 + i * 20, 30, 30 + i * 20, fill=legend_colors_crisis_type[i], outline='white')
            # Draw legend label
            canvas_legend_bar.create_text(40, 20 + i * 20, text=label, anchor=tk.W, fill='black')


