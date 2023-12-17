import csv
from tkinter import messagebox

def update_crisis_events(camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks):
    try:
        with open('crisis_events.csv', 'r') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        for row in data:
            if row[0] == camp_id:
                row[9] = no_refugees
                row[10] = no_weeks_aid
                row[11] = total_food_supplied
                row[12] = total_medicine_supplied
                row[13] = week_food_per_refugee
                row[14] = week_medicine_per_refugee
                row[15] = delivery_time_weeks
                break

        with open('crisis_events.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    except FileNotFoundError:
        messagebox.showinfo("File not found",
                            "The file 'crisis_events.csv' was not found.\n\nYou will not be able to change to another camp ID")
        print("Error: 'crisis_events.csv' file not found.")
