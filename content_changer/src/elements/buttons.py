import tkinter as tk


def executable_button(root: tk.Tk, button_name: str, command,
                      padding_x: int = 10,
                      padding_y: int = 5,
                      foreground: str = "white",
                      background: str = "black") -> tk:
    """
        Creates a tk button
        :param root: tk app
        :param button_name: name of the button
        :param command: attached command for the button
        :param padding_x: number of the padding x
        :param padding_y: number of the padding y
        :param foreground: foreground color
        :param background: background color
        :return: tk button
    """
    return tk.Button(root,
                     text=button_name,
                     padx=padding_x,
                     pady=padding_y,
                     fg=foreground,
                     bg=background,
                     command=command).pack()
