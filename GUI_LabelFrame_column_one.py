import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('LabelFrame')

button_frame = ttk.LabelFrame(win, text=' Labels in a Frame')
button_frame.grid(column=0, row=7)

ttk.Label(button_frame, text='Label1').grid(column=0, row=0, sticky=tk.W)
ttk.Label(button_frame, text='Label2').grid(column=1, row=0, sticky=tk.W)
ttk.Label(button_frame, text='Label3').grid(column=2, row=0, sticky=tk.W)

win.mainloop()