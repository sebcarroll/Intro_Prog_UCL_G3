import tkinter as tk
import csv
import os
import pandas as pd
from tkinter import PhotoImage, messagebox

class EmptyDataError(Exception):
    pass

class CountryMap:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main
        self.map_image = None


    def view_country_map_window(self):
        self.map_window = tk.Toplevel(self.window)
        self.map_window.title("View Crisis Map")
        self.map_window.geometry("1000x500")
        #self.map_window.configure(bg='black')
        # THIS SETS THE WINDOW FIXED SIZE!
        self.map_window.resizable(False, False)
        self.map_window.grab_set()

        # Call create gui function to create the map in the new level window
        self.show_map(self.map_window)


    def show_map(self, window):
        # Create a canvas for the map image
        map_canvas = tk.Canvas(window, width=1000, height=800)
        map_canvas.place(x=0, y=0)
        try:
            if self.map_image is None:
                self.map_image = PhotoImage(file="Images/dark_map.png")
        except:
            messagebox.showerror("No image found",
                                   "There is a problem accessing the database\n\nThe file may be missing or corrupted")
            self.map_image = None

        map_canvas.create_image(0, 0, anchor=tk.NW, image=self.map_image)

        # Coordinates for each country
        country_coordinates = {
            'Nigeria': [480, 280],
            'Sudan': [550, 260],
            'South Sudan': [550, 280],
            'Somalia': [585, 290],
            'Yemen': [580, 260],
            'Afghanistan': [640, 230],
            'England': [455, 165],
            'Syria': [570, 215],
            'Democratic Republic of the Congo': [520, 310],
            'Venezuela': [290, 310],
            'Iraq': [580, 230],
            'Ethiopia': [570, 280],
            'Myanmar': [710, 260],
            'Haiti': [290, 270],
            'Central African Republic': [550, 315],
            'Libya': [500, 240],
            'Chad': [500, 275],
            'Mali': [450, 280],
            'Cameroon': [520, 320],
            'Ukraine': [570, 190],
            'Pakistan': [660, 240],
            'Bangladesh': [700, 245],
            'Lebanon': [555, 210],
            'Zimbabwe': [540, 360],
            'Eritrea': [660, 300],
            'North Korea': [790, 200],
            'Eswatini': [550, 380],
            'Zambia': [520, 330],
            'Malawi': [550, 335],
        }

        # Locations from csv file
        locations = self.read_location_data_from_csv('crisis_events.csv')
        #print("loading locations", locations)

        # Track the count for each country
        country_counts = {country: 0 for country in country_coordinates}

        for location in locations:
            country = location["country"]
            if country in country_coordinates:
                coordinates = country_coordinates[country]

                # Increase the count for the country
                country_counts[country] += 1

                # Adjust oval size based on count
                oval_size = 3 + country_counts[country]

                # Draw the oval with adjusted size
                map_canvas.create_oval(
                    coordinates[0] - oval_size,
                    coordinates[1] - oval_size,
                    coordinates[0] + oval_size,
                    coordinates[1] + oval_size,
                    fill='red'
                )

                # Adjust font size based on the count (scaled down)
                font_size = int(10 - country_counts[country] * 0.2)

                map_canvas.create_text(coordinates[0], coordinates[1] - 10, text=country, anchor=tk.CENTER,
                                       fill='white', font=("Helvetica", font_size))


    def read_location_data_from_csv(self, crisis_events):
        try:
            data = pd.read_csv(crisis_events)
            locations = []
            for index, row in data.iterrows():
                # x and y are columns in the csv
                country = row['Country']
                crisis_type = row['Crisis Type']
                if pd.notna(country) and pd.notna(crisis_type):
                    locations.append({'country': country, 'crisis_type': crisis_type})
            return locations
        except FileNotFoundError:
            # Handle the case where the file is not found
            messagebox.showerror("File not found",
                                "The file 'crisis_events.csv' was not found."
                                )
            #print(f"Error: File '{crisis_events}' not found.")
            self.map_window.destroy()
            return []
        except pd.errors.EmptyDataError:
            # Handle the case where the file is empty
            messagebox.showinfo("No Data",
                                "The file 'crisis_events.csv' contains no data."
                                "\n\nPlease create a plan first.")
            print(f"Error: File '{crisis_events}' is empty.")
            return []
        except Exception as e:
            # Handle other exceptions
            messagebox.showerror("Error",
                                "Something went wrong.")
            #print(f"Error: An unexpected error occurred - {e}")
            return []

scale_factor = 0.5
