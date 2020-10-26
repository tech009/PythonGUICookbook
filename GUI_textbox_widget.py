import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title('TextBox Widget')

def click_me():
	action.configure(text='Hello ' + name.get())

ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

win.mainloop()