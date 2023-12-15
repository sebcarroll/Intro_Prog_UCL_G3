import tkinter as tk


class AdminHelp:
    def __init__(self, window, back_button_to_admin_main):
        self.window = window
        self.back_button_to_admin_main = back_button_to_admin_main

    def about_pop_up(self):
        about_window = tk.Toplevel(self.window)
        about_window.title("About")
        about_window.geometry("400x550")

        about_title = tk.Label(about_window, text="About", font=('Helvetica', 16))
        about_title.pack()

        about_frame = tk.Frame(about_window, relief=tk.RAISED, borderwidth=2)
        about_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        about_text = (
            "During wars, people flee their homes to more secure camps where they can receive medical"
            "assistance, food, and shelter.To distribute resources equally, humanitarian agencies need to"
            "record the number of refugees and their needs at every available camp.\n\n"
        
            "This application is designed to aid in organizing humanitarian crises, "
            "focusing on providing assistance to refugees and efficiently assigning resources to their camps. "
            "It serves as a management tool to coordinate efforts, track resources, and ensure "
            "that aid reaches those in need effectively. The application allows for real-time "
            "tracking of crises, resource allocation, and volunteer management, making it a "
            "vital tool in humanitarian response and support."
        )

        label_widget = tk.Label(about_frame, text=about_text, wraplength=350, justify=tk.LEFT)
        label_widget.pack(padx=5, pady=5)

        # Close button
        close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
        close_button.pack(pady=10)

    def info_pop_up(self):
        info_window = tk.Toplevel(self.window)
        info_window.title("Information")
        info_window.geometry("470x630")

        about_title = tk.Label(info_window, text="Information", font=('Helvetica', 16))
        about_title.pack()

        about_frame = tk.Frame(info_window, relief=tk.RAISED, borderwidth=2)
        about_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        about_text = (
            "(A) The general application admin can:\n\n" \
            "a. Create new humanitarian plans. Humanitarian plans recorded in the\n" \
            "   system require a description, the geographical location affected, the start\n" \
            "   date of the event.\n" \
            "b. End an event. To end an event, an end date must be added, and the\n" \
            "   humanitarian plan must be closed in the system.\n" \
            "c. Display humanitarian plan from the system. At any time of the\n" \
            "   humanitarian plan life cycle, the administrator can display summary of\n" \
            "   all related details; including, number of refugees, their camp\n" \
            "   identification, and number of humanitarian volunteers working at each\n" \
            "   camp.\n" \
            "d. Edit volunteer accounts. The admin can also deactivate/reactivate\n" \
            "   volunteers accounts or simply delete them completely from the system.\n" \
            "   Deactivating means, volunteers can no longer use their accounts. If they\n" \
            "   try to login, they get a message “Your account has been deactivated,\n" \
            "   contact the administrator”. Once reactivated they can login and use their\n" \
            "   account again as usual. If the account is rather deleted, the volunteer gets\n" \
            "   a message “Account doesn’t exist”.\n" \
            "e. Allocate resources to camps, including food packets, medical supplies,\n" \
            "   etc, based on current camp populations.\n\n" \
            "(B) The humanitarian volunteer can:\n\n" \
            "a. Edit their own personal information. This includes name, phone.\n" \
            "b. Edit their camp information. This includes the identification of their\n" \
            "   camp and the capacity for new refugees.\n" \
            "c. Create refugee profile for each refugee including their family. Each\n" \
            "   refugee must be logged with: their camp identification, medical\n" \
            "   condition, etc. Keep it simple, you can assume a family is a singular\n" \
            "   entity, rather than their constituent members.\n" \
            "d. Display resources (food packets, etc) currently available to the camp"
        )

        label_widget = tk.Label(about_frame, text=about_text, wraplength=400, justify=tk.LEFT)
        label_widget.pack(padx=5, pady=5)

        close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.pack(pady=10)

    def support_pop_up(self):
        about_window = tk.Toplevel(self.window)
        about_window.title("IT Support")
        about_window.geometry("400x400")

        about_title = tk.Label(about_window, text="Producers", font=('Helvetica', 16))
        about_title.pack()

        about_frame = tk.Frame(about_window, relief=tk.RAISED, borderwidth=2)
        about_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        about_text = (
            "About the Producers:\n\n" \
            "The software is the result of the collective efforts of a dedicated and skilled team. " \
            "Each member has brought their unique expertise and creativity to ensure the software meets the highest standards of quality and functionality. " \
            "Their hard work and commitment have been instrumental in bringing this project to life.\n\n" \
            "List of Producers:\n\n" \
            "Ayman Asaria\n" \
            "Costas Hadjineophytou\n" \
            "Kayza Warsame\n" \
            "Nikhita Bhatt\n" \
            "Sebastian Carroll\n" \
            "Thomas Wolstenholme-Hogg\n" \
            "Yingzhe Feng"

        )

        label_widget = tk.Label(about_frame, text=about_text, wraplength=350, justify=tk.LEFT)
        label_widget.pack(padx=5, pady=5)

        # Close button
        close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
        close_button.pack(pady=10)