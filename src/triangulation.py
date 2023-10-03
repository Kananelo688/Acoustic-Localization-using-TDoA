"""
	This module contains the functions that implement trialateration algorithm based on the 

	Time Difference of arrival data. The algorithm achieves this by using 
	optimization point of view.



	Author: Kananelo Chabeli
"""


import numpy as np
import scipy.optimize as op
import tkinter as tk
import math as mt
import signalProcessing as sp

SPEED_OF_SOUND=343 #m/s 



def matrices(sensors,tdoa,console=None):
	"""
		This function takes in array of tuples of sensor coordinates, 
		the first array is assumed to be the reference sensor, and array of tdoa data

		The function creates a Matrix M and solution matrix  B such that Mx=B, where x is the solution vector,
		as  specified in Multilaterization algorithm.

		The function assumes that the coordinate system is labeled in meters, and that tdoa data is in milliseconds.  
		-----------
		Parameters:
			sensors: array of tuples of sensor coordinates, first element taken as coordinate of reference sensor
			tdoa: 	array of tdoa data corresponding to each sensor.

		Returns:
			matrix: Matrix M, in the equaion Mx=B
			solution: The solution vector B
	"""
	try:
		if len(sensors)-1 !=len(tdoa) and console is not None:
			console.text.insert(tk.End,"Error Occured: missing Data.\n")
		ref=sensors[0] #Get coordinates of the reference signal
		matrix=np.ones((3,3))		#The expected  Matrix will be  3x3 ndarray object
		solution=np.ones((3,1))	#The solution vector

	#Run nested for loop and hard code these matrices
		for i in range(3):
			for j in range(3):
				if j==0:
					matrix[i][j]=ref[0]-sensors[i+1][0]
				elif j==1:
					matrix[i][j]=ref[1]-sensors[1+i][1]
				else:
					matrix[i][j]=SPEED_OF_SOUND*tdoa[i]

		b0=(mt.pow(ref[0],2)-mt.pow(sensors[1][0],2))+(mt.pow(ref[1],2)-mt.pow(sensors[1][1],2))+(mt.pow(SPEED_OF_SOUND*tdoa[0],2))

		b1=(mt.pow(ref[0],2)-mt.pow(sensors[2][0],2))+(mt.pow(ref[1],2)-mt.pow(sensors[2][1],2))+(mt.pow(SPEED_OF_SOUND*tdoa[1],2))

		b2=(mt.pow(ref[0],2)-mt.pow(sensors[3][0],2))+(mt.pow(ref[1],2)-mt.pow(sensors[3][1],2))+(mt.pow(SPEED_OF_SOUND*tdoa[2],2))
	
		solution=0.5*np.array([b0,b1,b2])
	except Exception as e:
		console.text.insert(tk.END,f"An Error Occured: str(e)\n")	

	#for i in range(3):
	#	entry=(mt.pow(ref[0],2)-mt.pow(sensors[i+1][0],2))+(mt.pow(ref[1],2)-mt.pow(sensors[i+1][1],2))+(mt.pow(SPEED_OF_SOUND*tdoa[i],2))
	#		solution[i][0]=entry
	return matrix,solution

def error(x,mat,sol,ref):
	"""
		This function defines and error vector fucntion is to be minimized by the optimization algorithm.

		---------
		Parameters:
			x: 	3x1 vector of initial estimate. x[0][0]=x-coordinate,x[1][0]=y-coordinate and x[2][0]=dist of ref sensor
			mat: 3x3 Matrix
			sol: 3x1 matrix
		Returns:
			estimate: a float that equal norm of the vector Mx-b

	"""
	dist=distance(x[:2],ref)
	x[2]=dist
	errVec=np.array([(mat[0][0]*x[0])+(mat[0][1]*x[1])+(mat[0][2]*x[2])-sol[0],
		(mat[1][0]*x[0])+(mat[1][1]*x[1])+(mat[1][2]*x[2])-sol[1],
		(mat[2][0]*x[0])+(mat[2][1]*x[1])+(mat[2][2]*x[2])-sol[2]])
	estimate=np.linalg.norm(errVec)
	return estimate

def compute(initial,matrix,solution,ref):
	"""
		This function implements the actual optimization algorithm to estimate the target location
	
	"""
	#bounds to independent variables
	bnds=((0.0,0.8),(0.0,0.5),(0.0,0.943398))
	res=op.minimize(
		error,
		initial,
		args=(matrix,solution,ref),
		method='L-BFGS-B',
		options={'ftol':1e-5},
		)

	return res

def distance(point1,point2):
	"""
		Function that computes distance between points in space(provided for testing purposes)
	"""
	return round(mt.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2),9)
def time(distances):
	"""
		returns array of flight times f
	"""
	x=np.array([round((dist/SPEED_OF_SOUND)*1e3,9) for dist in distances])
	return x #Returns flight times
def calc_tdoa(ftimes):
	"""
		Compute tdoa between signals and time (as magnitude positive values)
		provide for test purposes
	"""
	y=np.array([round((ftimes[0]-ftimes[1+i])*1e-3,9) for i in range(3)])
	return y

def distances(coordiates,target):
	x=[distance(coord,target) for coord in coordiates]
	return np.array(x)
def meansquares(x,mat,sol,ref):


	dist=distance(x,ref)
	x[2]=dist
	errVec=np.array([np.abs((mat[0][0]*x[0])+(mat[0][1]*x[1])+(mat[0][2]*x[2])-sol[0]),
		np.abs((mat[1][0]*x[0])+(mat[1][1]*x[1])+(mat[1][2]*x[2])-sol[1]),
		np.abs((mat[2][0]*x[0])+(mat[2][1]*x[1])+(mat[2][2]*x[2])-sol[2])])

	return np.sum(errVec**2/3)

	
def main():
	sensors=[(0.1,0.2),(.1,0.5),(0.4,0.4),(0.7,0.3)]
	target=(0.6,0.35)
	dist=distances(sensors,target)
	ftimes=time(dist)
	tdoa=calc_tdoa(ftimes)
	mat,sol=matrices(sensors,tdoa)
	err=error([0.6,0.35,0.522015325],mat,sol,sensors[0])
	res=compute([0.1,0.5,0.3],mat,sol,sensors[0])
	#print("****************************Testing Multilaterization Algorithm*****************************\n")
	#print(f"Microphone Coordinates Coordinates:\nMicrophone0:\t {sensors[0]}\nMicrophone1:\t {sensors[1]}\nMicrophone2:\t {sensors[2]}\nMicrophone3:\t {sensors[3]}\n")
	#print(f'Actual Target Location:\t {target}\n')
	#print(f'Distances of Microphone to target:\nMicrophone0:\t{dist[0]}\nMicrophone1:\t{dist[1]}\nMicrophone2:\t{dist[2]}\nMicrophone3:\t{dist[3]}\n')
	#print(f'Flight Times to microphones:\nTime0:\t {ftimes[0]} milliseconds\nTime1:\t {ftimes[1]} milliseconds\nTime2:\t {ftimes[2]} milliseconds\nTime3:\t {ftimes[3]} milliseconds\n')
	#print(f'Time Difference of Arrivals:\nTdoA_01:\t{tdoa[0]}\nTdoA_02:\t{tdoa[1]}\nTdoA_03:\t{tdoa[2]}\n')
	#print(f'Matrices used:\n {mat}\n\n {sol}\n')
	print(f'Solution that gives the approximation: {res.x}')

def executer(variables,console,coordinateSystem,verbose=False,useTestData=True):
	"""
		Function that reads the sensor coordinates, and invokes  function that computes TDoA data

		The fucntion plots the target to the GUI and reuslts summary to the console.

		--------------
		Paramters:
			variables		: an object that has all variables used in this application
			console			: a console object used in this project
			coordinateSystem:a coordinate system where reuslts are plotted	

	"""
	#Get sensor coordinates(convert coordinates to m)
	reference=0
	try:
		if(verbose):
			console.text.insert(tk.END,"Reading microphone coordinates coordiates...\n")
		sensor1X=variables.sensor1X.get()/100 #Must be set, not default values will be used
		sensor1Y=variables.sensor1Y.get()/100 
		sensor2X=variables.sensor2X.get()/100 
		sensor2Y=variables.sensor2Y.get()/100 
		sensor3X=variables.sensor3X.get()/100 
		sensor3Y=variables.sensor3Y.get()/100 
		sensor4X=variables.sensor4X.get()/100 
		sensor4Y=variables.sensor4Y.get()/100
		#Initial estimate(taken from the user)
		initialX=variables.initialX.get()/100
		initialY=variables.initialX.get()/100
		#
		#Actual coordinates of the target (provided for testing, its optional)
		actualX=variables.actualX.get()/100
		actualY=variables.actualY.get()/100
		#crease array of sensors 
		#Check which sensor if marked as reference sensor
		if variables.sensorSel.get()=='sensor1':
			reference=0
			sensors=np.array([(sensor1X,sensor1Y),(sensor2X,sensor2Y),(sensor3X,sensor3Y),(sensor4X,sensor4Y)])
	
		elif variables.sensorSel.get()=='sensor2':
			reference=1
			sensors=np.array([(sensor2X,sensor2Y),(sensor1X,sensor1Y),(sensor3X,sensor3Y),(sensor4X,sensor4Y)])
			initial=np.array([initialX,initialY,distance((initialX,initialY),sensors[0])])
		elif variables.sensorSel.get()=='sensor3':
			reference=2
			sensors=np.array([(sensor3X,sensor3Y),(sensor2X,sensor2Y),(sensor1X,sensor1Y),(sensor4X,sensor4Y)])
		
		else:
			reference=3
			sensors=np.array([(sensor4X,sensor4Y),(sensor2X,sensor2Y),(sensor3X,sensor3Y),(sensor1X,sensor1Y)])
			
		initial=np.array([initialX,initialY,distance((initialX,initialY),sensors[0])])
		target=(actualX,actualY)


		if useTestData:
			if verbose:
				console.text.insert(tk.END,"Multilatering with synthesized data...\n")
			dist=distances(sensors,target)
			flight_times=time(dist)
			tdoa=calc_tdoa(flight_times)
			mat,sol=matrices(sensors,tdoa)#Compute Matrices
			res=compute(initial,mat,sol,sensors[0])
			console.text.insert(tk.END,'\n--------------------------------RESULTS-------------------------------------\n')
			console.text.insert(tk.END,f'Actual Target Location   :\t {target}\n')
			console.text.insert(tk.END,f'Estimated Target Location:\t ({round(res.x[0],4)},{round(res.x[1],4)})\n')
			console.text.insert(tk.END,f"Estimated Error		  :\t {round(res.fun,4)}\n")
			console.text.insert(tk.END,'------------------------------------------------------------------------------\n')
			coordinateSystem.plot_point(actualX*100,actualY*100,label="Actual",color="ro")
			coordinateSystem.plot_point(round(res.x[0],3)*100,round(res.x[1],3)*100,label="Estimated",color="go")
			return 
		#Write Code that uses actual tdoa data from this point
		
		tdoa=sp.getTdoA(console,verbose)
		if verbose:
			console.text.insert(tk.END,"Multilatering using Optimization algorithm....\n")
		mat,sol=matrices(sensors,tdoa)#Compute Matrices
		res=compute(initial,mat,sol,sensors[0])
		console.text.insert(tk.END,'\n------------------------------------RESULTS------------------------------------\n')
		console.text.insert(tk.END,f'Actual Target Location   :\t {target}\n')
		console.text.insert(tk.END,f'Estimated Target Location:\t ({round(res.x[0],4)},{round(res.x[1],4)})\n')
		console.text.insert(tk.END,f"Estimated Error		  :\t {round(res.fun,4)}\n")
		console.text.insert(tk.END,'---------------------------------------------------------------------------------\n')

		coordinateSystem.plot_point(round(res.x[0],3)*100,round(res.x[1],3)*100,label="Estimated",color="go")
		coordinateSystem.plot_point(actualX*100,actualY*100,label="Actual",color="ro")


	except Exception as e:
		console.text.insert(tk.END,F"Error Occured: {str(e)}\n")

	#tdoa=sp.getTDoA(console,reference=1) #This function will be invoked to calculater

def distance_constaint(x,ref_sensor):
	"""
		This fnction is the constriant function that specifies the constraint to the function
	
	"""
	coords=x[0][:2]
	return np.abs(x[0][2]-distance(coords,ref_sensor))

if __name__ == '__main__': 
	main()


