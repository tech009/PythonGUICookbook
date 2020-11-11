import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

def _msgBox():
	answer = msg.askyesnocancel('Python Message Multi Choice Box', "Are you sure you really wish to do this ?")
	print(answer)