import tkinter as tk
from tkinter import filedialog, Text

from elements.canvas import create_app_canvas
from elements.buttons import executable_button
from actions.file_directory_actions import extract_excel_file_from_explorer

root = tk.Tk()

create_app_canvas(root)
executable_button(root, 'Open File', extract_excel_file_from_explorer)

root.mainloop()
