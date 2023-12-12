import tkinter as tk

def personal_information(window, username, y_personal_info, t_personal_info_edit, back_button_to_volunteer_main):
    for i in window.winfo_children():
        i.grid_forget()


    t_personal_frame = tk.Frame(window)
    t_personal_frame.grid(row=0, column=0)
    t_personal_frame.grid(padx=(window.winfo_width() - t_personal_frame.winfo_reqwidth()) // 3)

    t_personal_labelframe = tk.LabelFrame(t_personal_frame)
    t_personal_labelframe.grid(row=3, column=0, padx=10, pady=30, columnspan=4)

    t_personal_title = tk.Label(t_personal_frame, text='Volunteer Details', font=('Arial Bold', 30))
    t_personal_title.grid(row=0, column=0, columnspan=4, pady=30)

    # Name label
    t_personal_namelabel = tk.Label(t_personal_labelframe, text='Name', font=('TkDefaultFont', 15))
    t_personal_namelabel.grid(row=4, column=0, pady=5)
    t_personal_name = tk.Label(t_personal_labelframe, text=y_personal_info[username]['name'],
                                    font=('TkDefaultFont', 15))
    t_personal_name.grid(row=4, column=1, pady=5)

    # Email label
    t_personal_emailabel = tk.Label(t_personal_labelframe, text='Email Address: ', font=('TkDefaultFont', 15))
    t_personal_emailabel.grid(row=6, column=0, pady=5)
    t_personal_email = tk.Label(t_personal_labelframe,
                                     text=y_personal_info[username]['Email Address'],
                                     font=('TkDefaultFont', 15))
    t_personal_email.grid(row=6, column=1, pady=5)

    # Phone label
    t_personal_phonenumberlabel = tk.Label(t_personal_labelframe, text='Phone number: ',
                                                font=('TkDefaultFont', 15))
    t_personal_phonenumberlabel.grid(row=8, column=0, pady=5)
    t_phonenumber = tk.Label(t_personal_labelframe, text=y_personal_info[username]['Phone Number'],
                                  font=('TkDefaultFont', 15))
    t_phonenumber.grid(row=8, column=1, pady=5)

    t_personal_commitmentlabel = tk.Label(t_personal_labelframe, text='Commitment: ',
                                               font=('TkDefaultFont', 15))
    t_personal_commitmentlabel.grid(row=10, column=0, pady=5)
    t_commitment = tk.Label(t_personal_labelframe, text=y_personal_info[username]['Commitment'],
                                 font=('TkDefaultFont', 15))
    t_commitment.grid(row=10, column=1, pady=5)

    t_personal_namelabel = tk.Label(t_personal_labelframe, text='Work type: ', font=('TkDefaultFont', 15))
    t_personal_namelabel.grid(row=12, column=0, pady=5)

    t_work_type_label = tk.Label(t_personal_labelframe, text=y_personal_info[username]['Work Type'],
                                      font=('TkDefaultFont', 15))
    t_work_type_label.grid(row=12, column=1, pady=5)

    # Store details button
    t_edit_details = tk.Button(t_personal_frame, text='Edit details', command=t_personal_info_edit,
                                    height=1, width=20)
    t_edit_details.grid(row=14, column=1, columnspan=2, pady=10, padx=10)

    back_to_summary = tk.Button(t_personal_frame, text='Back to Home', command=back_button_to_volunteer_main)
    back_to_summary.grid(row=17, column=1, columnspan=2, pady=10, padx=10)





