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
        self.map_window.geometry("1000x800")

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

        # # Load the image using PhotoImage
        # map_image = PhotoImage(file="AdminSubpages/world_map_tkinter.png")  # Replace with the path to your image file
        #
        # map_label = tk.Label(window, image=map_image)
        # map_label.pack()

        # print("Loading image...")
        # photo = PhotoImage(file="world_map_tkinter.png")
        # print("Image loaded.")
        # label = tk.Label(window, image=photo)
        #
        # label.pack()

        # Define coordinates for each country
        country_coordinates = {
            'Nigeria': [150, 150],
            'Sudan': [150, 200],
            'South Sudan': [100, 200],
            'Somalia': [100, 250],
            'Yemen': [150, 300],
            'Afghanistan': [200, 350],
            'England': [200, 400],
            'Syria': [200, 450],
            'Democratic Republic of the Congo': [150, 500],
            'Venezuela': [250, 550],
            'Iraq': [250, 600],
            'Ethiopia': [150, 650],
            'Myanmar': [200, 700],
            'Haiti': [250, 750],
            'Central African Republic': [150, 800],
            'Libya': [200, 850],
            'Chad': [150, 900],
            'Mali': [150, 950],
            'Niger': [150, 1000],
            'Cameroon': [150, 1050],
            'Ukraine': [300, 1100],
            'Pakistan': [300, 1150],
            'Bangladesh': [350, 1200],
            'Lebanon': [200, 1250],
            'Zimbabwe': [200, 1300],
            'Eritrea': [100, 1350],
            'North Korea': [350, 1400],
            'Eswatini': [200, 1450],
            'Zambia': [200, 1500],
            'Malawi': [400, 900],
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
