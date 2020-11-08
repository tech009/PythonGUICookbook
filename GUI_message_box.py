import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg


def _msgBox():
	msg.showinfo('Python Message Info Box','A Python GUI created using tkinter:\nThe year is 2020')

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=_msgBox)
menu_bar.add_cascade(label='Help', menu=help_menu)