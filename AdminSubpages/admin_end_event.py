import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AdminEndEvent:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main



    def create_gui_end_event(self, window):
        # Main frame for this whole page
        for i in self.window.winfo_children():
            i.grid_forget()
        end_plan_frame = tk.Frame(self.window)
        end_plan_frame.grid()

        # Labels
        end_plan_title = tk.Label(end_plan_frame, text="Admin End Plan", font=('Helvetica', 16))
        end_plan_title.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")




        #end_plan_tree = ttk.Treeview(end_plan_frame)
        #end_plan_tree.pack(expand=True, fill=tk.BOTH)



        # Back button
        back_button = tk.Button(self.window, text='Back to Home', command=self.back_button_to_admin_main)
        back_button.grid(row=17, column=1, padx=5, pady=10)

