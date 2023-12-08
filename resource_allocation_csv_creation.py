import csv

def update_crisis_events(camp_id, no_refugees, no_weeks_aid, total_food_supplied, total_medicine_supplied,
             week_food_per_refugee, week_medicine_per_refugee, delivery_time_weeks):
    try:
        with open('crisis_events.csv', 'r') as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        for row in data:
            if row[0] == camp_id:
                row[8] = no_refugees
                row[9] = no_weeks_aid
                row[10] = total_food_supplied
                row[11] = total_medicine_supplied
                row[12] = week_food_per_refugee
                row[13] = week_medicine_per_refugee
                row[14] = delivery_time_weeks
                break

        with open('crisis_events.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    except FileNotFoundError:
        print("Error: 'crisis_events.csv' file not found.")
