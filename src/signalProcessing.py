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




def read_wav(filename,play=False):
	rate,data=io.wavfile.read(filename)
	if play:
		sd.play(data,rate)
	return data,rate
def record_wav(filename,duration,sampling_rate,channels=1):
	recording=sd.rec(int(duration*sampling_rate),samplerate=sampling_rate,channels=channels)
	sd.wait()
	io.wavfile.write(filename,sampling_rate,recording)

def audio_delay(data,rate,delay,filename,write=False):
	sample_delay=int(delay*rate)
	ret=np.concatenate((np.zeros(sample_delay)),data)
	if write:
		io.wavfile.write(filename,rate,ret.astype(np.int16))
	return ret
def gcc_phat(ref_signal,signal,rate,interp=16):
	N=signal.shape[0]+ref_signal.shape[0]

	SIGNAL=np.fft.fft(signal,n=N)
	REF_SIGNAL=np.fft.fft(ref_signal,n=N)
	CSD=REF_SIGNAL*np.conj(SIGNAL)
	cross_Corr=np.fft.ifft(CSD/np.abs(CSD),n=(interp*N))
	max_shift=int(interp*N/2)
	cross_Corr=np.concatenate((cross_Corr[-max_shift:],cross_Corr[:max_shift+1]))
	shift=np.argmax(np.abs(cross_Corr))-max_shift
	delay=shift/float(interp*rate)

	return delay,cross_Corr
def main():
	data1,rate=read_wav("ref_signal.wav")
	data2,rate=read_wav("1sec_delayed.wav")
	delay,cc=gcc_phat(data2,data1,rate)
	print(f'Estiated delay is {delay} second')
def getTdoA():
	"""
		This function read the wave files, and computes the time delays with mic choosen as reference

	"""

if __name__ == '__main__':
	main()
