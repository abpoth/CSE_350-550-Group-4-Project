import tkinter as tk
from turtle import left
from pandas import DataFrame
import pandas as pd1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from tkinter import filedialog

# Import the required Libraries

from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile


root= tk.Tk()

# Create a button to open the csv file
root.geometry("1080x550")
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
#scroll bar 
scroll_bar = Scrollbar(root)
  
scroll_bar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scroll_bar.set )

# Create a Button
b = ttk.Button(root, text="Browse", command=open_file,).pack(side= TOP)
# print(b)

def showgraph():
    # setting up env to show graph 
    
    filename = open_file() 
    df = pd1.read_csv(filename)
    df1 = DataFrame(df[['Datetime (UTC)','Temp avg']])
    df2 = DataFrame(df[['Datetime (UTC)','Eda avg']])
    df3 = DataFrame(df[['Datetime (UTC)','Acc magnitude avg']])
    df4 = DataFrame(df[['Datetime (UTC)','Movement intensity']])
    df5 = DataFrame(df[['Datetime (UTC)','Steps count']])
    df6 = DataFrame(df[['Datetime (UTC)','Rest']])
    

    figure1 = plt.Figure(figsize=(20,2), dpi=55)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side= TOP)
    df1 = df1[['Datetime (UTC)','Temp avg']]
    df1.plot(kind='line', legend=True, ax=ax1)
    ax1.set_title('Temp Avg')

    figure2 = plt.Figure(figsize=(20,2), dpi=55)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side= TOP)
    df2 = df2[['Datetime (UTC)','Eda avg']]
    df2.plot(kind='line', legend=True, ax=ax2)
    ax2.set_title('Eda Avg')

    figure3 = plt.Figure(figsize=(20,2), dpi=55)
    ax3 = figure3.add_subplot(111)
    line3 = FigureCanvasTkAgg(figure3, root)
    line3.get_tk_widget().pack(side= TOP)
    df3 = df3[['Datetime (UTC)','Acc magnitude avg']]
    df3.plot(kind='line', legend=True, ax=ax3)
    ax3.set_title('Acc magnitude avg')

    figure4 = plt.Figure(figsize=(20,2), dpi=55)
    ax4 = figure4.add_subplot(111)
    line4 = FigureCanvasTkAgg(figure4, root)
    line4.get_tk_widget().pack(side= TOP)
    df4 = df4[['Datetime (UTC)','Movement intensity']]
    df4.plot(kind='line', legend=True, ax=ax4)
    ax4.set_title('Movement intensity')

    figure5 = plt.Figure(figsize=(20,2), dpi=55)
    ax5 = figure5.add_subplot(111)
    line5 = FigureCanvasTkAgg(figure5, root)
    line5.get_tk_widget().pack(side= TOP)
    df5 = df5[['Datetime (UTC)','Steps count']]
    df5.plot(kind='line', legend=True, ax=ax5)
    ax5.set_title('Steps count')

    figure6 = plt.Figure(figsize=(20,2), dpi=55)
    ax6 = figure6.add_subplot(111)
    line6 = FigureCanvasTkAgg(figure6, root)
    line6.get_tk_widget().pack(side= TOP)
    df6 = df6[['Datetime (UTC)','Rest']]
    df6.plot(kind='line', legend=True, ax=ax6)
    ax6.set_title('Rest')
    
    mylist.pack( side = LEFT, fill = BOTH )
  
    scroll_bar.config( command = mylist.yview )

        
#     tkagg.NavigationToolbar2TkAgg(canvas, root)


showgraph()

if __name__ == "__main__":
    root.mainloop()
