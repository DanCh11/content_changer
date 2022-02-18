import tkinter as tk

from elements.canvas import create_app_canvas
from elements.buttons import executable_button
from actions.file_directory_actions import extract_excel_file_from_explorer, execute_transform_pipeline

root = tk.Tk()

create_app_canvas(root)
executable_button(root, 'Open File', execute_transform_pipeline)


root.mainloop()
