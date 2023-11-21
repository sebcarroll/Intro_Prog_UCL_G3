import tkinter as tk
from tkinter import ttk

class FancyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fancy Tkinter GUI")

        # Creating a Menu Bar
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.dummy_command)
        file_menu.add_command(label="Open", command=self.dummy_command)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Adding the menu bar to the root window
        self.root.config(menu=menu_bar)

        # Creating a Notebook (Tabbed Panels)
        tab_control = ttk.Notebook(self.root)

        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="Tab 1")

        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text="Tab 2")

        tab_control.pack(expand=1, fill="both")

        # Adding widgets to Tab 1
        label1 = ttk.Label(tab1, text="Welcome to Tab 1", font=("Arial", 16))
        label1.grid(column=0, row=0, padx=10, pady=10)

        btn1 = ttk.Button(tab1, text="Click Me", command=self.dummy_command)
        btn1.grid(column=0, row=1, padx=10, pady=10)

        # Adding widgets to Tab 2
        label2 = ttk.Label(tab2, text="Welcome to Tab 2", font=("Arial", 16))
        label2.grid(column=0, row=0, padx=10, pady=10)

        entry1 = ttk.Entry(tab2)
        entry1.grid(column=0, row=1, padx=10, pady=10)

    def dummy_command(self):
        print("Menu item clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FancyGUI(root)
    root.mainloop()
