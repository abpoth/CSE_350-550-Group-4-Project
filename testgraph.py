# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

def g1(): #filename, start, end, group, ect
    date_t = (r'\20200118')
    participant = (r'\310')
    filename =  (r"Dataset"+date_t+participant+"\summary.csv")
    df = pd.read_csv(filename, skiprows=[1])
    x = ("Datetime (UTC)")
    # Placing the plots in the plane
    row, cols = 7,1
    fig, ax = plt.subplots(figsize=(7,7), dpi=100,nrows=row,ncols=cols, sharex=True)
    fig.subplots_adjust(hspace=.6, wspace=.4,bottom=.5,top=1)
    p1 = ax[0];p2 = ax[1];p3 = ax[2];p4 = ax[3];p5 = ax[4]
    p6 = ax[5];p7 = ax[6]
    fromx = 0; tox1 = 1405
    df.iloc[fromx:tox1].plot(x, "Acc magnitude avg",ax=p1)
    df.iloc[fromx:tox1].plot(x, "Eda avg", ax=p2)
    df.iloc[fromx:tox1].plot(x, "Temp avg", ax=p3)
    df.iloc[fromx:tox1].plot(x, "Movement intensity", ax=p4)
    df.iloc[fromx:tox1].plot(x, "Steps count", ax=p5)
    df.iloc[fromx:tox1].plot(x, "Rest", ax=p6)

    # Packing all the plots and displaying them
    plt.tight_layout()
    plt.show()
g1()