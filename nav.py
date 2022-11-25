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

class Navbar(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.button1 = tk.Radiobutton(self, text="Button 1")
        self.button2 = tk.Scale(self, from_=0, to=100, orient=HORIZONTAL)
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