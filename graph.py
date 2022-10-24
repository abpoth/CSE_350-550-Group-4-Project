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


root= tk.Tk()
# Create a button to open the csv file
root.geometry("1080x750")
def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('CSV files', '*.csv')])
    if file:
        content = file.name
        file.close()
        print("%d characters in this file",len(content))
        return content   
# Add a Label widget
label = Label(root, text="Click the Button to browse the Files", font=('Georgia 8'))
label.pack(side= TOP)
# Create a Button
b = ttk.Button(root, text="Browse", command=open_file,).pack(side= TOP)


def showgraph():
    # setting up env to show graph 
    
    filename = open_file() 
    df = pd1.read_csv(filename)
    a = ('Datetime (UTC)')
    
    #scroll_bar(a)
    figure1 = plt.Figure(figsize=(20,2), dpi=55)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root)
    line1.get_tk_widget().pack(side= TOP)
    df.plot(kind='line', y = ['Temp avg'],x = a, legend=True, ax=ax1)
    ax1.set_title('Temp Avg')

    figure2 = plt.Figure(figsize=(20,2), dpi=55)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side= TOP)
    df.plot(kind='line', y = ['Eda avg'],x = a, legend=True, ax=ax2)
    ax2.set_title('Eda Avg')

    figure3 = plt.Figure(figsize=(20,2), dpi=55)
    ax3 = figure3.add_subplot(111)
    line3 = FigureCanvasTkAgg(figure3, root)
    line3.get_tk_widget().pack(side= TOP)
    df.plot(kind='line', y = ['Acc magnitude avg'],x = a, legend=True, ax=ax3)
    ax3.set_title('Acc magnitude avg')

    figure4 = plt.Figure(figsize=(20,2), dpi=55)
    ax4 = figure4.add_subplot(111)
    line4 = FigureCanvasTkAgg(figure4, root)
    line4.get_tk_widget().pack(side= TOP)
    df.plot(kind='line', y = ['Movement intensity'],x = a, legend=True, ax=ax4)
    ax4.set_title('Movement intensity')

    figure5 = plt.Figure(figsize=(20,2), dpi=55)
    ax5 = figure5.add_subplot(111)
    line5 = FigureCanvasTkAgg(figure5, root)
    line5.get_tk_widget().pack(side= TOP)
    df.plot(kind='line', y = ['Steps count'],x = a, legend=True, ax=ax5)
    ax5.set_title('Steps count')

    figure6 = plt.Figure(figsize=(20,2), dpi=55)
    ax6 = figure6.add_subplot(111)
    line6 = FigureCanvasTkAgg(figure6, root)
    line6.get_tk_widget().pack(side= TOP)
    df.plot(kind='line', y = ['Rest'],x = a, legend=True, ax=ax6)
    ax6.set_title('Rest')
    #arr=(line1)
    return line1,line2,line3,line4,line5,line6

line1,line2,line3,line4,line5,line6 = showgraph()

toolbar1 = NavigationToolbar2Tk(line1, root)
toolbar1.update()
toolbar2 = NavigationToolbar2Tk(line2, root)
toolbar2.update()
toolbar3 = NavigationToolbar2Tk(line3, root)
toolbar3.update()
toolbar4 = NavigationToolbar2Tk(line4, root)
toolbar4.update()
toolbar5 = NavigationToolbar2Tk(line5, root)
toolbar5.update()
toolbar6 = NavigationToolbar2Tk(line6, root)
toolbar6.update()


if __name__ == "__main__":
    root.mainloop() 
