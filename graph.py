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
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib
 
matplotlib.use('TkAgg')


from nav import Navbar,Toolbar
from OpenFiles import Paricipant
from tkstylesheet import TkThemeLoader



class Statusbar(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent,*args, **kwargs)
        self.label = tk.Label(self, text="Status bar:")
        self.label.grid(row=1,column=1)

        #print(FileOp.namef)
        
    

class Graph(tk.Frame): 
    def __init__(self, parent,  *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)
        matplotlib.use('TkAgg')

        self.label = Label(self, text="Graphs is here")
        self.label.grid(row=0,column=0,padx=10,pady=10)
        self.fileb = tk.Button(self, text="openf")
        self.fileb.config(command= lambda: self.tt())
        self.fileb.grid(row=0,column=0)




        date_t = (r'\20200118')
        participant = (r'\310')
        self.meme = []
        filename =  (r"Dataset"+date_t+participant+"\summary.csv")
        #filename = ''
        print("this is meme",self.meme)

        df = pd1.read_csv(filename)
        self.a = ('Datetime (UTC)')
        Unix_Timestamp = ('Unix Timestamp (UTC)')

        time_figure = plt.Figure(figsize=(15,2), dpi= 50)
        ax0 = time_figure.add_subplot(111)
        line0 = FigureCanvasTkAgg(time_figure, self)
        line0.get_tk_widget().grid(row=1,column=0)
        
        df.plot(kind='line',y = Unix_Timestamp,x = self.a, legend=True, ax=ax0)
        ax0.set_title('Time')

        figure1 = plt.Figure(figsize=(15,2), dpi=50)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, self)
        line1.get_tk_widget().grid(row=2,column=0)
        df.plot(kind='line', y = ['Temp avg'],x = self.a, legend=True, ax=ax1)
        ax1.set_title('Temp Avg')

        figure2 = plt.Figure(figsize=(15,2), dpi=50)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self)
        line2.get_tk_widget().grid(row=3,column=0)
        df.plot(kind='line', y = ['Eda avg'],x = self.a, legend=True, ax=ax2)
        ax2.set_title('Eda Avg')

        figure3 = plt.Figure(figsize=(15,2), dpi=50)
        ax3 = figure3.add_subplot(111)
        line3 = FigureCanvasTkAgg(figure3, self)
        line3.get_tk_widget().grid(row=4,column=0)
        df.plot(kind='line', y = ['Acc magnitude avg'],x = self.a, legend=True, ax=ax3)
        ax3.set_title('Acc magnitude avg')

        figure4 = plt.Figure(figsize=(15,2), dpi=50)
        ax4 = figure4.add_subplot(111)
        line4 = FigureCanvasTkAgg(figure4, self)
        line4.get_tk_widget().grid(row=5,column=0)
        df.plot(kind='line', y = ['Movement intensity'],x = self.a, legend=True, ax=ax4)
        ax4.set_title('Movement intensity')

        self.figure5 = plt.Figure(figsize=(15,2), dpi=50)
        self.ax5 = self.figure5.add_subplot(111)
        line5 = FigureCanvasTkAgg(self.figure5, self)
        line5.get_tk_widget().grid(row=6,column=0)
        df.plot(kind='line', y = ['Steps count'],x = self.a, legend=True, ax=self.ax5)
        self.ax5.set_title('Steps count')

        figure6 = plt.Figure(figsize=(15,2), dpi=50)
        ax6 = figure6.add_subplot(111)
        line6 = FigureCanvasTkAgg(figure6, self)
        line6.get_tk_widget().grid(row=7,column=0)
        df.plot(kind='line', y = ['Rest'],x = self.a, legend=True, ax=ax6)
        ax6.set_title('Rest')
        #arr=(line1)
        #return line1,line2,line3,line4,line5,line6
    
     

    def tt(self):
        gettagss = Paricipant(root)
        self.meme = gettagss.tclicked
        theme = TkThemeLoader(root)
        theme.loadStyleSheet("themes.tkss")  # pass file path
        self.display(gettagss)
    def display(self,widget1):
        widget1.grid()
    def sel(self):
        selection = "You selected the option " + (self.meme.get())
        self.label.config(text = selection)
    

    


class MainGraphApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.navbar.grid(row=0,column=0)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("750x675")

    Graph(root).grid(row=0,column=1,sticky='NE')
    #MainGraphApp(root).grid(row=0,column=0,sticky='W')
    root.mainloop()