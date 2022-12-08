import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

mpl.use('TkAgg')


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Main Screen")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        width = 1200
        height = 1200
        # creating a frame and assigning it to container
        
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        align = '%dx%d+%d+%d' % (width, height, (screenWidth - width)/2, (screenHeight - height)/2)
        self.geometry(align)
        # 
        container = tk.Frame(self)
        self.configure(background="#c7d6ed")
        # specifying the region where the frame is packed in root
        #container.pack(side="top", fill="both", expand=True)
        container.grid(row=0,column=0)
        # configuring the location of the container using grid
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainScreen, Paricipant, SelectDataAttributes, ShowGraph):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(background="#c7d6ed")
            

        # Using a method to switch frames
        self.show_frame(MainScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class MainScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        label = tk.Label(self, text="Welcome\nPlease Press the Button to\nStart Data Visualization")
        ft1 = tkFont.Font(family='Times',size=32)
        label["font"] = ft1
        label["justify"] = "center"
        #label.place(x=50,y=50,width=515,height=147)
        label.pack(padx=100, pady=100)
        #label.pack()

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        StartButton = tk.Button(
            self,
            text="Start",
            command=lambda: controller.show_frame(Paricipant),
        )
        StartButton["activebackground"] = "#00ced1"
        StartButton["bg"] = "#00ced1"
        ft2 = tkFont.Font(family='Times',size=28)
        StartButton["font"] = ft2
        StartButton["fg"] = "#393d49"
        StartButton["justify"] = "center"
        StartButton["text"] = "Start"
        StartButton["relief"] = "ridge"
        #StartButton.place(x=140,y=260,width=310,height=342)
        #StartButton.pack(side="bottom", fill=tk.X)
        StartButton.pack()

clicked=[]
clicked2=[]


class Paricipant(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global clicked
        global clicked2
        #self.dates1()
        # clicked=[]
        # clicked2=[]
        #self.showff()
        print("data is : ", clicked)
        self.tclicked=''
        SelectAttriutesPage = tk.Button(
            self,
            command=lambda: controller.show_frame(SelectDataAttributes),
        )
        SelectAttriutesPage["activebackground"] = "#9b60ad"
        SelectAttriutesPage["bg"] = "#c71585"
        ft8 = tkFont.Font(family='Times',size=28)
        SelectAttriutesPage["font"] = ft8
        #SelectAttriutesPage["fg"] = "#3S93d49"
        SelectAttriutesPage["justify"] = "center"
        SelectAttriutesPage["text"] = "Select Data Attributes"
        SelectAttriutesPage["relief"] = "ridge"
        SelectAttriutesPage.grid(row= 1,column=0,padx=1, pady=10, sticky=EW, columnspan=4)#pack(side=BOTTOM,expand=True, fill=BOTH,  anchor=S)

        
        
    #def dates1(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame1 = Frame(self, highlightbackground="blue", highlightthickness=2)
        self.frame1.grid(row=0,column=0)#pack(side=LEFT,fill=Y)
        self.frame2 = Frame(self, highlightbackground="blue", highlightthickness=2)
        self.frame2.grid(row=0,column=1)#pack(side=RIGHT, fill=Y)
        self.participant310 = tk.Button(self.frame1,text="Participant 310")
        self.participant310.config(command=lambda btn1=self.participant310: self.get_fname(btn1))
        self.participant311 = tk.Button(self.frame1,text="Participant 311")
        self.participant311.config(command=lambda btn1=self.participant311: self.get_fname(btn1))
        self.participant312 = tk.Button(self.frame1,text="Participant 312")
        self.participant312.config(command=lambda btn1=self.participant312: self.get_fname(btn1))
        self.participant310["activebackground"] = ["#00ced1"]
        self.participant310["bg"] = "#00ced1"
        ft2 = tkFont.Font(family='Times',size=28)
        self.participant310["font"] = ft2
        self.participant310["fg"] = "#393d49"
        self.participant310["justify"] = "center"
        self.participant310["relief"] = "ridge"

        self.participant311["activebackground"] = ["#00ced1"]
        self.participant311["bg"] = "#00ced1"
        ft2 = tkFont.Font(family='Times',size=28)
        self.participant311["font"] = ft2
        self.participant311["fg"] = "#393d49"
        self.participant311["justify"] = "center"
        self.participant311["relief"] = "ridge"

        self.participant312["activebackground"] = ["#00ced1"]
        self.participant312["bg"] = "#00ced1"
        ft2 = tkFont.Font(family='Times',size=28)
        self.participant312["font"] = ft2
        self.participant312["fg"] = "#393d49"
        self.participant312["justify"] = "center"
        self.participant312["relief"] = "ridge"

        self.Jan18_2020 = tk.Button(self.frame1,text="2020-01-18")
        self.Jan18_2020.config(command= lambda btn=self.Jan18_2020: self.showall(btn))
        self.Jan18_2020.grid(row=1,column=1, padx=10,pady=10)
 
        self.Jan19_2020 = tk.Button(self.frame1,text="2020-01-19")
        self.Jan19_2020.config(command=lambda btn=self.Jan19_2020: self.showall(btn))
        self.Jan19_2020.grid(row=2,column=1, padx=10,pady=10)

        self.Jan20_2020 = tk.Button(self.frame1,text="2020-01-20")
        self.Jan20_2020.config(command=lambda btn=self.Jan20_2020: self.parts(btn))
        self.Jan20_2020.grid(row=3,column=1, padx=10,pady=10)

        self.Jan21_2020 = tk.Button(self.frame1,text="2020-01-21")
        self.Jan21_2020.config(command=lambda btn=self.Jan21_2020: self.parts(btn))
        self.Jan21_2020.grid(row=4,column=1, padx=10,pady=10)
        self.Jan21_2020["activebackground"] = "#00ced1"
        self.Jan21_2020["bg"] = "#00ced1"
        self.Jan21_2020["font"] = ft2
        self.Jan21_2020["fg"] = "#393d49"
        self.Jan21_2020["justify"] = "center"
        self.Jan21_2020["relief"] = "ridge"

        self.Jan20_2020["activebackground"] = "#00ced1"
        self.Jan20_2020["bg"] = "#00ced1"
        self.Jan20_2020["font"] = ft2
        self.Jan20_2020["fg"] = "#393d49"
        self.Jan20_2020["justify"] = "center"
        self.Jan20_2020["relief"] = "ridge"

        self.Jan19_2020["activebackground"] = "#00ced1"
        self.Jan19_2020["bg"] = "#00ced1"
        self.Jan19_2020["font"] = ft2
        self.Jan19_2020["fg"] = "#393d49"
        self.Jan19_2020["justify"] = "center"
        self.Jan19_2020["relief"] = "ridge"

        self.Jan18_2020["activebackground"] = "#00ced1"
        self.Jan18_2020["bg"] = "#00ced1"
        self.Jan18_2020["font"] = ft2
        self.Jan18_2020["fg"] = "#393d49"
        self.Jan18_2020["justify"] = "center"
        self.Jan18_2020["relief"] = "ridge"
        

    def remove(self,widget1):
        widget1.grid_remove()
    def display(self,widget1, widget2, widget3):
        widget1.grid(row=1,column=2, padx=10,pady=10)
        widget2.grid(row=2,column=2, padx=10,pady=10)
        widget3.grid(row=3,column=2, padx=10,pady=10)
        
    def display2(self,widget1,widget2):
        widget1.grid(row=1,column=2, padx=10,pady=10)
        widget2.grid(row=3,column=2, padx=10,pady=10)
    # def exist(self,widget):
    #     print("Checking for existence = ", bool(widget.winfo_exists()))
    def parts(self, btn):
        global clicked
        global clicked
        text = btn.cget("text")
        text = text.replace('-', '')
        clicked.append(text)
        if(len(clicked) > 1):
            clicked.pop(0)
        print("clicked:", clicked)
        if(text == "20200120" or text == "20200121"):
            self.display2(self.participant310,self.participant312)
        if(bool(self.participant311.winfo_exists()) == True):
            #print("removing 311")
            self.remove(self.participant311)
    def showall(self,btn):
        global clicked
        global clicked2
        text = btn.cget("text")
        text = text.replace('-', '')
        clicked.append(text)
        if(len(clicked) > 1):
            clicked.pop(0)
        #prclicked:", text)   
        print("clicked:", clicked)
        if(text == "20200118" or text == "20200119"):
            self.display(self.participant310,self.participant311,self.participant312)
    def get_fname(self,btn1):
        text = btn1.cget("text")
        if(text == "Participant 310"):
            text = "310"
        elif(text == "Participant 311"):
            text = "311"
        elif(text == "Participant 312"):
            text = "312"
        
        text = text.replace('-', '')
        clicked2.append(text)
        if(len(clicked2) > 1):
            clicked2.pop(0)
        print("here", clicked," : ",clicked2)
    @classmethod
    def ttfd():
        return clicked,clicked2
    @staticmethod
    #@classmethod
    def g1234():
        global clicked  
        global clicked2
        global file
        #c,c2 = Paricipant.ttfd()
        clicked = clicked
        clicked2 = clicked2
        #Participaclicked
        print(clicked)
        date_t = clicked
        participant = (clicked2)
        de = "".join(date_t)
        pe = "".join(participant)
        de1 = ("r'/",de)
        #file = open("Dataset/"+de+"/"+pe+"/summary.csv")
        if (clicked and clicked2):
            file = open("Dataset/"+"".join(clicked)+"/"+"".join(clicked2)+"/summary.csv")
            #df = pd.read_csv('Dataset/20200121/310/summary.csv', skiprows=[1])

        else:
            file = open("Dataset/"+"20200118"+"/"+"310"+"/summary.csv")
        return file

        #return(file)
#        print("".join(date_t),"".join(participant))



class SelectDataAttributes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        frame1 = Frame(self, highlightbackground="blue", highlightthickness=2)
        frame1.grid(padx=10,pady=100,row=0,column=0)#pack(side=LEFT,fill=Y)
        label1 = tk.Label(frame1, text="Select Attribute(s)")
        ft1 = tkFont.Font(family='Times',size=14)
        label1["font"] = ft1
        label1["justify"] = "center"
        label1.grid(padx=10,pady=10,row=0,column=0)

        label2 = tk.Label(frame1, text="Query Operator(s)")
        ft1 = tkFont.Font(family='Times',size=14)
        label2["font"] = ft1
        label2["justify"] = "center"
        label2.grid(padx=10,pady=10,row=0,column=1)

        label3 = tk.Label(frame1, text="Input(s)")
        ft1 = tkFont.Font(family='Times',size=14)
        label3["font"] = ft1
        label3["justify"] = "center"
        label3.grid(padx=10,pady=10,row=0,column=2)

        MagnitudeAvg = tk.Button(
            frame1,
            text="Acc Magnitude Avg",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        MagnitudeAvg["activebackground"] = "#1e90ff"
        MagnitudeAvg["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=28)
        MagnitudeAvg["font"] = ft3
        MagnitudeAvg["fg"] = "#393d49"
        MagnitudeAvg["justify"] = "center"
        MagnitudeAvg["text"] = "Acc Magnitude Avg"
        MagnitudeAvg["relief"] = "ridge"
        MagnitudeAvg.grid(padx=10,pady=10,row=1,column=0)

        mag_avg_operators = OptionMenu(frame1, StringVar(), "Null", ">", ">", "=")
        mag_avg_operators.grid(padx=10,pady=10,row=1,column=1)

        mag_avg_input = tk.Text(frame1, height=2, width=20)
        mag_avg_input.grid(padx=10,pady=10,row=1,column=2)

        EdaAvg = tk.Button(
            frame1,
            text="Eda Avg",
        #    command=lambda: controller.show_frame(Paricipant),
        )
        EdaAvg["activebackground"] = "#1e90ff"
        EdaAvg["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=28)
        EdaAvg["font"] = ft3
        EdaAvg["fg"] = "#393d49"
        EdaAvg["justify"] = "center"
        EdaAvg["text"] = "Eda Avg"
        EdaAvg["relief"] = "ridge"
        EdaAvg.grid(padx=10,pady=10,row=2,column=0)

        eda_avg_operators = OptionMenu(frame1, StringVar(), "Null", ">", ">", "=")
        eda_avg_operators.grid(padx=10,pady=10,row=2,column=1)

        eda_avg_input = tk.Text(frame1, height=2, width=20)
        eda_avg_input.grid(padx=10,pady=10,row=2,column=2)

        TempAvg = tk.Button(
            frame1,
            text="Temp Avg",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        TempAvg["activebackground"] = "#1e90ff"
        TempAvg["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=28)
        TempAvg["font"] = ft3
        TempAvg["fg"] = "#393d49"
        TempAvg["justify"] = "center"
        TempAvg["text"] = "Temp Avg"
        TempAvg["relief"] = "ridge"
        TempAvg.grid(padx=10,pady=10,row=3,column=0)

        temp_avg_operators = OptionMenu(frame1, StringVar(), "Null", ">", ">", "=")
        temp_avg_operators.grid(padx=10,pady=10,row=3,column=1)

        temp_avg_input = tk.Text(frame1, height=2, width=20)
        temp_avg_input.grid(padx=10,pady=10,row=3,column=2)

        Movement = tk.Button(
            frame1,
            text="Movement",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        Movement["activebackground"] = "#1e90ff"
        Movement["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=28)
        Movement["font"] = ft3
        Movement["fg"] = "#393d49"
        Movement["justify"] = "center"
        Movement["text"] = "Movement"
        Movement["relief"] = "ridge"
        Movement.grid(padx=10,pady=10,row=4,column=0)

        movement_operators = OptionMenu(frame1, StringVar(), "Null", ">", ">", "=")
        movement_operators.grid(padx=10,pady=10,row=4,column=1)

        movement_input = tk.Text(frame1, height=2, width=20)
        movement_input.grid(padx=10,pady=10,row=4,column=2)

        StepCount = tk.Button(
            frame1,
            text="Step Count",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        StepCount["activebackground"] = "#1e90ff"
        StepCount["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=28)
        StepCount["font"] = ft3
        StepCount["fg"] = "#393d49"
        StepCount["justify"] = "center"
        StepCount["text"] = "Step Count"
        StepCount["relief"] = "ridge"
        StepCount.grid(padx=10,pady=10,row=5,column=0) 

        step_operators = OptionMenu(frame1, StringVar(), "Null", ">", ">", "=")
        step_operators.grid(padx=10,pady=10,row=5,column=1)

        step_input = tk.Text(frame1, height=2, width=20)
        step_input.grid(padx=10,pady=10,row=5,column=2)

        Rest = tk.Button(
            frame1,
            text="Rest",
           # command=lambda: controller.show_frame(Paricipant),
        )
        Rest["activebackground"] = "#1e90ff"
        Rest["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=28)
        Rest["font"] = ft3
        Rest["fg"] = "#393d49"
        Rest["justify"] = "center"
        Rest["text"] = "Rest"
        Rest["relief"] = "ridge"
        Rest.grid(padx=10,pady=10,row=6,column=0) 

        rest_operators = OptionMenu(frame1, StringVar(), "Null", ">", ">", "=")
        rest_operators.grid(padx=10,pady=10,row=6,column=1)

        rest_input = tk.Text(frame1, height=2, width=20)
        rest_input.grid(padx=10,pady=10,row=6,column=2,columnspan=4)

       
            #return self.d11,self.dpar

        ShowData = tk.Button(
            self,
            text="Show Data",
            command=lambda: (controller.show_frame(ShowGraph))
        )
        ShowData["activebackground"] = "#9b60ad"
        ShowData["bg"] = "#c71585"
        ft3 = tkFont.Font(family='Times',size=28)
        ShowData["font"] = ft3
        ShowData["fg"] = "#393d49"
        ShowData["justify"] = "center"
        ShowData["text"] = "Show Data"
        ShowData["relief"] = "ridge"
        ShowData.grid(row= 7,column=0,padx=1, pady=10, sticky=EW, columnspan=6)


#-----------------------------------------------------------------------------------------------------------------------------------------ShowGraph
filename = ''
#df = pd.DataFrame()
#df = pd.read_csv(filename, skiprows=[1])
df = pd.read_csv
class ShowGraph(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.graph()
        global filename
        global clicked
        
        #self.filename
        #global file
        print("been here:", clicked)
        
        #print(file)

        redo1 = tk.Button(
            self,
            text="Show Data",
            command=lambda: controller.show_frame(MainScreen),
        )
        redo1["activebackground"] = "#9b60ad"
        redo1["bg"] = "#c71585"
        ft3 = tkFont.Font(family='Times',size=28)
        redo1["font"] = ft3
        redo1["fg"] = "#393d49"
        redo1["justify"] = "center"
        redo1["text"] = "redo"
        redo1["relief"] = "ridge"
        redo1.pack(side=BOTTOM)#.grid(row= 7,column=0,padx=1, pady=1, sticky=EW, columnspan=6)
        
    def remove(self,widget1):
        widget1.pack_forget()

    def showit(self):
        global filename
        global df
        try: 
            self.canvas.get_tk_widget().pack_forget()
            self.toolbar.pack_forget()
        except AttributeError: 
            pass  
        if(not clicked):
            fw = Paricipant.g1234()
            #filename = open("Dataset"+date_t+participant+"/summary.csv")
            print("not clicked", fw)
            filename = fw
        else:
            fw = Paricipant.g1234()
            #filename = filename = Paricipant.g1234()
            print("it is clicked: file name:", fw.name)
            filename = fw.name
        if filename == '':
            df = pd.read_csv('Dataset/20200121/310/summary.csv', skiprows=[1])
        else:
            df = pd.read_csv(filename, skiprows=[1])
        print("this is global fn: ",filename)
        #return fw.name
        x = ("Datetime (UTC)")

        row, cols = 7,1
        fig, ax = plt.subplots(figsize=(7,7), dpi=100,nrows=row,ncols=cols, sharex=True)
        fig.subplots_adjust(hspace=1, wspace=.5,bottom=.1,top=1)
        p1 = ax[0];p2 = ax[1];p3 = ax[2];p4 = ax[3];p5 = ax[4]
        p6 = ax[5];p7 = ax[6]
        fromx = 0; tox1 = 1405
        #df = pd.read_csv(filename, skiprows=[1])
        df.iloc[fromx:tox1].plot(x, "Acc magnitude avg",ax=p1)
        df.iloc[fromx:tox1].plot(x, "Eda avg", ax=p2)
        df.iloc[fromx:tox1].plot(x, "Temp avg", ax=p3)
        df.iloc[fromx:tox1].plot(x, "Movement intensity", ax=p4)
        df.iloc[fromx:tox1].plot(x, "Steps count", ax=p5)
        df.iloc[fromx:tox1].plot(x, "Rest", ax=p6)
        fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side= TOP)#.grid(row= 1,column=0,padx=10, pady=10, sticky=N, columnspan=6)
        self.toolbar = NavigationToolbar2Tk(self.canvas,self) #pack_toolbar=False)
        self.toolbar.pack(side=BOTTOM)#.grid(row= 0,column=0,padx=10, pady=10, sticky=N, columnspan=6)
        self.toolbar.update()
        # if self.canvas > 1:
        #     self.canvas.pack_forget()
    def graph(self):
        frame1 = Frame(self, highlightbackground="blue", highlightthickness=2)
        frame1.pack()#.grid(row=0,column=0)#pack(side=LEFT,fill=Y)
        global filename
        Lb1 = Listbox(self)
        Lb1.insert(1, "Home/Reset -- h or r or home/n")
        Lb1.insert(2, "Back -- c or left arrow or backspace")
        Lb1.insert(3, "Forward	-- v or right arrow")
        Lb1.insert(4, "/n")
        Lb1.insert(5, "JSP")
        Lb1.insert(6, "Ruby")

        #Lb1.pack(side=RIGHT)
        label = tk.Label(self, text="""Home/Reset -- h or r or home/n
Back -- c or left arrow or backspace/n
Forward	-- v or right arrow/n
Pan/Zoom-- p/n
Zoom-to-rect -- o/n
Save -- ctrl + s /n
Toggle fullscreen -- f or ctrl + f /n
Close plot -- ctrl + w /n
Close all plots	-- shift + w""", anchor='w')
        ft1 = tkFont.Font(family='Times',size=15)
        label["font"] = ft1
        label["justify"] = "center"
        #label.place(x=50,y=50,width=515,height=147)
        label.pack(side= LEFT)

        rcp = mpl.rcParams
        rcp['lines.linewidth'] = 2.0
        rcp['lines.markeredgewidth'] = 1.0
        rcp['axes.labelsize'] = 2
        rcp['font.size'] = 7
        rcp['patch.linewidth'] = .7
        rcp['figure.facecolor'] = '#c7d6ed'
        rcp['figure.edgecolor'] = '#c7d6ed'
        
        #rcp['toolbar']= True
        date_t = (r'/20200118')
        participant = (r'/310')
        
        bnt = tk.Button(self,
            text="Show Selected Graph",
            command= lambda: self.showit()
        )
        bnt["activebackground"] = "#00ced1"
        bnt["bg"] = "#00ced1"
        ft2 = tkFont.Font(family='Times',size=28)
        bnt["font"] = ft2
        bnt["fg"] = "#393d49"
        bnt["justify"] = "center"
        #bnt["text"] = "Start"
        bnt["relief"] = "ridge"
        bnt.pack(side=TOP)#.grid(row=0,column=0,sticky=NE)
        #pack(side=BOTTOM, fill='both', expand=True)
       # canvas.draw()
        
        # toolbar = NavigationToolbar2Tk(canvas, self)
        # toolbar.update()
        # canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
if __name__ == "__main__":

    testObj = windows()
    #testObj.geometry("1200x1200")
    testObj.mainloop()