import pandas as pd
import os

def save_information_csv(data_to_add):
    file_name = 'camp_information.csv'
    columns = ['camp_id', 'no_refugees', 'no_weeks_aid', 'total_food_supplied', 'total_medicine_supplied','week_food_per_refugee', 'week_medicine_per_refugee', 'delivery_time_weeks']

    dataframe_containing_new_data = pd.DataFrame([data_to_add], columns=columns)

    if os.path.isfile(file_name):
        dataframe_of_existing_data = pd.read_csv(file_name)

        dataframe_containing_new_data['camp_id'] = dataframe_containing_new_data['camp_id'].astype(int)
        dataframe_of_existing_data['camp_id'] = dataframe_of_existing_data['camp_id'].astype(int)

        merged_dataframe = pd.concat([dataframe_of_existing_data, dataframe_containing_new_data]).drop_duplicates(subset=['camp_id'], keep='last')

        merged_dataframe.to_csv(file_name, index=False)
    else:
        dataframe_containing_new_data.to_csv(file_name, index=False)

    print("save_information_csv successfully run.")
