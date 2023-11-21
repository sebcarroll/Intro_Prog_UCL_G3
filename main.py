import tkinter as tk
from landing_page import LandingPage
from admin_main import AdminHomepage
from volunteer_main import VolunteerHomepage


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.landing_page = None
        self.admin_homepage = None
        self.volunteer_homepage = None
        self.username = None
        self.go_to_landing_page()

        self.root.mainloop()

    def go_to_landing_page(self):
        if self.admin_homepage:
            self.admin_homepage.destroy()
        if self.volunteer_homepage:
            self.volunteer_homepage.destroy()
        self.landing_page = LandingPage(self.root, self.go_to_admin_main, self.go_to_volunteer_main)

    def go_to_admin_main(self):
        if self.landing_page:
            self.landing_page.destroy()
        self.admin_homepage = AdminHomepage(self.root, self.go_to_landing_page)

    def go_to_volunteer_main(self, username):
        if self.landing_page:
            self.landing_page.destroy()
        self.volunteer_homepage = VolunteerHomepage(self.root, username, self.go_to_landing_page)


if __name__ == "__main__":
    Main()
