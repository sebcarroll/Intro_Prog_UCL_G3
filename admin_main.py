import tkinter as tk


class AdminHomepage:
    def __init__(self, root, go_to_landing_page):
        self.root = root
        self.go_to_landing_page = go_to_landing_page
        self.window = tk.Toplevel(self.root)
        self.window.title('Admin Homepage')
        self.window.geometry('1300x600')

        # MENU BAR:
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)
        # create a menu item 1
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Plan", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Log Out", command=self.exit_and_go_back)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_software)
        # create a menu item 2
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=file_menu)
        file_menu.add_command(label="Edit Event", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Resources", command=self.our_cmd)
        # create a menu item 3
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=file_menu)
        file_menu.add_command(label="View Events", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="View Summaries", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Allocate Resources", command=self.our_cmd)
        # create a menu item 4
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Accounts", menu=file_menu)
        file_menu.add_command(label="Create", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Volunteers", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Admins", command=self.our_cmd)
        # create a menu item 5
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_command(label="Display", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="Audio", command=self.our_cmd)
        # create a menu item 6
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=file_menu)
        file_menu.add_command(label="Contact Support", command=self.our_cmd)
        file_menu.add_separator()
        file_menu.add_command(label="About", command=self.our_cmd)

        self.admin_welcome_title = tk.Label(self.window, text='Welcome to the Admin portal', font=('Arial Bold', 40))
        self.admin_welcome_title.grid(row=0, column=3, pady=30)

        # MAIN BUTTONS
        # Create new event button
        self.btn_create_event = tk.Button(self.window, text="Create new event", command=self.create_event)
        self.btn_create_event.grid(row=3, column=3, pady=5)

        # End an event button
        self.btn_end_event = tk.Button(self.window, text="End an event", command=self.end_event)
        self.btn_end_event.grid(row=5, column=3, pady=5)

        # View summaries button
        self.btn_view_summaries = tk.Button(self.window, text="View Summaries", command=self.view_summaries)
        self.btn_view_summaries.grid(row=7, column=3, pady=5)

        # Edit volunteer accounts button
        self.btn_edit_accounts = tk.Button(self.window, text="Edit volunteer accounts", command=self.edit_accounts)
        self.btn_edit_accounts.grid(row=9, column=3, pady=5)

        # Allocate resources button
        self.btn_allocate_resources = tk.Button(self.window, text="Allocate resources", command=self.allocate_resources)
        self.btn_allocate_resources.grid(row=11, column=3, pady=5)




    def create_event(self):
        # Open the resource allocation GUI
        print("Create event...")
        #new_window = tk.Toplevel()
        #apcg.create_plan_gui(new_window)

    def end_event(self):
        # Add functionality for ending an event
        print("Ending an event...")
        # Implement the function's logic here

    def view_summaries(self):
        # Add functionality for viewing summaries
        print("Viewing summaries...")
        # Implement the function's logic here

    def edit_accounts(self):
        # Add functionality for editing volunteer accounts
        print("Editing volunteer accounts...")
        # Implement the function's logic here

    def allocate_resources(self):
        # Open the resource allocation GUI
        for i in self.window.winfo_children():
            i.grid_forget()
        self.resources_frame = tk.Frame(self.window)
        self.resources_frame.grid()

        # import modules locally to this function only
        from tkinter import ttk, Listbox
        from general_functions import create_listbox_with_label

        # Title for the page
        self.resources_title = tk.Label(self.resources_frame, text='Allocate Resources', font=('tkDefault', 20))
        self.resources_title.grid(row=0, column=0, pady=10)



        # Comes from list of IDs created by admin in camp creation
        camp_ids = ["Camp_1", "Camp_2", "Camp_3", "Camp_4"]
        camp_id_listbox: Listbox
        camp_id_listbox, camp_id_scrollbar = create_listbox_with_label(self.resources_frame, "Camp ID:", 5, 0, camp_ids)

        tk.Label(self.resources_frame, text="Number of Weeks of Aid:").grid(row=11, column=0)
        no_weeks_aid_entry = tk.Entry(self.resources_frame)
        no_weeks_aid_entry.grid(row=11, column=1)

        tk.Label(self.resources_frame, text="Total Food Supplied to Camp:").grid(row=12, column=0)
        total_food_supplied_entry = tk.Entry(self.resources_frame)
        total_food_supplied_entry.grid(row=12, column=1)

        tk.Label(self.resources_frame, text="Total Medicine Supplied to Camp:").grid(row=13, column=0)
        total_medicine_supplied_entry = tk.Entry(self.resources_frame)
        total_medicine_supplied_entry.grid(row=13, column=1)

        # This will eventually come from the number of refugees stored with the camp_id
        tk.Label(self.resources_frame, text="Number of Refugees:").grid(row=14, column=0)
        no_refugees_entry = tk.Entry(self.resources_frame)
        no_refugees_entry.grid(row=14, column=1)

        food_amount_refugee = [7, 14, 21, 28]
        food_amount_refugee_listbox, food_amount_refugee_scrollbar = create_listbox_with_label(self.resources_frame,"Number of Weekly Meals Provided per Refugee: ",16, 0, food_amount_refugee)

        medicine_amount_refugee = [0, 1, 2, 3, 4, 5, 6, 7]
        medicine_amount_refugee_listbox, medicine_amount_refugee_scrollbar = create_listbox_with_label(self.resources_frame,"Number of Health Supplies Provided per Refugee Weekly: ",17, 0, medicine_amount_refugee)

        estimated_delivery_time_options = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
        estimated_delivery_time_listbox, estimated_delivery_time_scrollbar = create_listbox_with_label(self.resources_frame,"Estimated Resource Delivery Time (weeks): ",18, 0, estimated_delivery_time_options)

        """message_label = tk.Label(window, text="")
        submit_button_row = 8
        submit_button_column = 0
        submit_column_span = 2"""
        self.back_button = ttk.Button(self.resources_frame, text='Back to Home', command=self.back_button_to_admin_main)
        self.back_button.grid(row=20, column=0, columnspan=1)
        submit_button = ttk.Button(self.resources_frame, text="Submit", command=self.admin_resource_submit)
        submit_button.grid(row=20, column=1, columnspan=1)

    # CGH: I am yet to look at this submit function

    def admin_resource_submit():"""
        # import modules locally to this function only
        from general_functions import check_input_valid
        from general_functions import get_selected_listbox_value

        camp_id = get_selected_listbox_value(camp_id_listbox)
        check_input_valid(camp_id, window, message_label, submit_button_row, submit_button_column, submit_column_span)

        no_weeks_aid = no_weeks_aid_entry.get()
        check_input_valid(no_weeks_aid, window, message_label, submit_button_row, submit_button_column,
                          submit_column_span)

        total_food_supplied = total_food_supplied_entry.get()
        check_input_valid(total_food_supplied, window, message_label, submit_button_row, submit_button_column,
                          submit_column_span)

        total_medicine_supplied = total_medicine_supplied_entry.get()
        check_input_valid(total_medicine_supplied, window, message_label, submit_button_row, submit_button_column,
                          submit_column_span)

        no_refugees = no_refugees_entry.get()  # Will need to come from the volunteer.
        check_input_valid(no_refugees, window, message_label, submit_button_row, submit_button_column,
                          submit_column_span)

        week_food_per_refugee = get_selected_listbox_value(food_amount_refugee_listbox)
        check_input_valid(week_food_per_refugee, window, message_label, submit_button_row, submit_button_column,
                          submit_column_span)

        week_medicine_per_refugee = get_selected_listbox_value(medicine_amount_refugee_listbox)
        check_input_valid(week_medicine_per_refugee, window, message_label, submit_button_row, submit_button_column,
                          submit_column_span)

        delivery_time_weeks = get_selected_listbox_value(estimated_delivery_time_listbox)
        check_input_valid(delivery_time_weeks, window, message_label, submit_button_row, submit_button_column,
                          submit_column_span)"""







    def back_button_to_admin_main(self):
        # Clear current contents
        for widget in self.window.winfo_children():
            widget.grid_forget()
        # Repopulate main page
        self.admin_welcome_title.grid(row=0, column=3, pady=30)
        self.btn_create_event.grid(row=3, column=3, pady=5)
        # End an event button
        self.btn_end_event.grid(row=5, column=3, pady=5)
        # View summaries button
        self.btn_view_summaries.grid(row=7, column=3, pady=5)
        # Edit volunteer accounts button
        self.btn_edit_accounts.grid(row=9, column=3, pady=5)
        # Allocate resources button
        self.btn_allocate_resources.grid(row=11, column=3, pady=5)

    def our_cmd(self):
        pass

    def exit_and_go_back(self):
        self.window.destroy()
        self.go_to_landing_page()

    def exit_software(self):
        self.root.quit()

    def destroy(self):
        self.window.destroy()



