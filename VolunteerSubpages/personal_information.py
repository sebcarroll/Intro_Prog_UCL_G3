import tkinter as tk

def personal_information(window, username, y_personal_info, t_personal_info_edit, back_button_to_volunteer_main):
    for i in window.winfo_children():
        i.grid_forget()
    for i in range(9):
        window.grid_columnconfigure(i, weight=1)
    t_personal_frame = tk.Frame(window)
    t_personal_frame.grid(sticky="nsew", padx=5, pady=5, columnspan=9, rowspan=9)
    for i in range(9):
        t_personal_frame.grid_columnconfigure(i, weight=1)
    for i in range(8):
        t_personal_frame.grid_rowconfigure(i, weight=1)

    t_personal_title = tk.Label(t_personal_frame, text='Your Personal Details', font=('TKDefault', 25), fg='white')
    t_personal_title.grid(row=0, column=0, sticky="ew", pady=5, padx=5, columnspan=9)
    t_personal_title.configure(background="grey")

    t_personal_labelframe = tk.LabelFrame(t_personal_frame)
    t_personal_labelframe.grid(row=1, column=0, padx=10, pady=30, columnspan=9)

    # Name label
    t_personal_namelabel = tk.Label(t_personal_labelframe, text='Name', font=('TkDefaultFont', 15))
    t_personal_namelabel.grid(row=2, column=0, pady=5, padx=5)
    t_personal_name = tk.Label(t_personal_labelframe, text=y_personal_info[username]['name'],
                                    font=('TkDefaultFont', 15))
    t_personal_name.grid(row=2, column=1, pady=5, padx=5)

    # Email label
    t_personal_emailabel = tk.Label(t_personal_labelframe, text='Email Address: ', font=('TkDefaultFont', 15))
    t_personal_emailabel.grid(row=3, column=0, pady=5, padx=5)
    t_personal_email = tk.Label(t_personal_labelframe,
                                     text=y_personal_info[username]['Email Address'],
                                     font=('TkDefaultFont', 15))
    t_personal_email.grid(row=3, column=1, pady=5, padx=5)

    # Phone label
    t_personal_phonenumberlabel = tk.Label(t_personal_labelframe, text='Phone number: ',
                                                font=('TkDefaultFont', 15))
    t_personal_phonenumberlabel.grid(row=4, column=0, pady=5, padx=5)
    t_phonenumber = tk.Label(t_personal_labelframe, text=str(y_personal_info[username]['Phone Number']),
                                  font=('TkDefaultFont', 15))
    t_phonenumber.grid(row=4, column=1, pady=5, padx=5)

    t_personal_commitmentlabel = tk.Label(t_personal_labelframe, text='Commitment: ',
                                               font=('TkDefaultFont', 15))
    t_personal_commitmentlabel.grid(row=5, column=0, pady=5, padx=5)
    t_commitment = tk.Label(t_personal_labelframe, text=y_personal_info[username]['Commitment'],
                                 font=('TkDefaultFont', 15))
    t_commitment.grid(row=5, column=1, pady=5, padx=5)

    t_personal_namelabel = tk.Label(t_personal_labelframe, text='Work type: ', font=('TkDefaultFont', 15))
    t_personal_namelabel.grid(row=6, column=0, pady=5, padx=5)

    t_work_type_label = tk.Label(t_personal_labelframe, text=y_personal_info[username]['Work Type'],
                                      font=('TkDefaultFont', 15))
    t_work_type_label.grid(row=6, column=1, pady=5, padx=5)

    # Button Frame:
    btn_frame = tk.Frame(t_personal_frame)
    btn_frame.grid(row=2, column=4, pady=10)
    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(2, weight=1)

    # Store details button
    t_edit_details = tk.Button(btn_frame, text='Edit details', command=t_personal_info_edit,
                                    height=1, width=20)
    t_edit_details.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    back_to_summary = tk.Button(btn_frame, text='Back to Home', command=back_button_to_volunteer_main)
    back_to_summary.grid(row=1, column=0, columnspan=2, pady=10, padx=10)






