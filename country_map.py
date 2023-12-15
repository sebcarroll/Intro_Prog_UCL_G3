import tkinter as tk
import csv
import os
import pandas as pd

class CountryMap:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main


    def view_country_map_window(self):
        # Create a new window for the map
        self.map_window = tk.Toplevel(self.window)
        self.map_window.title("View Charts & Map")
        self.map_window.geometry("800x800")

        self.map_window.grab_set()

        # Call the method to create the pie chart in the new window
        self.show_map(self.map_window)


    def show_map(self, window):

        # Create a canvas for the map
        map_canvas = tk.Canvas(window, width=800, height=600)
        map_canvas.place(x=400, y=400)

        # Create a label for the map
        map_label = tk.Label(window, text="Country Crisis View", font=('Helvetica', 15, 'bold'))
        map_label.place(x=400, y=425)  # Adjust the x and y coordinates as needed

        # Define coordinates for each country
        country_coordinates = {
            'Nigeria': [100, 100],
            'Sudan': [100, 150],
            'South Sudan': [100, 200],
            'Somalia': [100, 250],
            'Yemen': [150, 250],
            'Afghanistan': [200, 100],
            'England': [200, 150],
            'Syria': [200, 200],
            'Democratic Republic of the Congo': [150, 200],
            'Venezuela': [250, 100],
            'Iraq': [250, 150],
            'Ethiopia': [150, 250],
            'Myanmar': [200, 250],
            'Haiti': [250, 200],
            'Central African Republic': [150, 300],
            'Libya': [200, 250],
            'Chad': [150, 300],
            'Mali': [150, 250],
            'Niger': [150, 300],
            'Cameroon': [150, 300],
            'Ukraine': [300, 100],
            'Pakistan': [300, 150],
            'Bangladesh': [350, 200],
            'Lebanon': [200, 200],
            'Zimbabwe': [200, 300],
            'Eritrea': [100, 200],
            'North Korea': [350, 150],
            'Eswatini': [200, 300],
            'Zambia': [200, 250],
            'Malawi': [200, 300],
        }



        # Read locations from CSV file
        locations = self.read_location_data_from_csv('crisis_events.csv')
        print("loading locations", locations)

        # Track the count for each country
        country_counts = {country: 0 for country in country_coordinates}

        for location in locations:
            country = location["country"]
            if country in country_coordinates:
                coordinates = country_coordinates[country]

                # Increase the count for the country
                country_counts[country] += 1

                # Adjust the oval size based on the count
                oval_size = 5 + country_counts[country]

                # Draw the oval with adjusted size
                map_canvas.create_oval(
                    coordinates[0] - oval_size,
                    coordinates[1] - oval_size,
                    coordinates[0] + oval_size,
                    coordinates[1] + oval_size,
                    fill='red'
                )

                map_canvas.create_text(coordinates[0], coordinates[1] - 10, text=country, anchor=tk.CENTER)


    def read_location_data_from_csv(self, crisis_events):
        data = pd.read_csv(crisis_events)
        locations = []
        for index, row in data.iterrows():
            # x and y are columns in the csv
            country = row['Country']
            crisis_type = row['Crisis Type']
            if pd.notna(country) and pd.notna(crisis_type):
                locations.append({'country': country, 'crisis_type': crisis_type})
        return locations
