import tkinter
import pickle
import re
import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class file_not_found(Exception):
     pass

class refugee_stuff:

    def __init__(self):
        self.window = tkinter.Frame()
        self.window.pack()
        self.y_camp_info = {"Country": "America", "Max Capacity": ""}
        try:
            if os.path.getsize('Camp.pickle') > 0:
                with open('Camp.pickle', 'rb') as f:
                    self.y_camp_info = pickle.load(f)
            else:
                self.y_camp_info['ID'] = {"Country": "America 132", "Max Capacity": 1000, 'Food packets': 0, 'Medical supplies': 0, 'Water and sanitation': 0, 'Clothing': 0, 'Shelter materials': 0}
        except(FileNotFoundError):
            self.y_camp_info['ID'] = {"Country": "America 132", "Max Capacity": 1000, 'Food packets': 0, 'Medical supplies': 0, 'Water and sanitation': 0, 'Clothing': 0, 'Shelter materials': 0}
        print(self.y_camp_info)
        self.t_edit_camp()


    def t_refugee_dict(self):
        try:
            with open('Camp.pickle', 'wb') as f:
                refugee_change = self.t_camp_campacitybox.get()
                refugee_capacity = self.y_camp_info['ID']['Max Capacity']
                refugee_capacity -= int(refugee_change)
                request_resources_type = self.n_resource_typebox.get()
                request_resources_quant = self.n_resource_quantbox.get()
                current_resources = self.y_camp_info['ID'][request_resources_type]
                current_resources += int(request_resources_quant)
                self.y_camp_info['ID']['Max Capacity'] = refugee_capacity
                self.y_camp_info['ID'][request_resources_type] = current_resources
                pickle.dump(self.y_camp_info, f)
        except:
            raise file_not_found


    def t_edit_camp(self):
            for i in self.window.winfo_children():
                i.destroy()
            t_edit_campframe = tkinter.Frame(self.window)
            t_edit_campframe.pack()
            t_edit_camp_title = tkinter.Label(t_edit_campframe, text='Edit camp', font=('TkDefaultFont', 30), pady=30)
            t_edit_camp_title.grid(row=0, column=1)
            t_camp_labelframe = tkinter.LabelFrame(t_edit_campframe, text=self.y_camp_info['ID']['Country'], font=('TkDefaultFont', 20))
            t_camp_labelframe.grid(row=1, column=1)

            # Current amount you can add
            t_current_capacity = tkinter.Label(t_camp_labelframe, text='Current Capacity: ', font=('TkDefaultFont', 15))
            t_current_capacity.grid(row=2, column= 3)
            t_capacity_label = tkinter.Label(t_camp_labelframe, text= self.y_camp_info['ID']['Max Capacity'], font=('TkDefaultFont', 15))
            t_capacity_label.grid(row=2, column= 5)

            # Capacity for new refugees box and label
            t_camp_capacity = tkinter.Label(t_camp_labelframe,
                                            text='Add new refugees:')  # Need to add current number here next to it so Ying add that in with dictionary or however.
            t_camp_capacity.grid(row=4, column=3, padx=5)
            self.t_camp_campacitybox = ttk.Spinbox(t_camp_labelframe, from_=0, to=1000, style='info.TSpinbox')
            self.t_camp_campacitybox.grid(row=4, column=5, padx=5)

            # Request type of resource box and label
            n_resource_type = tkinter.Label(t_camp_labelframe, text='Select resource type you would like to request')
            n_resource_type.grid(row=5, column=3, padx=5)
            self.n_resource_typebox = ttk.Combobox(t_camp_labelframe, values=['Food packets', 'Medical supplies', 'Water and sanitation', 'Clothing', 'Shelter materials'])
            self.n_resource_typebox.grid(row=5, column=5, padx=5)

            # Request quantity of resource box and label
            n_resource_quantity = tkinter.Label(t_camp_labelframe, text='Select quantity of resource')
            n_resource_quantity.grid(row=6, column=3, padx=5)
            self.n_resource_quantbox = ttk.Spinbox(t_camp_labelframe, from_=0, to=1000)
            self.n_resource_quantbox.grid(row=6, column=5, padx=5)

             # Save changes button, need to add this to a dictionary.
            t_save_changes = tkinter.Button(t_edit_campframe, text='Save changes', command= self.t_refugee_dict)
            t_save_changes.grid(row=7, column=1, padx=5, pady=10)

            self.window.mainloop()

refugee_stuff()