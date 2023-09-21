"""
	
	This module defines classes that are responsible for handling graphical user interfaces of the project.
	

	Author: Kananelo Chabeli
	Created on: 27-08-2023

"""

#*************import required modules*********

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import threading
import time
from multiprocessing import Process
from matplotlib.animation import FuncAnimation
import os
import glob
import signalProcessing as sp
import signalAcquisition as sa

import triangulation as tr

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

		#Initial Target Location for Optimization Algorithm
		self.initialX=tk.IntVar(self.container,value=0)
		self.initialY=tk.IntVar(self.container,value=0)

		#Actual Target Location(Need when testing Multilaaterization)


		self.actualX=tk.IntVar(self.container,value=0)
		self.actualY=tk.IntVar(self.container,value=0)

		#Sensor 1 Coords

		self.sensor1X=tk.IntVar(self.container, value=0) #Must be set, not default values will be used
		self.sensor1Y=tk.IntVar(self.container, value=0)

		#Sensor 2 coords

		self.sensor2X=tk.IntVar(self.container, value=0) #Must be set, not default values will be used
		self.sensor2Y=tk.IntVar(self.container, value=0)

		#Sensor 3 Coords

		self.sensor3X=tk.IntVar(self.container, value=0) #Must be set, not default values will be used
		self.sensor3Y=tk.IntVar(self.container, value=0)

		#Sensor 4 Coords

		self.sensor4X=tk.IntVar(self.container, value=0) #Must be set, not default values will be used
		self.sensor4Y=tk.IntVar(self.container, value=0)
		#Variable for Start Button

		self.startButton=tk.StringVar(self.container, value="Start Acquisition")


		self.xMin=tk.IntVar(self.container,value=0)
		self.yMin=tk.IntVar(self.container,value=0)
		self.xMax=tk.IntVar(self.container,value=80)
		self.yMax=tk.IntVar(self.container,value=50)




	def reset(self):
		"""Sets All variables to thier defualt values"""
		self.gccAlgo.set("gcc-phat")

		#Variable that will be used to get sampling frequency fromt he user.
		self.frequencyValue.set(1000) 

		#Control variable for radio buttons that select the preffered reference sensor. Sensor 1
		#sensor 1 will be used checked by default
		self.sensorSel.set("sensor1") 

		#Variables to get sensor data from the user

		#Sensor 1 coords

		self.sensor1X.set(0) #Must be set, not default values will be used
		self.sensor1Y.set(0)

		#Sensor 2 coords

		self.sensor2X.set(0) #Must be set, not default values will be used
		self.sensor2Y.set(0)

		#Sensor 3 Coords

		self.sensor3X.set(0) #Must be set, not default values will be used
		self.sensor3Y.set(0)

		#Sensor 4 Coords

		self.sensor4X.set(0) #Must be set, not default values will be used
		self.sensor4Y.set(0)
		#Variable for Start Button

		self.startButton.set("Start Acquisition")
		self.initialX.set(0)
		self.initialY.set(0)

		#Actual Target Location(Need when testing Multilaaterization)


		self.actualX.set(0)
		self.actualY.set(0)

#/***************Define a class that handles all Control button Widgets on the main window*********************************

class ControlPanel(tk.Frame):
	"""
	"""	
	#Costructor
	def __init__(self, mainContainer, container, x_positon=500,y_position=0,width="500",height="200",bd=20):
		"""
				
		"""
		super().__init__(container,width=width,height=height,bd=20,bg="#9ef051")
		self.mainContainer=mainContainer
		self.__add_widgets()
		self.place(x=x_positon,y=y_position) #Place the window are required position

	#Method that adds widgets / buttons to this frame
	def __add_widgets(self):
		tk.Label(self,text="__________Control Panel_________",font=("Arial", 12),bg="#9ef051").pack(side=tk.TOP)
		self.placeHolder2=tk.Frame(self,width=300,height=100,bd=6,bg="black")

		#Start Button
		self.startB=tk.Button(self.placeHolder2,bd=5, textvariable=self.mainContainer.variable.startButton,command=EventHandler.startButton,activebackground="#FD349C")
		self.startB.grid(row=0,column=1)

		#plot button
		self.plotB=tk.Button(self.placeHolder2,text="  Plot  ",bd=5,command=EventHandler.plotButtonAction,
			activebackground="#FD349C")
		self.plotB.grid(row=0,column=0)

		#clear button
		self.clearB=tk.Button(self.placeHolder2, text=" Clear ",bd=5,command=EventHandler.clearButtonAction,activebackground="#FD349C")
		self.clearB.grid(row=1,column=0)

		#quit button
		self.quitB=tk.Button(self.placeHolder2,text="Exit",bd=5,command=EventHandler.quitButtonAction,activebackground="#FD349C")
		self.quitB.grid(row=0,column=3)
		tk.Button(self.placeHolder2,text="Play",bd=5,activebackground="#FD349C",command=EventHandler.playButtonAction).grid(row=1,column=3)
		#reset button
		self.resetB=tk.Button(self.placeHolder2, text="          Reset        ",bd=5,command=EventHandler.resetButtonAction,activebackground="#FD349C")
		self.resetB.grid(row=1, column=1)

		self.placeHolder2.pack(anchor=tk.CENTER)
		tk.Frame(self,width=70).pack(side=tk.RIGHT)


class SignalPropertiesPanel(tk.Frame):
	
	def __init__(self,mainContainer,container,bd=20,bg="#9ef051",height="300"):
		super().__init__(container,bd=bd,bg=bg,height=height)
		
		self.mainContainer=mainContainer
		self.place(x=500,y=150)
		self.__add_widgets()

	def __add_widgets(self):
		tk.Label(self,text="_________Signal Properties_________",font=("Arial", 12),bg="#9ef051").pack(side=tk.TOP)
		self.placeHolder=tk.Frame(self,width="300",height="106",bd=6,bg="black");

		self.frequency=tk.Label(self.placeHolder,text="Sampling Frequency:",bg="#9ef051")
		self.frequency.place(x=5,y=10)

		self.freqInput=tk.Entry(self.placeHolder,bd=1,fg="red",width=10,textvariable=self.mainContainer.variable.frequencyValue)

		self.freqInput.place(x=150,y=10)

		self.freqUnits=tk.Label(self.placeHolder,text="Hz",bg="#9ef051")
		self.freqUnits.place(x=240,y=10)

		self.message=tk.Label(self.placeHolder,text="Select GCC Algorithm Below:",bg="#9ef051")
		self.message.place(x=5,y=40)

		#Do More Research on python RadioButtons
		self.gcc_phat=tk.Radiobutton(self.placeHolder,text="GCC-PHAT",bg="white",fg="red", bd=5,activeforeground="blue",variable=self.mainContainer.variable.gccAlgo, value="gcc-phat")	
		self.gcc_phat.place(x=0,y=70)

		self.gcc_scot=tk.Radiobutton(self.placeHolder, text="GCC-SCOT",bg="white", bd=5,variable=self.mainContainer.variable.gccAlgo,activeforeground="blue", value="gcc-scot")
		self.gcc_scot.place(x=100,y=70)
		tk.Frame(self,height=37,bg="#9ef051").pack(side=tk.BOTTOM)
		self.gcc_ml=tk.Radiobutton(self.placeHolder, text="GCC-ML", bg="white",bd=5,variable=self.mainContainer.variable.gccAlgo,activeforeground="blue", value="gcc-ml")
		self.gcc_ml.place(x=200,y=70)
		self.placeHolder.pack(anchor=tk.CENTER)

class SensorDataPanel(tk.Frame):
	
	def __init__(self,mainContainer,container,width="500", height="100"):
		super().__init__(container,width=width,height=height,bd=20,bg="#9ef051")
		self.mainContainer=mainContainer
		self.place(x=0,y=0)
		self.__add_widgets()
		
	def __add_widgets(self):
		tk.Label(self,text="__________________Sensor Data__________________",font=("Arial", 12),bg="#9ef051").pack()
		self.placeHolder1=tk.Frame(self,width=300,height=100,bd=6,bg="black")
		#Target information
		self.actualLab=tk.Label(self.placeHolder1,text="Target Coords:",bg="#9ef051")

		self.actualXL=tk.Label(self.placeHolder1,text="x-coord: ",bg="#9ef051")
		self.actualXVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.actualX)

		self.actualYL=tk.Label(self.placeHolder1,text="y-coord: ",bg="#9ef051")
		self.actuaYVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.actualY)

		#Initial Target Estimate Information
		self.initialLab=tk.Label(self.placeHolder1,text="Initial Estimate:",bg="#9ef051")
		self.initialXL=tk.Label(self.placeHolder1,text="x-coord: ",bg="#9ef051")
		self.initialXVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.initialX)

		self.initialYL=tk.Label(self.placeHolder1,text="y-coord: ",bg="#9ef051")
		self.initialYVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.initialY)



 		#sensor 1 Configuration
		self.sensor1L=tk.Label(self.placeHolder1,text=" Sensor 1:",bg="#9ef051")
		self.sensor1XcoordL=tk.Label(self.placeHolder1,text="x-coord:",bg="#9ef051")
		self.sensor1xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor1X)
		self.sensor1YCoordL=tk.Label(self.placeHolder1,text="y-coord:",bg="#9ef051")
		self.sensor1yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor1Y) #textfield for y-coord Input

		self.sensor1L.grid(row=0,column=0)
		self.sensor1XcoordL.grid(row=1,column=1)
		self.sensor1xVal.grid(row=1,column=2)
		self.sensor1YCoordL.grid(row=1,column=3)
		self.sensor1yVal.grid(row=1,column=4)

		#Sensor 2 Configuration
		self.sensor2L=tk.Label(self.placeHolder1,text=" Sensor 2:",bg="#9ef051")
		self.sensor2XcoordL=tk.Label(self.placeHolder1,text="x-coord:",bg="#9ef051")
		self.sensor2xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor2X)
		self.sensor2YCoordL=tk.Label(self.placeHolder1,text="y-coord:",bg="#9ef051")
		self.sensor2yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor2Y) #textfield for y-coord Input

		self.sensor2L.grid(row=2,column=0)
		self.sensor2XcoordL.grid(row=3,column=1)
		self.sensor2xVal.grid(row=3,column=2)
		self.sensor2YCoordL.grid(row=3,column=3)
		self.sensor2yVal.grid(row=3,column=4)

		#Sensor 3 Configuration

		self.sensor3L=tk.Label(self.placeHolder1,text=" Sensor 3:",bg="#9ef051")
		self.sensor3XcoordL=tk.Label(self.placeHolder1,text="x-coord:",bg="#9ef051")
		self.sensor3xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor3X)
		self.sensor3YCoordL=tk.Label(self.placeHolder1,text="y-coord:",bg="#9ef051")
		self.sensor3yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor3Y) #textfield for y-coord Input

		self.sensor3L.grid(row=4,column=0)
		self.sensor3XcoordL.grid(row=5,column=1)
		self.sensor3xVal.grid(row=5,column=2)
		self.sensor3YCoordL.grid(row=5,column=3)
		self.sensor3yVal.grid(row=5,column=4)

		#Sensor 4 Configuration
		self.sensor4L=tk.Label(self.placeHolder1,text=" Sensor 4:",bg="#9ef051")
		self.sensor4XcoordL=tk.Label(self.placeHolder1,text="x-coord:",bg="#9ef051")
		self.sensor4xVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor4X)
		self.sensor4YCoordL=tk.Label(self.placeHolder1,text="y-coord:",bg="#9ef051")
		self.sensor4yVal=tk.Entry(self.placeHolder1,width=10,textvariable=self.mainContainer.variable.sensor4Y) #textfield for y-coord Input

		self.sensor4L.grid(row=6,column=0)
		self.sensor4XcoordL.grid(row=7,column=1)
		self.sensor4xVal.grid(row=7,column=2)
		self.sensor4YCoordL.grid(row=7,column=3)
		self.sensor4yVal.grid(row=7,column=4)

		#message to promt the user to select sensor being considered as reference

		self.bot=tk.Frame(self,height=60,bg="#9ef051").pack(side=tk.BOTTOM)	
		tk.Label(self.placeHolder1,text="Select reference:",bg="#9ef051").grid(row=12,column=0)
		tk.Label(self.bot,text="Please Enter Sensor Coord is Centimeters").pack()

		self.actualLab.grid(row=8,column=0)
		self.actualXL.grid(row=9,column=1)
		self.actualXVal.grid(row=9,column=2)
		self.actualYL.grid(row=9,column=3)
		self.actuaYVal.grid(row=9,column=4)

		self.initialLab.grid(row=10,column=0)
		self.initialXL.grid(row=11,column=1)
		self.initialXVal.grid(row=11,column=2)
		self.initialYL.grid(row=11,column=3)
		self.initialYVal.grid(row=11,column=4)




		#Reference Sensor Radio Buttons

		self.sensor1=tk.Radiobutton(self.placeHolder1,text="Sensor 1",
			variable=self.mainContainer.variable.sensorSel, 
			value="sensor1",fg="red",
			activeforeground="blue"
			,bg="white")
		self.sensor2=tk.Radiobutton(self.placeHolder1,
			text="Sensor 2",variable=self.mainContainer.variable.sensorSel,
			value="sensor2",activeforeground="blue",
			bg="white")
		self.sensor3=tk.Radiobutton(self.placeHolder1,text="Sensor 3",
			variable=self.mainContainer.variable.sensorSel,
			value="sensor3",activeforeground="blue",bg="white")
		self.sensor4=tk.Radiobutton(self.placeHolder1,text="Sensor 4",
			variable=self.mainContainer.variable.sensorSel,value="sensor4",activeforeground="blue",bg="white")

		self.sensor1.grid(row=13,column=1)	
		self.sensor2.grid(row=13,column=2)
		self.sensor3.grid(row=13,column=3)
		self.sensor4.grid(row=13,column=4)

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
		"""Terms the program when invoked"""
		cls.container.destroy()
	@classmethod			
	def setContainer(cls,container):		
		"""Sets the value of the container to the one passed in the argument returns true if the  container was set to"""
		cls.container=container


	@classmethod
	def startButton(cls):

		if cls.startPressed:
			#Copy Files from the remote Server
			sa.transfer_file(cls.container.console,"10.42.0.179","eee3097s","!@#$%^&*()1234567890","/home/eee3097s/Documents/text.txt",'/home/chabeli/Documents/Acoustic-Localization-using-TDoA/Data/file.txt')
			cls.startPressed=False
			cls.container.variable.startButton.set("Start Acquisition")

		else:
			
			if not cls.container.writer.inputValidate():
				return None
			sa.acquire(cls.container.console,"10.42.0.179","eee3097s","!@#$%^&*()1234567890","python3 /home/eee3097s/Documents/signalAcquisition.py")
			cls.container.variable.startButton.set("Stop Acquisition")
			cls.startPressed=True
			

	@classmethod
	def plotButtonAction(cls):
		VALIDATION=cls.container.writer.inputValidate()
		if VALIDATION:
			cls.container.coordSystem.plot()#Plot Sensors
			tr.executer(cls.container.variable,cls.container.console,cls.container.coordSystem)#Plot target
		return None #Else return from the plot
	@classmethod
	def clearButtonAction(cls):
		cls.container.console.reset()
	@classmethod
	def resetButtonAction(cls):
		cls.startPressed=False 
		cls.container.variable.reset()
		cls.container.console.reset()
		cls.container.coordSystem.clear()
		#invoke function that clears the target plot
	@classmethod
	def playButtonAction(cls):
		cls.directory = '/home/chabeli/Documents/Acoustic-Localization-using-TDoA/Data/'
		for filename in os.listdir(cls.directory):
			f=os.path.join(cls.directory,filename)
			cls.container.console.text.insert(tk.END,f"Playing audio {filename}...\n")
			cls.container.audioReader.read_wav(f,True)
class CoordSystem(tk.Frame):
	"""
		Class that represents the c
	"""
	def __init__(self,mainContainer,container,width="400",height="400",x_position=843,y_position=0):
		super().__init__(container,width=width,height=height,bg="white")
		self.mainContainer=mainContainer
		self.place(x=x_position,y=y_position)
		self.fig,self.ax=plt.subplots(figsize=(5,5))
		self.plotConfig()
	def plotConfig(self):
		tk.Label(self,text="______________________Rectangular Grid____________________",bg="white",font=("Arial",12)).pack(side=tk.TOP)
		self.fig.patch.set_facecolor('#ffffff')
		self.ax.set(xlim=(self.mainContainer.variable.xMin.get()-1,self.mainContainer.variable.xMax.get()+1),ylim=(self.mainContainer.variable.yMin.get()-1,self.mainContainer.variable.yMax.get()+1))
		self.resetPlot()
		self.canvas=FigureCanvasTkAgg(self.fig,self)
		self.canvas.get_tk_widget().pack(anchor=tk.CENTER)

		self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
		self.toolbar.update()
		self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
	def resetPlot(self):
		self.ax.set(xlim=(self.mainContainer.variable.xMin.get()-1,self.mainContainer.variable.xMax.get()+1),ylim=(self.mainContainer.variable.yMin.get()-1,self.mainContainer.variable.yMax.get()+1))
		self.ax.set_aspect("equal")
		self.ax.spines['bottom'].set_position('zero')
		self.ax.spines['left'].set_position('zero')
		self.ax.spines['top'].set_visible(False)
		self.ax.spines['right'].set_visible(False)
		self.ax.set_ylabel('$y(cm)$',size=7,labelpad=-24,loc="top")
		self.ax.set_xlabel('$x(cm)$',size=7,labelpad=-21, loc="right",rotation=0)
		plt.text(0,0,r"$o$",ha='right',va='top',transform=self.ax.transAxes, horizontalalignment='center',fontsize=7)
		self.x_ticks=np.arange(self.mainContainer.variable.xMin.get(),self.mainContainer.variable.xMax.get()+1,10)
		self.y_ticks=np.arange(self.mainContainer.variable.yMin.get(),self.mainContainer.variable.yMax.get()+1,10)
		self.ax.set_xticks(self.x_ticks[self.x_ticks !=0])
		self.ax.set_yticks(self.y_ticks[self.y_ticks !=0])
		self.ax.set_xticks(np.arange(self.mainContainer.variable.xMin.get(),self.mainContainer.variable.xMax.get()+1),minor=True)
		self.ax.set_yticks(np.arange(self.mainContainer.variable.yMin.get(),self.mainContainer.variable.yMax.get()+1),minor=True)
		self.ax.grid(which='both',color='gray',linewidth=1,linestyle='-',alpha=0.2)


	def plot(self):
		self.ax.cla()
		x1=self.mainContainer.variable.sensor1X.get() #x-coord of sensor 1
		y1=self.mainContainer.variable.sensor1Y.get() #y-coordintae of sensor 2
		x2=self.mainContainer.variable.sensor2X.get()
		y2=self.mainContainer.variable.sensor2Y.get()

		x3=self.mainContainer.variable.sensor3X.get()
		y3=self.mainContainer.variable.sensor3Y.get()

		x4=self.mainContainer.variable.sensor4X.get()
		y4=self.mainContainer.variable.sensor4Y.get()

		xv=[x1,x2,x3,x4]
		yv=[y1,y2,y3,y4]
		self.resetPlot()
		self.ax.plot(xv,yv,'bo',markersize=5)
		self.ax.annotate("sensor1",xy=(x1,y1))
		self.ax.annotate("sensor2",xy=(x2,y2))
		self.ax.annotate("sensor3",xy=(x3,y3))
		self.ax.annotate("sensor4",xy=(x4,y4))
		self.canvas.draw()
	def plot_point(self,x,y,label,color):
		self.ax.plot(x,y,color,markersize=5)
		self.ax.annotate(label,xy=(x,y))
		self.canvas.draw()


	def clear(self):
		self.ax.cla() #clear the plot
		self.resetPlot() #reset the plot to it default value



class Console(tk.Frame):
	"""
	A class that resents the console where errors are printed.
	"""
	def __init__(self,mainContainer,container):
		super().__init__(container,width="300",height="100",bg="white",bd=10)
		self.mainContainer=mainContainer
		self.text=tk.Text(self,width="102",height="40")
		self.__add_widgets()
		self.text.insert(tk.END,"*****************Welcome to Acoustic Traiangulation System***************\n")
		self.text.insert(tk.END,"Please Enter Coordinates in centimeters\n")

		self.place(x=0,y=360)
	def __add_widgets(self):
		tk.Label(self,text="_______________________Console________________________",font=("Arial", 12),bg="white").pack(side=tk.TOP)
		self.text.pack(anchor=tk.CENTER)
	def reset(self):
			self.text.delete("1.0",tk.END)
			self.text.insert(tk.END,"*****************Welcome to Acoustic Traiangulation System****************\n")
			self.text.insert(tk.END,"Please Enter Coordinates in centimeters\n")
class ConsoleWritter:
	"""
		Class that tracks Errors within the program and display them on the console
	"""
	def __init__(self,container,console):
		self.variable=container.variable
		self.console=console  #console where errors are printed
		self.accumulated=""
		self.container=container
	def inputValidate(self):

		if self.variable.sensor1X.get()<0 or self.container.variable.sensor1X.get()>80 or self.container.variable.sensor1Y.get()<0 or self.container.variable.sensor1Y.get()>50:
			self.container.console.text.insert(tk.END,"Error: Sensor 1 is out of bounds!\n")
			return False
		elif self.container.variable.sensor2X.get()<0 or self.container.variable.sensor2X.get()>80 or  self.container.variable.sensor2Y.get()<0 or self.container.variable.sensor2Y.get()>50:
			self.container.console.text.insert(tk.END,"Error: Sensor 2 is out of bounds!\n")
			return False
		elif self.container.variable.sensor3X.get()<0 or self.container.variable.sensor3X.get()>80 or  self.container.variable.sensor3Y.get()<0 or  self.container.variable.sensor3Y.get()>50:
			self.container.console.text.insert(tk.END,"Error: Sensor 3 is out of bounds!\n")
			return False
		elif self.container.variable.sensor4X.get()<0 or self.container.variable.sensor4X.get()>80 or self.container.variable.sensor4Y.get()<0 or self.container.variable.sensor4Y.get()>50:
			self.container.console.text.insert(tk.END,"Error: Sensor 4 is out of bounds!\n")
			return False

		if self.container.variable.sensor1X.get()==self.container.variable.sensor2X.get() and self.container.variable.sensor1Y.get()==self.container.variable.sensor2Y.get():
			self.container.console.text.insert(tk.END,"Error: Sensor 1 and Sensor 2 can not have similar coords!\n")
			return False
		elif self.container.variable.sensor1X.get()==self.container.variable.sensor3X.get() and self.container.variable.sensor1Y.get()==self.container.variable.sensor3Y.get():
			self.container.console.text.insert(tk.END,"Error: Sensor 1 and Sensor 3 can not have similar coords!\n")
			return False
		elif self.container.variable.sensor1X.get()==self.container.variable.sensor4X.get() and self.container.variable.sensor1Y.get()==self.container.variable.sensor4Y.get():
			self.container.console.text.insert(tk.END,"Error: Sensor 1 and Sensor 4 can not have similar coords!\n")
			return False
		elif self.container.variable.sensor3X.get()==self.container.variable.sensor2X.get() and self.container.variable.sensor3Y.get()==self.container.variable.sensor2Y.get():
			self.container.console.text.insert(tk.END,"Error: Sensor 2 and Sensor 3 can not have similar coords!\n")
			return False
		elif self.container.variable.sensor4X.get()==self.container.variable.sensor2X.get() and self.container.variable.sensor4Y.get()==self.container.variable.sensor2Y.get():
			self.container.console.text.insert(tk.END,"Error: Sensor 2 and Sensor 4 can not have similar coords!\n")
			return False
		elif self.container.variable.sensor3X.get()==self.container.variable.sensor4X.get() and self.container.variable.sensor4Y.get()==self.container.variable.sensor3Y.get():
			self.container.console.text.insert(tk.END,"Error: Sensor 3 and Sensor 4 can not have similar coords!\n")
			return False
		elif self.container.variable.frequencyValue.get()<0:
			self.container.console.text.insert(tk.END,"Error: Sampling Frequency can  not be negative!\n")
			return False
		else:
			return True

#************************************Main Application***************************
class Application(tk.Tk):
	"""
		A class	Represents the main Application
	"""

	def __init__(self,width,height,title):
		super().__init__()
		# Create an SSH client instance
		self.geometry(width+"x"+height)
		EventHandler.setContainer(self)
		self.title(title)
		self.variable=Variables(self) #Creat isntance of tk Varaibles
		self.__add_widgets()
		#Object that will read audio data when button pressed
		self.audioReader=sp.AudioReader(self.console)
		#Object that wil be used to calculate TDoA
		self.tdoaEstimator=sp.TDoA_Estimator(self.console)
		#Instantiate the background frame object 
		
	def __add_widgets(self):
		self.background=BackgroundFrame(self)
		self.sensor=SensorDataPanel(self,self.background) #add sensor data frame
		self.control=ControlPanel(self,self.background) #Add control panel frame
		self.console=Console(self,self.background) #add the console frame
		self.signalPropertiesPanel=SignalPropertiesPanel(self,self.background) #add signal properties panel
		self.coordSystem=CoordSystem(self,self.background) #Add coord System Frame
		self.writer=ConsoleWritter(self,self.console)
		self.dis=Display(self)

	def display(self):
		self.mainloop()


class BackgroundFrame(tk.Frame):
	"""
		A Class that presents a frame object where all other frames are enchored.
	"""
	#Will be static Class
	def __init__(self,parent):
		super().__init__(parent,width=1500,height=750,bg="black",bd=10) #Just create a Frame object of the same size and main Window
		self.pack(anchor=tk.CENTER)
class Display(tk.Frame):
	"""A Class that displays information on the screen"""
	def __init__(self,parent):
		super().__init__(parent,width="150",height="1200",bg="white")
		tk.Label(self,text="_____EEE3097S-GROUP 4_____",bg='white',font=("Trattatello,",25)).grid(row=0,column=0)
		tk.Label(self,text="1.Miss   Pius",font=("Trattatello,",15),bg="white").grid(row=1,column=0)
		tk.Label(self,text="2.Mr. Mutetwa",font=("Trattatello,",15),bg="white").grid(row=2,column=0)
		tk.Label(self,text="3.Prof Chabeli",font=("Trattatello,",15),bg="white").grid(row=3,column=0)
		self.place(x=854,y=580)
def main():
	myApp=Application("1500","800","Acoustic Localization")
	myApp.display()
def quit(app):
		app.destroy()
if __name__ == '__main__':
	main()