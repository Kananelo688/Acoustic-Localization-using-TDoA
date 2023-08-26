"""
    The following program defines Graphical user interface that will interact the user with the systems that implements acoustic triangulation algorithms

@author: Kananelo Chabeli
@Created on: 25th August 2023
"""

#import tkinter python packgae

import tkinter as tk

#create a main window object

mainWindow=tk.Tk() #creates a main window object
mainWindow.title("Acoustic Localization System") #set title of the window
mainWindow.geometry("2000x800")



#Define control Panel that houses all user inputs and buttons

control=tk.Frame(mainWindow,width="2000",height="300",bg="black",bd=10)



"""Defining control panel that takes inputs of the user regarding signal properties"""

signalPanel=tk.Frame(control,bd=7,bg="black") #panel to add all other widgets

panelLabel=tk.Label(signalPanel,text="____________________Signal Properties_____________")# define a heading of this panel
panelLabel.pack(side=tk.TOP)

placeHolder=tk.Frame(signalPanel,width="300",height="200",bd=6);

frequency=tk.Label(placeHolder,text="Sampling Frequency:")
frequency.place(x=5,y=10)

freqInput=tk.Entry(placeHolder,bd=1,fg="red",width=10)
freqInput.place(x=150,y=10)

freqUnits=tk.Label(placeHolder,text="Hz")
freqUnits.place(x=240,y=10)

message=tk.Label(placeHolder,text="Select GCC Algorithm Below:")
message.place(x=5,y=40)

#Do More Research on python RadioButtons
gcc_phat=tk.Radiobutton(placeHolder,text="GCC-PHAT")
gcc_phat.place(x=0,y=70)

gcc_scot=tk.Radiobutton(placeHolder, text="GCC-SCOT")
gcc_scot.place(x=100,y=70)

gcc_ml=tk.Radiobutton(placeHolder, text="GCC-ML")
gcc_ml.place(x=200,y=70)


placeHolder.pack(anchor=tk.CENTER)

"""Define Panel for Interfacing with the user about Sensor Information"""

sensorFrame=tk.Frame(control, width="500", height="100",bd=7,bg="black")
sensorLabel=tk.Label(sensorFrame,text="_______________Sensor Data_________________")
sensorLabel.pack()

placeHolder1=tk.Frame(sensorFrame,width=300,height=100,bd=6)

 #sensor 1 Configuration
sensor1L=tk.Label(placeHolder1,text=" Sensor 1:")
sensor1XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor1xVal=tk.Entry(placeHolder1,width=20)
sensor1YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor1yVal=tk.Entry(placeHolder1,width=20) #textfield for y-coordinate Input

sensor1L.grid(row=0,column=0)
sensor1XcoordL.grid(row=1,column=1)
sensor1xVal.grid(row=1,column=2)
sensor1YCoordL.grid(row=1,column=3)
sensor1yVal.grid(row=1,column=4)

#Sensor 2 Configuration
sensor2L=tk.Label(placeHolder1,text=" Sensor 2:")
sensor2XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor2xVal=tk.Entry(placeHolder1,width=20)
sensor2YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor2yVal=tk.Entry(placeHolder1,width=20) #textfield for y-coordinate Input

sensor2L.grid(row=2,column=0)
sensor2XcoordL.grid(row=3,column=1)
sensor2xVal.grid(row=3,column=2)
sensor2YCoordL.grid(row=3,column=3)
sensor2yVal.grid(row=3,column=4)

#Sensor 3 Configuration

sensor3L=tk.Label(placeHolder1,text=" Sensor 3:")
sensor3XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor3xVal=tk.Entry(placeHolder1,width=20)
sensor3YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor3yVal=tk.Entry(placeHolder1,width=20) #textfield for y-coordinate Input

sensor3L.grid(row=4,column=0)
sensor3XcoordL.grid(row=5,column=1)
sensor3xVal.grid(row=5,column=2)
sensor3YCoordL.grid(row=5,column=3)
sensor3yVal.grid(row=5,column=4)

#Sensor 4 Configuration
sensor4L=tk.Label(placeHolder1,text=" Sensor 4:")
sensor4XcoordL=tk.Label(placeHolder1,text="x-coordinate:")
sensor4xVal=tk.Entry(placeHolder1,width=20)
sensor4YCoordL=tk.Label(placeHolder1,text="y-coordinate:")
sensor4yVal=tk.Entry(placeHolder1,width=20) #textfield for y-coordinate Input

sensor4L.grid(row=6,column=0)
sensor4XcoordL.grid(row=7,column=1)
sensor4xVal.grid(row=7,column=2)
sensor4YCoordL.grid(row=7,column=3)
sensor4yVal.grid(row=7,column=4)

#message to promt the user to select sensor being considered as reference

message2=tk.Label(placeHolder1,text="Select reference:")

message2.grid(row=8,column=0)


#Modify this After reading more about Radio buttons

sensor1=tk.Radiobutton(placeHolder1,text="Sensor 1")
sensor2=tk.Radiobutton(placeHolder1,text="Sensor 2")
sensor3=tk.Radiobutton(placeHolder1,text="Sensor 3")
sensor4=tk.Radiobutton(placeHolder1,text="Sensor 4")

sensor1.grid(row=10,column=1)
sensor2.grid(row=10,column=2)
sensor3.grid(row=10,column=3)
sensor4.grid(row=10,column=4)

placeHolder1.pack(anchor=tk.CENTER)




"""Define control Buttons"""
controlPanel=tk.Frame(control,width="500",height="300",bd=7,bg="black")

panelLabel=tk.Label(controlPanel,text="____________Control Panel___________")
panelLabel.pack(side=tk.TOP)

placeHolder2=tk.Frame(controlPanel,width=300,height=150,bd=6)
placeHolder.pack(anchor=tk.CENTER)

#Button that starts signal Acquisition
startB=tk.Button(placeHolder2, text="Start Acquisition")
startB.grid(row=0,column=0)

#Button that stops signal Acquisition
stopB=tk.Button(placeHolder2, text="Stop Acquisition")
stopB.grid(row=0,column=1)
#Button that plots the target location on the grid
plotB=tk.Button(placeHolder2,text="Plot Target")
plotB.grid(row=1,column=0)
#Button that clears the plot
clearB=tk.Button(placeHolder2, text="Clear Plot")
clearB.grid(row=1,column=1)
#Button the reset the given data and starts from scratch
resetB=tk.Button(placeHolder2, text="Reset")
resetB.grid(row=2, column=0)
#Button that quits the program(Exits the program)
quitB=tk.Button(placeHolder2,text="Quit")
quitB.grid(row=2,column=1)

placeHolder2.pack(anchor=tk.CENTER)


"""Define Grid dimensions panel and place it in the main window"""
gridDim=tk.Frame(control,bd=7,bg="black",width="400",height="100")

gridDimLabel=tk.Label(gridDim,text="_____Grid Dimesntions_____")
gridDimLabel.pack(side=tk.TOP)
placeHolder3=tk.Frame(gridDim, bd=6,width="400",height="100")



#Minimum x-coordinate
XminLabel=tk.Label(placeHolder3, text="Xmin:")
XminVal=tk.Entry(placeHolder3,width=25)
#Maximum x-coordinate
XmaxLabel=tk.Label(placeHolder3, text="Xmax:")
XmaxVal=tk.Entry(placeHolder3,width=25)
#Minimum y-coordinate
YminLabel=tk.Label(placeHolder3, text="Ymin:")
YminVal=tk.Entry(placeHolder3,width=25)
#Maximum y-Coordinate
YmaxLabel=tk.Label(placeHolder3, text="Xmax:")
YmaxVal=tk.Entry(placeHolder3,width=25)

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
sensorFrame.place(x=645,y=0)# sensor data Panel
controlPanel.place(x=358,y=0) #control buttons
gridDim.place(x=358, y=140)

control.pack()
#sensorFrame.grid(row=3,column=1) 
mainWindow.mainloop()# invoke the main loop

