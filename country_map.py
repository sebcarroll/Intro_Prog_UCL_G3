import tkinter as tk
import csv
import os
import pandas as pd
from tkinter import PhotoImage

class CountryMap:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main
        self.map_image = None


    def view_country_map_window(self):
        # Create a new window for the map
        self.map_window = tk.Toplevel(self.window)
        self.map_window.title("View Crisis Map")
        self.map_window.geometry("1000x500")

        self.map_window.grab_set()

        # Call the method to create the pie chart in the new window
        self.show_map(self.map_window)


    def show_map(self, window):

        # Create a canvas for the map
        map_canvas = tk.Canvas(window, width=1000, height=800)  # Adjust the canvas size as needed
        map_canvas.place(x=0, y=0)  # Adjust the x and y coordinates as needed

        # Load the image using PhotoImage
        if self.map_image is None:
            self.map_image = PhotoImage(file="world_map_tkinter.png")

        # Display the image on the canvas
        map_canvas.create_image(0, 0, anchor=tk.NW, image=self.map_image)

        # Define coordinates for each country
        country_coordinates = {
            'Nigeria': [450, 350],
            'Sudan': [500, 300],
            'South Sudan': [550, 300],
            'Somalia': [600, 350],
            'Yemen': [500, 400],
            'Afghanistan': [600, 250],
            'England': [450, 200],
            'Syria': [500, 150],
            'Democratic Republic of the Congo': [450, 300],
            'Venezuela': [700, 150],
            'Iraq': [600, 150],
            'Ethiopia': [550, 350],
            'Myanmar': [600, 500],
            'Haiti': [750, 150],
            'Central African Republic': [550, 300],
            'Libya': [500, 150],
            'Chad': [500, 250],
            'Mali': [550, 300],
            'Niger': [600, 300],
            'Cameroon': [550, 350],
            'Ukraine': [750, 50],
            'Pakistan': [800, 100],
            'Bangladesh': [850, 150],
            'Lebanon': [700, 150],
            'Zimbabwe': [550, 400],
            'Eritrea': [600, 400],
            'North Korea': [850, 200],
            'Eswatini': [550, 450],
            'Zambia': [600, 400],
            'Malawi': [700, 350],
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

                map_canvas.create_text(coordinates[0], coordinates[1] - 10, text=country, anchor=tk.CENTER, fill='white')


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

scale_factor = 1
