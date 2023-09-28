"""
		The python module provides a complete implementation of signal processing algoritms and time difference of arrival techniques used
		 in this project.


		Author: Kananelo Chabeli

		Date: 06/ 09/2023

"""

#****************Import Modules**********************
import sounddevice as sd
from scipy import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk #For  using tk.inter fucntions

def read_wav(filename,play=False,console=None):
	try:
		rate,data=io.wavfile.read(filename)
		if play:
			sd.play(data,rate)
		return data,rate
	except Exception as e:
		console.text.insert(tk.END,f"An Error Occured: {str(e)}\n")
def record_wav(filename,duration,sampling_rate,channels=1,console=None):

	recording=sd.rec(int(duration*sampling_rate),samplerate=sampling_rate,channels=channels)
	sd.wait()
	io.wavfile.write(filename,sampling_rate,recording)

def audio_delay(data,rate,delay,filename=None,write=False,console=None):
	try:
		sample_delay=int(delay*rate)
		ret=np.concatenate((np.zeros(sample_delay)),data)
		if write:
			io.wavfile.write(filename,rate,ret.astype(np.int16))

		return ret
	except Exception as e:
		console.text.insert(tk.END,f"An Error Occured: {str(e)}\n")
def gcc_phat(ref_signal,signal,rate,interp=16,console=None):
	
	try:
		N=signal.shape[0]+ref_signal.shape[0]
		SIGNAL=np.fft.fft(signal,n=N)
		REF_SIGNAL=np.fft.fft(ref_signal,n=N)
		CSD=REF_SIGNAL*np.conj(SIGNAL)
		cross_Corr=np.fft.ifft(CSD/np.abs(CSD),n=(interp*N))
		max_shift=int(interp*N/2)
		cross_Corr=np.concatenate((cross_Corr[-max_shift:],cross_Corr[:max_shift+1]))
		shift=np.argmax(np.abs(cross_Corr))-max_shift
		delay=shift/float(interp*rate)
	except Exception as e:
		console.text.insert(tk.END,f"An Error Occured: {str(e)}\n")

	return delay,cross_Corr
def main():
	data1,rate=read_wav("ref_signal.wav")
	data2,rate=read_wav("1sec_delayed.wav")
	delay,cc=gcc_phat(data2,data1,rate)
	print(f'Estiated delay is {delay} second')
def getTdoA(ref,console=None):
	"""
		This function read the wave files, and computes the time delays with mic choosen as reference

		Parameters:
			ref(str): 	A string stating which microphone is to be taken as reference.

	"""
	try:
		if ref=='sensor1':
			ref,rate=read_wav("sensor1.wav")#Read the sensor data that's reference
			data1,rate=read_wav("sensor2.wav")
			data2,rate=read_wav("sensor3.wav")
			data3,rate=read_wav("sensor4.wav")
		elif ref=='sensor2':
			ref,rate=read_wav("sensor2.wav")#Read the sensor data that's reference
			data1,rate=read_wav("sensor1.wav")
			data2,rate=read_wav("sensor2.wav")
			data3,rate=read_wav("sensor4.wav")
		elif ref=='sensor3':
			ref,rate=read_wav("sensor3.wav")#Read the sensor data that's reference
			data1,rate=read_wav("sensor1.wav")
			data2,rate=read_wav("sensor2.wav")
			data3,rate=read_wav("sensor4.wav")
		elif ref=='sensor4':
			ref,rate=read_wav("sensor4.wav")#Read the sensor data that's reference
			data1,rate=read_wav("sensor1.wav")
			data2,rate=read_wav("sensor2.wav")
			data3,rate=read_wav("sensor3.wav")
		d0=gcc_phat(ref,data1,rate)[0] #Compute first time tdelay
		d1=gcc_phat(ref,data2,rate)[0] #Compute first time tdelay
		d2=gcc_phat(ref,data3,rate)[0] #Compute first time tdelay
		tdoa=np.array([d0,d1,d2])
		return tdoa

	except Exception as e:
		console.text.insert(f"An Error Occured:{str(e)}\n")


if __name__ == '__main__':
	main()
