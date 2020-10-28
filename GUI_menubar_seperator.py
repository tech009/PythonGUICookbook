import tkinter as tk
from tkinter import ttk,scrolledtext,Menu

win = tk.Tk()
win.title("Menu Bar")

menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=win.quit)
menu_bar.add_cascade(label='File', menu=file_menu)

win.mainloop()