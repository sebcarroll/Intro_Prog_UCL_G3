import csv
import os

def save_information_csv(data_to_add):
    file_name = 'camp_information.csv'
    columns = ['camp_id', 'no_refugees', 'no_weeks_aid', 'total_food_supplied', 'total_medicine_supplied',
           'week_food_per_refugee', 'week_medicine_per_refugee', 'delivery_time_weeks']

    if not os.path.isfile(file_name):
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            writer.writerows(data_to_add)
    else:

        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data_to_add)

    print(f"Data added to {file_name}.")