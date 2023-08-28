"""
	
	This module defines classes that are responsible for handling graphical user interfaces of the project.
	

	Author: Kananelo Chabeli
	Created on: 27-08-2023

"""


#*************import required modules*********
import tkinter as tk
from tkinter import ttk

#/**************Define class that holds All tkinter variables that are to be used by the main Aplication

class Variables:
	"""

	"""

	def __init__(self,container):

		"""
			Creates a new instance of the class with containter attributes initialized.
		"""
		self.container=container
		self.__add_widgets()

	def __add_widgets(self):
		self.gccAlgo=tk.StringVar(self.container,value="gcc-phat")

		#Variable that will be used to get sampling frequency fromt he user.
		self.frequencyValue=tk.IntVar(self.container, value=1000) 

		#Control variable for radio buttons that select the preffered reference sensor. Sensor 1
		#sensor 1 will be used checked by default
		self.sensorSel=tk.StringVar(self.container, value="sensor1") 


		#Variables to get sensor data from the user

		#Sensor 1 coordinates

		self.sensor1X=tk.DoubleVar(self.container, value=0.0) #Must be set, not default values will be used
		self.sensor1Y=tk.DoubleVar(self.container, value=0.0)

		#Sensor 2 coordinates

		self.sensor2X=tk.DoubleVar(self.container, value=0.0) #Must be set, not default values will be used
		self.sensor2Y=tk.DoubleVar(self.container, value=0.0)

		#Sensor 3 Coordinates

		self.sensor3X=tk.DoubleVar(self.container, value=0.0) #Must be set, not default values will be used
		self.sensor3Y=tk.DoubleVar(self.container, value=0.0)

		#Sensor 4 Coordinates

		self.sensor4X=tk.DoubleVar(self.container, value=0.0) #Must be set, not default values will be used
		self.sensor4Y=tk.DoubleVar(self.container, value=0.0)
		#Variable for Start Button

		self.startButton=tk.StringVar(self.container, value="Start Acquisition")

		#Variables to get data about dimension of the Grid

		self.xMin=tk.IntVar(self.container, value=-5)
		self.xMax=tk.IntVar(self.container, value=5)

		self.yMin=tk.IntVar(self.container, value=-5)
		self.yMax=tk.IntVar(self.container, value=5)

		#Define Variable that Display Results of the Experiment

		self.snr=tk.StringVar(self.container,value="Signal-to-Noise Ration:<Some Value>")
		self.location=tk.StringVar(self.container,value="Estimaned Location:(x,y)")
		self.time=tk.StringVar(self.container,value="Computational Time:<time> seconds")
	def reset(self):
		"""Sets All variables to thier defualt values"""
		self.gccAlgo.set("gcc-phat")

		#Variable that will be used to get sampling frequency fromt he user.
		self.frequencyValue.set(1000) 

		#Control variable for radio buttons that select the preffered reference sensor. Sensor 1
		#sensor 1 will be used checked by default
		self.sensorSel.set("sensor1") 


		#Variables to get sensor data from the user

		#Sensor 1 coordinates

		self.sensor1X.set(0.0) #Must be set, not default values will be used
		self.sensor1Y.set(0.0)

		#Sensor 2 coordinates

		self.sensor2X.set(0.0) #Must be set, not default values will be used
		self.sensor2Y.set(0.0)

		#Sensor 3 Coordinates

		self.sensor3X.set(0.0) #Must be set, not default values will be used
		self.sensor3Y.set(0.0)

		#Sensor 4 Coordinates

		self.sensor4X.set(0.0) #Must be set, not default values will be used
		self.sensor4Y.set(0.0)
		#Variable for Start Button

		self.startButton.set("Start Acquisition")

		#Variables to get data about dimension of the Grid

		self.xMin.set(-5)
		self.xMax.set(5)

		self.yMin.set(-5)
		self.yMax.set(5)

		#Define Variable that Display Results of the Experiment

		self.snr.set("Signal-to-Noise Ration:<Some Value>")
		self.location.set("Estimaned Location:(x,y)")
		self.time.set("Computational Time:<time> seconds")

#/***************Define a class that handles all Control button Widgets on the main window

class ControlPanel(tk.Frame):
	"""
	"""	
	#Costructor
	def __init__(self, mainContainer, container, x_positon=584,y_position=0,width="500",height="300",bd=7):
		"""
				
		"""
		super().__init__(container,width=width,height=height,bd=7)
		self.mainContainer=mainContainer
		self.__add_widgets()
		self.place(x=x_positon,y=y_position) #Place the window are required position

	#Method that adds widgets / buttons to this frame
	def __add_widgets(self):
		tk.Label(self,text="__________Control Panel_________",font=("Arial", 15)).pack(side=tk.TOP)
		self.placeHolder2=tk.Frame(self,width=300,height=150,bd=6)

		#Start Button
		self.startB=tk.Button(self.placeHolder2, textvariable=self.mainContainer.variable.startButton,command=EventHandler.startButton,activebackground="#8E44AD")
		self.startB.grid(row=0,column=1)

		#plot button
		self.plotB=tk.Button(self.placeHolder2,text="Plot Target",command=EventHandler.plotButtonAction,activebackground="#8E44AD")
		self.plotB.grid(row=1,column=0)

		#clear button
		self.clearB=tk.Button(self.placeHolder2, text="Clear Plot",command=EventHandler.clearButtonAction,activebackground="#8E44AD")
		self.clearB.grid(row=1,column=2)

		#quit button
		self.quitB=tk.Button(self.placeHolder2,text="Quit",command=EventHandler.quitButtonAction,activebackground="#8E44AD")
		self.quitB.grid(row=2,column=2)

		#reset button
		self.resetB=tk.Button(self.placeHolder2, text="Reset",command=EventHandler.resetButtonAction,activebackground="#8E44AD")
		self.resetB.grid(row=2, column=0)

		self.placeHolder2.pack(anchor=tk.CENTER)
		tk.Frame(self,width=70).pack(side=tk.RIGHT)


class SignalPropertiesPanel(tk.Frame):
	
	def __init__(self,mainContainer,container,bd=7,height="300"):
		super().__init__(container,bd=bd,height=height)
		
		self.mainContainer=mainContainer
		self.place(x=960,y=0)
		self.__add_widgets()


	def __add_widgets(self):
		tk.Label(self,text="_________Signal Properties_________",font=("Arial", 15)).pack(side=tk.TOP)
		self.placeHolder=tk.Frame(self,width="300",height="106",bd=6);

		self.frequency=tk.Label(self.placeHolder,text="Sampling Frequency:")
		self.frequency.place(x=5,y=10)

		self.freqInput=tk.Entry(self.placeHolder,bd=1,fg="red",width=10,textvariable=self.mainContainer.variable.frequencyValue)

		self.freqInput.place(x=150,y=10)

		self.freqUnits=tk.Label(self.placeHolder,text="Hz")
		self.freqUnits.place(x=240,y=10)

		self.message=tk.Label(self.placeHolder,text="Select GCC Algorithm Below:")
		self.message.place(x=5,y=40)

		#Do More Research on python RadioButtons
		self.gcc_phat=tk.Radiobutton(self.placeHolder,text="GCC-PHAT",fg="red", bd=5,activeforeground="blue",variable=self.mainContainer.variable.gccAlgo, value="gcc-phat")	
		self.gcc_phat.place(x=0,y=70)

		self.gcc_scot=tk.Radiobutton(self.placeHolder, text="GCC-SCOT", bd=5,variable=self.mainContainer.variable.gccAlgo,activeforeground="blue", value="gcc-scot")
		self.gcc_scot.place(x=100,y=70)

		self.gcc_ml=tk.Radiobutton(self.placeHolder, text="GCC-ML", bd=5,variable=self.mainContainer.variable.gccAlgo,activeforeground="blue", value="gcc-ml")
		self.gcc_ml.place(x=200,y=70)
		self.placeHolder.pack(anchor=tk.CENTER)




class SensorDataPanel(tk.Frame):
	

	def __init__(self,mainContainer,container,width="500", height="100"):
		super().__init__(container,width=width,height=height,bd=10)
		self.mainContainer=mainContainer
		self.place(x=15,y=0)
		self.__add_widgets()
		
	def __add_widgets(self):
		tk.Label(self,text="__________________Sensor Data__________________",font=("Arial", 15)).pack()
		self.placeHolder1=tk.Frame(self,width=300,height=100,bd=6)

 		#sensor 1 Configuration
		self.sensor1L=tk.Label(self.placeHolder1,text=" Sensor 1:")
		self.sensor1XcoordL=tk.Label(self.placeHolder1,text="x-coordinate:")
		self.sensor1xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor1X)
		self.sensor1YCoordL=tk.Label(self.placeHolder1,text="y-coordinate:")
		self.sensor1yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor1Y) #textfield for y-coordinate Input

		self.sensor1L.grid(row=0,column=0)
		self.sensor1XcoordL.grid(row=1,column=1)
		self.sensor1xVal.grid(row=1,column=2)
		self.sensor1YCoordL.grid(row=1,column=3)
		self.sensor1yVal.grid(row=1,column=4)

		#Sensor 2 Configuration
		self.sensor2L=tk.Label(self.placeHolder1,text=" Sensor 2:")
		self.sensor2XcoordL=tk.Label(self.placeHolder1,text="x-coordinate:")
		self.sensor2xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor2X)
		self.sensor2YCoordL=tk.Label(self.placeHolder1,text="y-coordinate:")
		self.sensor2yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor2Y) #textfield for y-coordinate Input

		self.sensor2L.grid(row=2,column=0)
		self.sensor2XcoordL.grid(row=3,column=1)
		self.sensor2xVal.grid(row=3,column=2)
		self.sensor2YCoordL.grid(row=3,column=3)
		self.sensor2yVal.grid(row=3,column=4)

		#Sensor 3 Configuration

		self.sensor3L=tk.Label(self.placeHolder1,text=" Sensor 3:")
		self.sensor3XcoordL=tk.Label(self.placeHolder1,text="x-coordinate:")
		self.sensor3xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor3X)
		self.sensor3YCoordL=tk.Label(self.placeHolder1,text="y-coordinate:")
		self.sensor3yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor3Y) #textfield for y-coordinate Input

		self.sensor3L.grid(row=4,column=0)
		self.sensor3XcoordL.grid(row=5,column=1)
		self.sensor3xVal.grid(row=5,column=2)
		self.sensor3YCoordL.grid(row=5,column=3)
		self.sensor3yVal.grid(row=5,column=4)

		#Sensor 4 Configuration
		self.sensor4L=tk.Label(self.placeHolder1,text=" Sensor 4:")
		self.sensor4XcoordL=tk.Label(self.placeHolder1,text="x-coordinate:")
		self.sensor4xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor4X)
		self.sensor4YCoordL=tk.Label(self.placeHolder1,text="y-coordinate:")
		self.sensor4yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor4Y) #textfield for y-coordinate Input

		self.sensor4L.grid(row=6,column=0)
		self.sensor4XcoordL.grid(row=7,column=1)
		self.sensor4xVal.grid(row=7,column=2)
		self.sensor4YCoordL.grid(row=7,column=3)
		self.sensor4yVal.grid(row=7,column=4)

		#message to promt the user to select sensor being considered as reference

		tk.Frame(self,width=50).pack(side=tk.RIGHT)
		tk.Frame(self,height=21).pack(side=tk.BOTTOM)	
		tk.Label(self.placeHolder1,text="Select reference:").grid(row=8,column=0)


		#Reference Sensor Radio Buttons

		self.sensor1=tk.Radiobutton(self.placeHolder1,text="Sensor 1",variable=self.mainContainer.variable.sensorSel, value="sensor1",fg="red",activeforeground="blue")
		self.sensor2=tk.Radiobutton(self.placeHolder1,text="Sensor 2",variable=self.mainContainer.variable.sensorSel,value="sensor2",activeforeground="blue")
		self.sensor3=tk.Radiobutton(self.placeHolder1,text="Sensor 3",variable=self.mainContainer.variable.sensorSel,value="sensor3",activeforeground="blue")
		self.sensor4=tk.Radiobutton(self.placeHolder1,text="Sensor 4",variable=self.mainContainer.variable.sensorSel,value="sensor4",activeforeground="blue")

		self.sensor1.grid(row=10,column=1)	
		self.sensor2.grid(row=10,column=2)
		self.sensor3.grid(row=10,column=3)
		self.sensor4.grid(row=10,column=4)

		self.placeHolder1.pack(anchor=tk.CENTER)

#*******************Class that implements methods that handle all events fired by button of the main Application*****************
class EventHandler:
	"""
	A class that define functions or methods that are invoked when a button is pressed on the main application
	
	All of the methods defines are class methods.
	"""	
	startPressed=False #Class variable that decides if the start method has been pressed or not

	def __init__(self):
		pass

	@classmethod
	def quitButtonAction(cls):
		"""Terminates the program when invoked"""
		cls.container.destroy()
	@classmethod			
	def setContainer(cls,container):		
		"""Sets the value of the container to the one passed in the argument returns true if the  container was set to"""
		cls.container=container

	@classmethod
	def startButton(cls):
		if(cls.startPressed):
			cls.startPressed=False
			cls.container.variable.startButton.set("Start Acquisition")
			#Invoke method that starts clock signals of Raspberry Pi

		else:
			cls.startPressed=True
			cls.container.variable.startButton.set("Stop Acquisition")


	@classmethod
	def plotButtonAction(cls):
		cls.container.variable.snr.set(f"Signal-to-Noise Ration: {20.98}dB")
		cls.container.variable.location.set(f"Estimaned Location:x_coord: {456},y_coord: {798}")
		cls.container.variable.time.set(f"Computational Time:{20.0} milliseconds")
	@classmethod
	def clearButtonAction(cls):
		pass

		#Invokemethod that remove target from the location
	@classmethod
	def resetButtonAction(cls):
		cls.container.variable.reset()
		#invoke function that clears the target plot
#**************Class that represent the results panel of the application***********************

class ResultsPanel(tk.Frame):
	"""A class that holds Labels which display the results of the system to the main application"""
	def __init__(self, mainContainer, container, width="100", height="100", x_position=960, y_position=154):
		"""Creates a new instance of the class with the given container and at the given location"""
		super().__init__(container,width=width,height=height)
		
		self.mainContainer=mainContainer
		self.__add_widgets()
		self.place(x=x_position,y=y_position)
		#Not completed
	def __add_widgets(self):
		tk.Label(self,text="_____________Results______________",font=("Arial", 15)).pack(side=tk.TOP)
		self.center=tk.Frame(self,width="100", height="100")	
		self.targetLocation=tk.Label(self.center,textvariable=self.mainContainer.variable.location)
		self.targetLocation.grid(row=0,column=0) #place the label nicely

		self.signalToNoise=tk.Label(self.center,textvariable=self.mainContainer.variable.snr)
		self.signalToNoise.grid(row=1,column=0)

		self.computationalTime=tk.Label(self.center,textvariable=self.mainContainer.variable.time)
		self.computationalTime.grid(row=2,column=0)
		tk.Frame(self,width=105).pack(side=tk.RIGHT)
		tk.Frame(self,height=57).pack(side=tk.BOTTOM)
		self.center.pack(anchor=tk.CENTER)	



	def setTargetLocation(self,loc):
		"""Sets the value of the target location Label to the string passed into the argument"""
		self.mainContainer.variable.location.set(loc)

	def setSignalToNoise(self,ratio):
		"""Sets the value of the signal to noise ratio Label to the string passed into the argument"""
		self.mainContainer.variable.snr.set(ratio)

	def setTime(self, newTime):
		"""Sets the value of the time label to the string passed"""
		self.mainContainer.variable.time.set(newTime)



#**********Define class that represents the main control frame of the application**************************

class MainControl(tk.Frame):
	"""Class that represents the main control pannel of the application"""
	def __init__(self,container,color,width,height):
		
		super().__init__(container,width=width,height=height,bg=color,bd=10)
		self.pack(side=tk.TOP) #place the control button at the top

#************************Class that add coordinate system into the user************************************

class CoordinateSystem(tk.Frame):
	"""
		Class that represents the c
	"""
class GridDimensions(tk.Frame):
	"""
		A Class that represents that panel that inputs Grid dimensions from the user
	"""
	def __init__(self,mainContainer,container,bd=7,width="400",height="100"):
		super().__init__(container,width=width,height=height,bd=bd)
		self.mainContainer=mainContainer
		self.__add_widgets()
		self.place(x=574, y=154)

	def __add_widgets(self):
		tk.Label(self,text="________Grid Dimensions___________",font=("Arial", 15)).pack(side=tk.TOP)
		self.placeHolder3=tk.Frame(self, bd=6,width="400",height="100")

		#Minimum x-coordinate
		self.XminLabel=tk.Label(self.placeHolder3, text="Xmin:")
		self.XminVal=tk.Entry(self.placeHolder3,width=10,textvariable=self.mainContainer.variable.xMin)
		#Maximum x-coordinate
		
		self.XmaxLabel=tk.Label(self.placeHolder3, text="Xmax:")
		self.XmaxVal=tk.Entry(self.placeHolder3,width=10,textvariable=self.mainContainer.variable.xMax)
		#Minimum y-coordinate
		
		self.YminLabel=tk.Label(self.placeHolder3, text="Ymin:")
		
		self.YminVal=tk.Entry(self.placeHolder3,width=10,textvariable=self.mainContainer.variable.yMin)
		#Maximum y-Coordinate
		
		self.YmaxLabel=tk.Label(self.placeHolder3, text="Xmax:")
		self.YmaxVal=tk.Entry(self.placeHolder3,width=10,textvariable=self.mainContainer.variable.yMax)

		#add labels
		self.XminLabel.grid(row=0,column=0)
		self.XminVal.grid(row=0, column=1)

		self.XmaxLabel.grid(row=1,column=0)
		self.XmaxVal.grid(row=1, column=1)

		self.YminLabel.grid(row=2,column=0)
		self.YminVal.grid(row=2, column=1)

		self.YmaxLabel.grid(row=3,column=0)
		self.YmaxVal.grid(row=3, column=1)

		tk.Frame(self, width=100, height=106).pack(side=tk.LEFT)
		tk.Frame(self, width=120, height=106).pack(side=tk.RIGHT)

		tk.Frame(self).pack(side=tk.BOTTOM)
		self.placeHolder3.pack(anchor=tk.CENTER)


#************************************Main Application***************************
class Application(tk.Tk):
	"""
		A class	Represents the main Application
		
	"""
	def __init__(self,width,height,title):
		super().__init__()
		self.geometry(width+"x"+height)
		EventHandler.setContainer(self)
		self.variable=Variables(self)
		self.title(title)
		self.mainControl=MainControl(self,"black","1500","320")
		self.gridDimensions=GridDimensions(self,self.mainControl)
		self.signalPropertiesPanel=SignalPropertiesPanel(self,self.mainControl)
		self.sensors=SensorDataPanel(self,self.mainControl)
		self.res=ResultsPanel(self,self.mainControl)
		self.control=ControlPanel(self,self.mainControl)

	def display(self):
		self.mainloop()


def main():
	myApp=Application("1500","800","Acoustic Localization")
	myApp.display()

def quit(app):
		app.destroy()
if __name__ == '__main__':
	main()