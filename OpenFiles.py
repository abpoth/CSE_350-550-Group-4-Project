import tkinter as tk
# test code
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkstylesheet import TkThemeLoader

class Paricipant(tk.Toplevel):
    def __init__(self, parent,  *args, **kwargs):
        tk.Toplevel.__init__(self,parent, *args, **kwargs)
        #self.controller = controller
        self.dates1()
        #self.parts()
        self.clicked=[]
        self.tclicked=''

    def dates1(self):
        self.participant310 = tk.Button(self,text="Participant 310")
        self.participant311 = tk.Button(self,text="Participant 311")
        self.participant312 = tk.Button(self,text="Participant 312")

        self.Jan18_2020 = tk.Button(self,text="2020-01-18")
        self.Jan18_2020.config(command= lambda btn=self.Jan18_2020: self.showall(btn))
        self.Jan18_2020.grid(row=1,column=0)
 
        self.Jan19_2020 = tk.Button(self,text="2020-01-19")
        self.Jan19_2020.config(command=lambda btn=self.Jan19_2020: self.showall(btn))
        self.Jan19_2020.grid(row=2,column=0)

        self.Jan20_2020 = tk.Button(self,text="2020-01-20")
        self.Jan20_2020.config(command=lambda btn=self.Jan20_2020: self.parts(btn))
        self.Jan20_2020.grid(row=3,column=0)

        self.Jan21_2020 = tk.Button(self,text="2020-01-21")
        self.Jan21_2020.config(command=lambda btn=self.Jan21_2020: self.parts(btn))
        self.Jan21_2020.grid(row=4,column=0)
    def remove(self,widget1):
        widget1.grid_remove()
    def display(self,widget1, widget2, widget3):
        widget1.grid(column=3, row=1, padx=10, pady=10)
        widget2.grid(column=3, row=2, padx=10, pady=10)
        widget3.grid(column=3, row=3, padx=10, pady=10)
    def display2(self,widget1,widget2):
        widget1.grid(row=1,column=3)
        widget2.grid(row=3,column=3)
    def exist(self,widget):
        print("Checking for existence = ", bool(widget.winfo_exists()))
    def parts(self, btn):
        text = btn.cget("text")
        text = text.replace('-', '')
        if(text == "20200120" or text == "20200121"):
            self.display2(self.participant310,self.participant312)
        if(bool(self.participant311.winfo_exists()) == True):
            print("checking")
            self.remove(self.participant311)
    def showall(self,btn):
        text = btn.cget("text")
        text = text.replace('-', '')
        self.clicked.append(text)
        if(len(self.clicked) > 1):
            self.clicked.pop(0)
        #print("clicked:", text)   
        print("clicked:", self.clicked)
        if(text == "20200118" or text == "20200119"):
            self.display(self.participant310,self.participant311,self.participant312)
