def create_listbox_with_label(widget, text_label, num_rows, num_columns, item_list):
    tk.Label(widget, text=text_label).grid(row=num_rows, column=num_columns)

    scrollbar = tk.Scrollbar(widget)
    scrollbar.grid(row=num_rows, column=num_columns+2, sticky='ns')

    listbox = tk.Listbox(widget, yscrollcommand=scrollbar.set, height=1)
    listbox.grid(row=num_rows, column=num_columns+1)

    scrollbar.config(command=listbox.yview)

    for item in item_list:
        listbox.insert(tk.END, item)

    return listbox, scrollbar