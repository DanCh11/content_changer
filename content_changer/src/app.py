import tkinter as tk

from elements.canvas import create_app_canvas
from elements.buttons import executable_button
from actions.file_directory_actions import execute_transform_pipeline

root = tk.Tk()

create_app_canvas(root)
a = executable_button(root, 'Open File', command=execute_transform_pipeline)

root.mainloop()
