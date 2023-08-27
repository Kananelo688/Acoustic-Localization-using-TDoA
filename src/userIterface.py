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
	A class that defines all  tkinter variables which are intended t tbe used by the main Application. 

	The class implements methods that set and set thier Values. All variables are set to thier default values 
	 
	 Attributes:
	 -----------
	 containter: Tk
	 	A Tk object which represents the main window
	 <Many other variables>


	"""

	def __init__(self,container):

		"""
			Creates a new instance of the class with containter attributes initialized.
		"""
		self.container=container

		self.gccAlgo=tk.StringVar(container,value="gcc-phat")

		#Variable that will be used to get sampling frequency fromt he user.
		self.frequencyValue=tk.IntVar(container, value=1000) 

		#Control variable for radio buttons that select the preffered reference sensor. Sensor 1
		#sensor 1 will be used checked by default
		self.sensorSel=tk.StringVar(container, value="sensor1") 


#Variables to get sensor data from the user

		#Sensor 1 coordinates

		self.sensor1X=tk.DoubleVar(container, value=0.0) #Must be set, not default values will be used
		self.sensor1Y=tk.DoubleVar(container, value=0.0)

		#Sensor 2 coordinates

		self.sensor2X=tk.DoubleVar(container, value=0.0) #Must be set, not default values will be used
		self.sensor2Y=tk.DoubleVar(container, value=0.0)

		#Sensor 3 Coordinates

		self.sensor3X=tk.DoubleVar(container, value=0.0) #Must be set, not default values will be used
		self.sensor3Y=tk.DoubleVar(container, value=0.0)

		#Sensor 4 Coordinates

		self.sensor4X=tk.DoubleVar(container, value=0.0) #Must be set, not default values will be used
		self.sensor4Y=tk.DoubleVar(container, value=0.0)
		#Variable for Start Button

		self.startButton=tk.StringVar(container, value="Start Acquisition")

		#Variables to get data about dimension of the Grid

		self.xMin=tk.IntVar(container, value=-5)
		self.xMax=tk.IntVar(container, value=5)

		self.yMin=tk.IntVar(mainWindow, value=-5)
		self.yMax=tk.IntVar(mainWindow, value=5)

		#Define Variable that Display Results of the Experiment

		self.snr=tk.StringVar(container,value="Signal-to-Noise Ration:<Some Value>")
		self.location=tk.StringVar(container,value="Estimaned Location:(x,y)")
		self.time=tk.StringVar(container,value="Computational Time:<time> seconds")

#/***************Define a class that handles all Control button Widgets on the main window

class ControlPanel(ttk.Frame):
	"""
	A class that represents a Control Panel on the main Application window.
	A control panel holds button that control behavoir of the application.


	Attributes:
	-----------
	containter: Frame
		An object of the ttk.Frame class that holds all other user defines widgets
	x_positon: int
		An integer that represents the x position of this ControlPanel on the container.
	y_position: int
		An integer that represent the y-positon of this Frame relative to the container


	"""
	
	startButton=None #Button that starts/stops signal Acquisition
	quitButton=None #Button that exit the main program
	resetButton=None#Button that resets the propeties of the window to thier defaults
	plotButton=None #Button that plots the target location on the grid
	clearButton=None#Object that clear the plotting of the target on the grid

	#Costructor
	def __init__(self, container, x_positon,y_position,width,height):
		"""
			Creates new instance of the Frame within given container at given x and y positions
			
			Attributes:
			-----------
			Containter: Frame
				An object of the ttk.Frame class that holds all other user defines widgets
			x_positon: int
				integer that represents the x position of this ControlPanel on the container.
			y_position: int
				An integer that represent the y-positon of this Frame relative to the container
			width: int
				An integer defining the width of this frame
			height: int
				An integer representing the height of this  frame	
		"""

		super().__init__(container,width=width,height=height)
		self.place(x_positon,y_position) #Place the window are required position


	#Method that adds widgets / buttons to this frame
	def __add_widgets(self):
		pass # TO DO


class SignalPropertiesPanel(ttk.Frame):
	pass #TO DO
class SensorDataPanel(ttk.Frame):
	pass #TO DO

class ResultsPanel(ttk.Frame):
	pass #TO DO
class MainControl(ttk.Frame):
	pass #TO DO
class CoordinateSystem(ttk.Frame):
	pass #TO DO
class GridDimensions(ttk.Frame):
	pass #TO DO
class Application(tk.Tk):
	pass#

def main():
	print("Hello World\n")


if __name__ == '__main__':
	main()