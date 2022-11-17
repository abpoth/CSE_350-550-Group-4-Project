import tkinter as tk
from turtle import left
from pandas import DataFrame
import pandas as pd1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from tkinter import filedialog
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

class FileOp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.on = PhotoImage(file = "images/on.png")
        self.off = PhotoImage(file = "images/off.png")
        self.on310 = False
        self.on311 = False
        self.on312 = False
        self.button_310 = Button(self, image = self.off,text="310", width=15,height=15,command = self.switch310)
        self.button_310.grid(row=1,column=0, pady= 5)
        self.button_311 = Button(self, image = self.off,width=15,height=15,command = self.switch311)
        self.button_311.grid(row=2,column=0, pady= 5)
        self.button_312 = Button(self, image = self.off, width=15,height=15,command = self.switch312)
        self.button_312.grid(row=3,column=0, pady= 5)
        self.parti = ''
        self.date_oo = Label(self, text= self.parti)
        self.date_oo.grid(row=4,column=5)
    def switch310(self):
        global is_on
        if not self.on310:
            self.button_310.config(image = self.on)
            self.on310 = True
            self.parti = (r'\310')
        else:
            self.button_310.config(image = self.off)
            self.on310 = False
    def switch311(self):
        if not self.on311:
            self.button_311.config(image = self.on)
            self.on311 = True
        else:
            self.button_311.config(image = self.off)
            self.on311 = False
    def switch312(self):
        if not self.on312:
            self.button_312.config(image = self.on)
            self.on312 = True
        else:
            self.button_312.config(image = self.off)
            self.on312 = False


class Navbar(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.button1 = tk.Button(self, text="Button 1")
        self.button2 = tk.Button(self, text="Button 2")
        self.button3 = tk.Button(self, text="Button 3")
        self.button1.pack(side="top")
        self.button2.pack(side="top")
        self.button3.pack(side="top")

class Toolbar(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.button1 = tk.Button(self, text="Button 1")
        # self.button2 = tk.Button(self, text="Button 2")
        # self.button3 = tk.Button(self, text="Button 3")
        # self.button1.pack(side="left")
        # self.button2.pack(side="left")
        # self.button3.pack(side="left")