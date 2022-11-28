import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Main Screen")
        width = 600
        height = 500
        # creating a frame and assigning it to container
        
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        align = '%dx%d+%d+%d' % (width, height, (screenWidth - width)/2, (screenHeight - height)/2)
        self.geometry(align)
        # 
        container = tk.Frame(self, height=600, width=500)
        # specifying the region where the frame is packed in root
        #container.pack(side="top", fill="both", expand=True)
        container.pack(side = TOP)
        # configuring the location of the container using grid
        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainScreen, Paricipant, SelectDataAttributes):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

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


class Paricipant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.dates1()
        self.clicked=[]
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
        SelectAttriutesPage.place(x=110,y=350,width=400,height=75)
        
    def dates1(self):
        self.participant310 = tk.Button(self,text="Participant 310")
        self.participant311 = tk.Button(self,text="Participant 311")
        self.participant312 = tk.Button(self,text="Participant 312")
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

        self.Jan18_2020 = tk.Button(self,text="2020-01-18")
        self.Jan18_2020.config(command= lambda btn=self.Jan18_2020: self.showall(btn))
        self.Jan18_2020.grid(row=1,column=0,padx=10, pady=5)
 
        self.Jan19_2020 = tk.Button(self,text="2020-01-19")
        self.Jan19_2020.config(command=lambda btn=self.Jan19_2020: self.showall(btn))
        self.Jan19_2020.grid(row=2,column=0,padx=10, pady=5)

        self.Jan20_2020 = tk.Button(self,text="2020-01-20")
        self.Jan20_2020.config(command=lambda btn=self.Jan20_2020: self.parts(btn))
        self.Jan20_2020.grid(row=3,column=0,padx=10, pady=5)

        self.Jan21_2020 = tk.Button(self,text="2020-01-21")
        self.Jan21_2020.config(command=lambda btn=self.Jan21_2020: self.parts(btn))
        self.Jan21_2020.grid(row=4,column=0,padx=10, pady=5)
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
        widget1.grid(column=3, row=1, padx=10, pady=5)
        widget2.grid(column=3, row=2, padx=10, pady=5)
        widget3.grid(column=3, row=3, padx=10, pady=5)
    def display2(self,widget1,widget2):
        widget1.grid(row=1,column=3,padx=10, pady=5)
        widget2.grid(row=3,column=3,padx=10, pady=5)
    # def exist(self,widget):
    #     print("Checking for existence = ", bool(widget.winfo_exists()))
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



class SelectDataAttributes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label1 = tk.Label(self, text="Select Attribute(s)")
        ft1 = tkFont.Font(family='Times',size=14)
        label1["font"] = ft1
        label1["justify"] = "center"
        label1.place(x=25,y=25,width=200,height=40)

        label2 = tk.Label(self, text="Query Operator(s)")
        ft1 = tkFont.Font(family='Times',size=14)
        label2["font"] = ft1
        label2["justify"] = "center"
        label2.place(x=250,y=25,width=200,height=40)

        label3 = tk.Label(self, text="Input(s)")
        ft1 = tkFont.Font(family='Times',size=14)
        label3["font"] = ft1
        label3["justify"] = "center"
        label3.place(x=400,y=25,width=200,height=40)

        MagnitudeAvg = tk.Button(
            self,
            text="Acc Magnitude Avg",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        MagnitudeAvg["activebackground"] = "#1e90ff"
        MagnitudeAvg["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=12)
        MagnitudeAvg["font"] = ft3
        MagnitudeAvg["fg"] = "#393d49"
        MagnitudeAvg["justify"] = "center"
        MagnitudeAvg["text"] = "Acc Magnitude Avg"
        MagnitudeAvg["relief"] = "ridge"
        MagnitudeAvg.place(x=50,y=75,width=150,height=40)

        mag_avg_operators = OptionMenu(self, StringVar(), "Null", ">", ">", "=")
        mag_avg_operators.place(x=325,y=75,width=50,height=40)

        mag_avg_input = tk.Text(self, height=5, width=10)
        mag_avg_input.place(x=475,y=75,width=50,height=40)

        EdaAvg = tk.Button(
            self,
            text="Eda Avg",
        #    command=lambda: controller.show_frame(Paricipant),
        )
        EdaAvg["activebackground"] = "#1e90ff"
        EdaAvg["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=12)
        EdaAvg["font"] = ft3
        EdaAvg["fg"] = "#393d49"
        EdaAvg["justify"] = "center"
        EdaAvg["text"] = "Eda Avg"
        EdaAvg["relief"] = "ridge"
        EdaAvg.place(x=75,y=125,width=100,height=40)

        eda_avg_operators = OptionMenu(self, StringVar(), "Null", ">", ">", "=")
        eda_avg_operators.place(x=325,y=125,width=50,height=40)

        eda_avg_input = tk.Text(self, height=5, width=10)
        eda_avg_input.place(x=475,y=125,width=50,height=40)

        TempAvg = tk.Button(
            self,
            text="Temp Avg",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        TempAvg["activebackground"] = "#1e90ff"
        TempAvg["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=12)
        TempAvg["font"] = ft3
        TempAvg["fg"] = "#393d49"
        TempAvg["justify"] = "center"
        TempAvg["text"] = "Temp Avg"
        TempAvg["relief"] = "ridge"
        TempAvg.place(x=75,y=175,width=100,height=40)

        temp_avg_operators = OptionMenu(self, StringVar(), "Null", ">", ">", "=")
        temp_avg_operators.place(x=325,y=175,width=50,height=40)

        temp_avg_input = tk.Text(self, height=5, width=10)
        temp_avg_input.place(x=475,y=175,width=50,height=40)

        Movement = tk.Button(
            self,
            text="Movement",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        Movement["activebackground"] = "#1e90ff"
        Movement["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=12)
        Movement["font"] = ft3
        Movement["fg"] = "#393d49"
        Movement["justify"] = "center"
        Movement["text"] = "Movement"
        Movement["relief"] = "ridge"
        Movement.place(x=75,y=225,width=100,height=40)

        movement_operators = OptionMenu(self, StringVar(), "Null", ">", ">", "=")
        movement_operators.place(x=325,y=225,width=50,height=40)

        movement_input = tk.Text(self, height=5, width=10)
        movement_input.place(x=475,y=225,width=50,height=40)

        StepCount = tk.Button(
            self,
            text="Step Count",
         #   command=lambda: controller.show_frame(Paricipant),
        )
        StepCount["activebackground"] = "#1e90ff"
        StepCount["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=12)
        StepCount["font"] = ft3
        StepCount["fg"] = "#393d49"
        StepCount["justify"] = "center"
        StepCount["text"] = "Step Count"
        StepCount["relief"] = "ridge"
        StepCount.place(x=75,y=275,width=100,height=40) 

        step_operators = OptionMenu(self, StringVar(), "Null", ">", ">", "=")
        step_operators.place(x=325,y=275,width=50,height=40)

        step_input = tk.Text(self, height=5, width=10)
        step_input.place(x=475,y=275,width=50,height=40)

        Rest = tk.Button(
            self,
            text="Rest",
           # command=lambda: controller.show_frame(Paricipant),
        )
        Rest["activebackground"] = "#1e90ff"
        Rest["bg"] = "#00ced1"
        ft3 = tkFont.Font(family='Times',size=12)
        Rest["font"] = ft3
        Rest["fg"] = "#393d49"
        Rest["justify"] = "center"
        Rest["text"] = "Rest"
        Rest["relief"] = "ridge"
        Rest.place(x=75,y=325,width=100,height=40) 

        rest_operators = OptionMenu(self, StringVar(), "Null", ">", ">", "=")
        rest_operators.place(x=325,y=325,width=50,height=40)

        rest_input = tk.Text(self, height=5, width=10)
        rest_input.place(x=475,y=325,width=50,height=40)

        ShowData = tk.Button(
            self,
            text="Show Data",
            command=lambda: controller.show_frame(MainScreen),
        )
        ShowData["activebackground"] = "#9b60ad"
        ShowData["bg"] = "#c71585"
        ft3 = tkFont.Font(family='Times',size=22)
        ShowData["font"] = ft3
        ShowData["fg"] = "#393d49"
        ShowData["justify"] = "center"
        ShowData["text"] = "Show Data"
        ShowData["relief"] = "ridge"
        ShowData.pack(side=BOTTOM, fill="both")

if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()