# admin_gui.py

import tkinter as tk
from LearningResourceAndOldFiles import admin_functions as af


class AdminHomepage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('750x600')
        self.root.title("Admin Homepage")

        # Create new event button
        self.btn_create_event = tk.Button(self.root, text="Create new event", command=af.create_event)
        self.btn_create_event.pack(pady=10)

        # End an event button
        self.btn_end_event = tk.Button(self.root, text="End an event", command=af.end_event)
        self.btn_end_event.pack(pady=10)

        # View summaries button
        self.btn_view_summaries = tk.Button(self.root, text="View Summaries", command=af.view_summaries)
        self.btn_view_summaries.pack(pady=10)

        # Edit volunteer accounts button
        self.btn_edit_accounts = tk.Button(self.root, text="Edit volunteer accounts", command=af.edit_accounts)
        self.btn_edit_accounts.pack(pady=10)

        # Allocate resources button
        self.btn_allocate_resources = tk.Button(self.root, text="Allocate resources", command=af.allocate_resources)
        self.btn_allocate_resources.pack(pady=10)




# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AdminHomepage(root)
    root.mainloop()