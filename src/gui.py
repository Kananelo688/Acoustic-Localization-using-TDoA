"""
    The following program defines Graphical user interface that will interact the user with the systems that implements acoustic triangulation algorithms

@author: Kananelo Chabeli
@Created on: 25th August 2023
"""

#*************************************Imports******************************************************************************

import tkinter as tk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np

#*****************************************Set up the Main Window of the Appliction*****************************************

mainWindow=tk.Tk() #creates a main window object
mainWindow.title("Acoustic Localization System") #set title of the window
mainWindow.geometry("1500x800")


#*****************************************Global Variables******************************************************************


#This the control variable for radio buttons that select required gcc algorithms
#gcc-phat algorithm is selected by default   
gccAlgo=tk.StringVar(mainWindow,value="gcc-phat")

#Variable that will be used to get sampling frequency fromt he user.
frequencyValue=tk.IntVar(mainWindow, value=1000) 

#Control variable for radio buttons that select the preffered reference sensor. Sensor 1
#sensor 1 will be used checked by default
sensorSel=tk.StringVar(mainWindow, value="sensor1") 


#Variables to get sensor data from the user

#Sensor 1 coordinates
sensor1X=tk.DoubleVar(mainWindow, value=0.0) #Must be set, not default values will be used
sensor1Y=tk.DoubleVar(mainWindow, value=0.0)

#Sensor 2 coordinates

sensor2X=tk.DoubleVar(mainWindow, value=0.0) #Must be set, not default values will be used
sensor2Y=tk.DoubleVar(mainWindow, value=0.0)

#Sensor 3 Coordinates

sensor3X=tk.DoubleVar(mainWindow, value=0.0) #Must be set, not default values will be used
sensor3Y=tk.DoubleVar(mainWindow, value=0.0)

#Sensor 4 Coordinates

sensor4X=tk.DoubleVar(mainWindow, value=0.0) #Must be set, not default values will be used
sensor4Y=tk.DoubleVar(mainWindow, value=0.0)
#Variable for Start Button

startButton=tk.StringVar(mainWindow, value="Start Acquisition")

#Variables to get data about dimension of the Grid

xMin=tk.IntVar(mainWindow, value=-5)
xMax=tk.IntVar(mainWindow, value=5)

yMin=tk.IntVar(mainWindow, value=-5)
yMax=tk.IntVar(mainWindow, value=5)

#Define Variable that Display Results of the Experiment
snr=tk.StringVar(value="Signal-to-Noise Ration:<Some Value>")
location=tk.StringVar(value="Estimaned Location:(x,y)")
time=tk.StringVar(value="Computational Time:<time> seconds")

#************************************Function Invoked when button are pressed**********************************


def quit():
    """Terminates the program when run"""
    mainWindow.destroy()

#**********************************Panel that houses all User Widgets***************************************

control=tk.Frame(mainWindow,width="1500",height="300",bg="black",bd=10)



#******************************Defining control panel that takes inputs of the user regarding signal properties******************

signalPanel=tk.Frame(control,bd=7,height="300") #panel to add all other widgets

panelLabel=tk.Label(signalPanel,text="____________________Signal Properties_____________")# define a heading of this panel
panelLabel.pack(side=tk.TOP)

placeHolder=tk.Frame(signalPanel,width="300",height="106",bd=6);

frequency=tk.Label(placeHolder,text="Sampling Frequency:")
frequency.place(x=5,y=10)

freqInput=tk.Entry(placeHolder,bd=1,fg="red",width=10,textvariable=frequencyValue)
freqInput.place(x=150,y=10)

freqUnits=tk.Label(placeHolder,text="Hz")
freqUnits.place(x=240,y=10)

message=tk.Label(placeHolder,text="Select GCC Algorithm Below:")
message.place(x=5,y=40)

#Do More Research on python RadioButtons
gcc_phat=tk.Radiobutton(placeHolder,text="GCC-PHAT",fg="red", bd=5,activeforeground="blue",variable=gccAlgo, value="gcc-phat")
gcc_phat.place(x=0,y=70)

gcc_scot=tk.Radiobutton(placeHolder, text="GCC-SCOT", bd=5,variable=gccAlgo,activeforeground="blue", value="gcc-scot")
gcc_scot.place(x=100,y=70)

gcc_ml=tk.Radiobutton(placeHolder, text="GCC-ML", bd=5,variable=gccAlgo,activeforeground="blue", value="gcc-ml")
gcc_ml.place(x=200,y=70)
#*****************************Define Panel that will display results of the system***********************************************
results=tk.Frame(control, width="100", height="100")
center=tk.Frame(results,width="100", height="100")

#Label that displays SNR of the system
snrLabel=tk.Label(center,textvariable=snr)
snrLabel.grid(row=0,column=0)

#Label that displays target location
tk.Label(results,text="_______________Results___________________").pack(side=tk.TOP)

tk.Frame(results,width=129).pack(side=tk.RIGHT)
tk.Frame(results,height=57).pack(side=tk.BOTTOM)
locLabel=tk.Label(center,textvariable=location)
locLabel.grid(row=1,column=0) 
#Label that displays computational time in seconds
timeLabel=tk.Label(center,textvariable=time)
timeLabel.grid(row=2,column=0)

center.pack(anchor=tk.CENTER)
tk.Frame(signalPanel,width=70).pack(side=tk.RIGHT)
placeHolder.pack(anchor=tk.CENTER)

#********************************Define Panel for Interfacing with the user about Sensor Information*****************************

sensorFrame=tk.Frame(control, width="500", height="100",bd=7)
sensorLabel=tk.Label(sensorFrame,text="___________________________Sensor Data_____________________________")
sensorLabel.pack()

placeHolder1=tk.Frame(sensorFrame,width=300,height=100,bd=6)

 #sensor 1 Configuration
sensor1L=tk.Label(placeHolder1,text=" Sensor 1:")
sensor1XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor1xVal=tk.Entry(placeHolder1,width=10,textvariable=sensor1X)
sensor1YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor1yVal=tk.Entry(placeHolder1,width=10,textvariable=sensor2X) #textfield for y-coordinate Input

sensor1L.grid(row=0,column=0)
sensor1XcoordL.grid(row=1,column=1)
sensor1xVal.grid(row=1,column=2)
sensor1YCoordL.grid(row=1,column=3)
sensor1yVal.grid(row=1,column=4)

#Sensor 2 Configuration
sensor2L=tk.Label(placeHolder1,text=" Sensor 2:")
sensor2XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor2xVal=tk.Entry(placeHolder1,width=10,textvariable=sensor2X)
sensor2YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor2yVal=tk.Entry(placeHolder1,width=10,textvariable=sensor2X) #textfield for y-coordinate Input

sensor2L.grid(row=2,column=0)
sensor2XcoordL.grid(row=3,column=1)
sensor2xVal.grid(row=3,column=2)
sensor2YCoordL.grid(row=3,column=3)
sensor2yVal.grid(row=3,column=4)

#Sensor 3 Configuration

sensor3L=tk.Label(placeHolder1,text=" Sensor 3:")
sensor3XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor3xVal=tk.Entry(placeHolder1,width=10,textvariable=sensor3X)
sensor3YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor3yVal=tk.Entry(placeHolder1,width=10,textvariable=sensor3X) #textfield for y-coordinate Input

sensor3L.grid(row=4,column=0)
sensor3XcoordL.grid(row=5,column=1)
sensor3xVal.grid(row=5,column=2)
sensor3YCoordL.grid(row=5,column=3)
sensor3yVal.grid(row=5,column=4)

#Sensor 4 Configuration
sensor4L=tk.Label(placeHolder1,text=" Sensor 4:")
sensor4XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor4xVal=tk.Entry(placeHolder1,width=10,textvariable=sensor4X)
sensor4YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor4yVal=tk.Entry(placeHolder1,width=10,textvariable=sensor4X) #textfield for y-coordinate Input

sensor4L.grid(row=6,column=0)
sensor4XcoordL.grid(row=7,column=1)
sensor4xVal.grid(row=7,column=2)
sensor4YCoordL.grid(row=7,column=3)
sensor4yVal.grid(row=7,column=4)

#message to promt the user to select sensor being considered as reference

tk.Frame(sensorFrame,width=50).pack(side=tk.RIGHT)
tk.Frame(sensorFrame,height=19).pack(side=tk.BOTTOM)
message2=tk.Label(placeHolder1,text="Select reference:")

message2.grid(row=8,column=0)


#Modify this After reading more about Radio buttons

sensor1=tk.Radiobutton(placeHolder1,text="Sensor 1",variable=sensorSel, value="sensor1",fg="red",activeforeground="blue")
sensor2=tk.Radiobutton(placeHolder1,text="Sensor 2",variable=sensorSel,value="sensor2",activeforeground="blue")
sensor3=tk.Radiobutton(placeHolder1,text="Sensor 3",variable=sensorSel,value="sensor3",activeforeground="blue")
sensor4=tk.Radiobutton(placeHolder1,text="Sensor 4",variable=sensorSel,value="sensor4",activeforeground="blue")

sensor1.grid(row=10,column=1)
sensor2.grid(row=10,column=2)
sensor3.grid(row=10,column=3)
sensor4.grid(row=10,column=4)

placeHolder1.pack(anchor=tk.CENTER)


#*****************************************Define control Buttons*******************************
controlPanel=tk.Frame(control,width="500",height="300",bd=7)

panelLabel=tk.Label(controlPanel,text="______________________Control Panel_________________")
panelLabel.pack(side=tk.TOP)

placeHolder2=tk.Frame(controlPanel,width=300,height=150,bd=6)
placeHolder.pack(anchor=tk.CENTER)

#Button that starts signal Acquisition
startB=tk.Button(placeHolder2, textvariable=startButton,activebackground="#8E44AD")
startB.grid(row=0,column=1)

#Button that stops signal Acquisition

#Button that plots the target location on the grid
plotB=tk.Button(placeHolder2,text="Plot Target",activebackground="#8E44AD")
plotB.grid(row=1,column=0)
#Button that clears the plot
clearB=tk.Button(placeHolder2, text="Clear Plot",activebackground="#8E44AD")
clearB.grid(row=1,column=2)
#Button the reset the given data and starts from scratch
resetB=tk.Button(placeHolder2, text="Reset",activebackground="#8E44AD")
resetB.grid(row=2, column=0)
#Button that quits the program(Exits the program)
quitB=tk.Button(placeHolder2,text="Quit",command=quit,activebackground="#8E44AD")
quitB.grid(row=2,column=2)

tk.Frame(controlPanel,width=50).pack(side=tk.RIGHT)
placeHolder2.pack(anchor=tk.CENTER)


#******************************************Define Grid dimensions panel***********************************************
gridDim=tk.Frame(control,bd=7,width="400",height="100")

gridDimLabel=tk.Label(gridDim,text="________________Grid Dimesntions_________________")
gridDimLabel.pack(side=tk.TOP)
placeHolder3=tk.Frame(gridDim, bd=6,width="400",height="100")



#Minimum x-coordinate
XminLabel=tk.Label(placeHolder3, text="Xmin:")
XminVal=tk.Entry(placeHolder3,width=10,textvariable=xMin)
#Maximum x-coordinate
XmaxLabel=tk.Label(placeHolder3, text="Xmax:")
XmaxVal=tk.Entry(placeHolder3,width=10,textvariable=xMax)
#Minimum y-coordinate
YminLabel=tk.Label(placeHolder3, text="Ymin:")
YminVal=tk.Entry(placeHolder3,width=10,textvariable=yMin)
#Maximum y-Coordinate
YmaxLabel=tk.Label(placeHolder3, text="Xmax:")
YmaxVal=tk.Entry(placeHolder3,width=10,textvariable=yMax)

#add labels
XminLabel.grid(row=0,column=0)
XminVal.grid(row=0, column=1)

XmaxLabel.grid(row=1,column=0)
XmaxVal.grid(row=1, column=1)

YminLabel.grid(row=2,column=0)
YminVal.grid(row=2, column=1)

YmaxLabel.grid(row=3,column=0)
YmaxVal.grid(row=3, column=1)

temp1=tk.Frame(gridDim, width=103, height=106)
temp1.pack(side=tk.LEFT)

temp2=tk.Frame(gridDim, width=140, height=106)
temp2.pack(side=tk.RIGHT)

tk.Frame(gridDim).pack(side=tk.BOTTOM)
placeHolder3.pack(anchor=tk.CENTER)
#**************************************************Embedding Matplot Figure in tkinter***************************

# First configure the plot so that the rectangular coodinate system is displayed on the grid

figure,axes=plt.subplots(figsize=(14,4))
figure.patch.set_facecolor('#ffffff')
axes.set_aspect("equal")
#Appy Ranges to Axes

axes.set(xlim=(xMin.get()-1,xMax.get()+1),ylim=(yMin.get()-1,yMax.get()+1))

#set the both axes to zero positon

axes.spines['bottom'].set_position('zero')
axes.spines['left'].set_position('zero')

#Hide the top and the right spine
axes.spines['top'].set_visible(False)
axes.spines['right'].set_visible(False)

#Set x and y labels and add origin label
axes.set_ylabel('$y$',size=14,labelpad=-24,loc="top")
axes.set_xlabel('$x$',size=14,labelpad=-21, loc="right",rotation=0)
plt.text(0.49,0.49,r"$o$",ha='right',va='top',transform=axes.transAxes, horizontalalignment='center',fontsize=14)

#creates x and y ticks and apply them both axes
x_ticks=np.arange(xMin.get(),xMax.get()+1,1)
y_ticks=np.arange(yMin.get(),yMax.get()+1,1)

axes.set_xticks(x_ticks[x_ticks !=0])
axes.set_yticks(y_ticks[y_ticks !=0])
axes.set_xticks(np.arange(xMin.get(),xMax.get()+1),minor=True)
axes.set_yticks(np.arange(yMin.get(),yMax.get()+1),minor=True)

#Add grid
axes.grid(which='both',color='gray',linewidth=1,linestyle='-',alpha=0.2)

#Create a canvas object
frame=tk.Frame(mainWindow)
canvas=FigureCanvasTkAgg(figure,frame)
canvas.get_tk_widget().pack(anchor=tk.CENTER); #this adds the figure into matplotlib

frame.grid(row=1,column=0)

#this updates changes on the plots



signalPanel.place(x=960,y=0) #add signal Properties to the main window
sensorFrame.place(x=0,y=0)# sensor data Panel
controlPanel.place(x=550,y=0) #control buttons
gridDim.place(x=550, y=145)
results.place(x=960,y=145)
tk.Frame(mainWindow,height="50").grid(row=2,column=0)
control.grid(row=0,column=0)
#sensorFrame.grid(row=3,column=1) 
mainWindow.mainloop()# invoke the main loop


