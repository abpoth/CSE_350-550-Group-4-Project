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
        # self.button1 = tk.Button(self, text="Button 1")
        # self.button2 = tk.Button(self, text="Button 2")
        # self.button3 = tk.Button(self, text="Button 3")
        # self.button1.pack(side="top")
        # self.button2.pack(side="top")
        # self.button3.pack(side="top")

class Toolbar(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.button1 = tk.Button(self, text="Button 1")
        # self.button2 = tk.Button(self, text="Button 2")
        # self.button3 = tk.Button(self, text="Button 3")
        # self.button1.pack(side="left")
        # self.button2.pack(side="left")
        # self.button3.pack(side="left")

class Statusbar(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.label = tk.Label(self, text="Status bar")
        self.label.pack(side="left",)

class Filepack(tk.Frame):
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
        self.date_on = Label()
    def switch310(self):
        global is_on
        if not self.on310:
            self.button_310.config(image = self.on)
            self.on310 = True
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

class Graph(tk.Frame): 
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.label = Label(self, text="Graphs")
        self.label.grid(row=0,column=0,padx=10,pady=10)
        # Link a scrollbar to the canvas
        
    
  

        date_t = (r'\20200118')
        participant = (r'\310')

        filename =  (r"C:\Users\15027\Desktop\real\Dataset"+date_t+participant+"\summary.csv")
        #filename = ''
        
        df = pd1.read_csv(filename)
        a = ('Datetime (UTC)')
        Unix_Timestamp = ('Unix Timestamp (UTC)')

        #scroll_bar(a)

        time_figure = plt.Figure(figsize=(15,2), dpi= 50)
        ax0 = time_figure.add_subplot(111)
        line0 = FigureCanvasTkAgg(time_figure, self)
        line0.get_tk_widget().grid(row=1,column=0,pady=6)
        df.plot(kind='line',y = Unix_Timestamp,x = a, legend=True, ax=ax0)
        ax0.set_title('Time')

        figure1 = plt.Figure(figsize=(15,2), dpi=50)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, self)
        line1.get_tk_widget().grid(row=2,column=0,pady=6)
        df.plot(kind='line', y = ['Temp avg'],x = a, legend=True, ax=ax1)
        ax1.set_title('Temp Avg')

        figure2 = plt.Figure(figsize=(15,2), dpi=50)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self)
        line2.get_tk_widget().grid(row=3,column=0,pady=6)
        df.plot(kind='line', y = ['Eda avg'],x = a, legend=True, ax=ax2)
        ax2.set_title('Eda Avg')

        figure3 = plt.Figure(figsize=(15,2), dpi=50)
        ax3 = figure3.add_subplot(111)
        line3 = FigureCanvasTkAgg(figure3, self)
        line3.get_tk_widget().grid(row=4,column=0,pady=6)
        df.plot(kind='line', y = ['Acc magnitude avg'],x = a, legend=True, ax=ax3)
        ax3.set_title('Acc magnitude avg')

        figure4 = plt.Figure(figsize=(15,2), dpi=50)
        ax4 = figure4.add_subplot(111)
        line4 = FigureCanvasTkAgg(figure4, self)
        line4.get_tk_widget().grid(row=5,column=0,pady=6)
        df.plot(kind='line', y = ['Movement intensity'],x = a, legend=True, ax=ax4)
        ax4.set_title('Movement intensity')

        figure5 = plt.Figure(figsize=(15,2), dpi=50)
        ax5 = figure5.add_subplot(111)
        line5 = FigureCanvasTkAgg(figure5, self)
        line5.get_tk_widget().grid(row=6,column=0,pady=6)
        df.plot(kind='line', y = ['Steps count'],x = a, legend=True, ax=ax5)
        ax5.set_title('Steps count')

        figure6 = plt.Figure(figsize=(15,2), dpi=50)
        ax6 = figure6.add_subplot(111)
        line6 = FigureCanvasTkAgg(figure6, self)
        line6.get_tk_widget().grid(row=7,column=0,pady=6)
        df.plot(kind='line', y = ['Rest'],x = a, legend=True, ax=ax6)
        ax6.set_title('Rest')
        #arr=(line1)
        #return line1,line2,line3,line4,line5,line6
    def open_file(self):
        global content
        file = filedialog.askopenfile(mode='r', filetypes=[('CSV files', '*.csv')])
        if file:    
            content = file.name
            file.close()
            print("%d characters in this file",len(content))
            print(content)
            #return content
        #return file.name


            

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.statusbar = Statusbar(self)
        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        #self.graph = Graph(self)
        self.filep = Filepack(self)
       

        self.statusbar.grid(row=10,column=3,padx=10,pady=10)
        #self.toolbar.pack(side="top", fill="x")
        #self.navbar.pack(side="left", fill="y")
        self.filep.grid(row=1,column=0,padx=10,pady=10)

    

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("750x675")
    Graph(root).grid(row=1,column=1,padx=1,pady=1)
    MainApplication(root).grid(row=0,column=0,padx=10,pady=1)
    root.grid_columnconfigure(4, minsize=200)  # Here
    root.mainloop()