import tkinter as tk

def resource_display(window, back_button_to_volunteer_main):
    for i in window.winfo_children():
        i.grid_forget()
    resources_frame = tk.Frame(window)
    resources_frame.grid()

    # Title
    resources_title = tk.Label(resources_frame, text='Resources Currently Available', font=('tkDefault', 30))
    resources_title.grid(row=0, column=1)

    # Creating label frame
    resources_labelframe = tk.LabelFrame(resources_frame)
    resources_labelframe.grid(row=1, column=1)

    # Not sure what is meant to go in here at the moment so will just leave it for now.
    t_back_button = tk.Button(resources_frame, text='Back to Home', command=back_button_to_volunteer_main)
    t_back_button.grid(row=9, column=0, padx=5, pady=10)