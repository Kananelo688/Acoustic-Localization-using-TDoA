"""
    The following program defines Graphical user interface that will interact the user with the systems that implements acoustic triangulation algorithms

@author: Kananelo Chabeli
@Created on: 25th August 2023
"""

#*************************************Imports******************************************************************************

import tkinter as tk








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

xMin=tk.DoubleVar(mainWindow, value=0.0)
xMax=tk.DoubleVar(mainWindow, value=0.0)

yMin=tk.DoubleVar(mainWindow, value=0.0)
yMax=tk.DoubleVar(mainWindow, value=0.0)

#**********************************Panel that house all User Widgets***************************************

control=tk.Frame(mainWindow,width="1500",height="300",bg="black",bd=10)



#******************************Defining control panel that takes inputs of the user regarding signal properties******************

signalPanel=tk.Frame(control,bd=7,bg="black") #panel to add all other widgets

panelLabel=tk.Label(signalPanel,text="____________________Signal Properties_____________")# define a heading of this panel
panelLabel.pack(side=tk.TOP)

placeHolder=tk.Frame(signalPanel,width="300",height="200",bd=6);

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

placeHolder.pack(anchor=tk.CENTER)

#****************************Define Panel for Interfacing with the user about Sensor Information*********************

sensorFrame=tk.Frame(control, width="500", height="100",bd=7,bg="black")
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




#*****************************************Define control Buttons"""
controlPanel=tk.Frame(control,width="500",height="300",bd=7,bg="black")

panelLabel=tk.Label(controlPanel,text="____________Control Panel___________")
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
quitB=tk.Button(placeHolder2,text="Quit",activebackground="#8E44AD")
quitB.grid(row=2,column=2)

placeHolder2.pack(anchor=tk.CENTER)


"""Define Grid dimensions panel and place it in the main window"""
gridDim=tk.Frame(control,bd=7,bg="black",width="400",height="100")

gridDimLabel=tk.Label(gridDim,text="_____________Grid Dimesntions______________")
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

placeHolder3.pack(anchor=tk.CENTER)




signalPanel.place(x=0,y=0) #add signal Properties to the main window
sensorFrame.place(x=700,y=0)# sensor data Panel
controlPanel.place(x=357,y=0) #control buttons
gridDim.place(x=328, y=140)

control.pack()
#sensorFrame.grid(row=3,column=1) 
mainWindow.mainloop()# invoke the main loop

