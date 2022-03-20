import tkinter as tk


def create_app_canvas(root: tk.Tk, height: int = 100, width: int = 150) -> tk:
    """
        This function creates the canvas and manages the height and width of the app window
        :param root: tk app
        :param height: height of the window
        :param width: width of the window
        :return: app's canvas
    """
    return tk.Canvas(root, height=height, width=width).pack()
