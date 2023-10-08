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



description='-----------------Time Delay Estimations---------------\n\tWith no filter:\t\t with bandpass filter:\n'

def read_wav(filename,play=False,console=None):
	try:
		rate,data=io.wavfile.read(filename)
		if play:
			sd.play(data,rate)
		return data,rate
	except Exception as e:
		console.text.insert(tk.END,f"Error Occured: {str(e)}\n")
def play(filename,console):
	"""
		Function that play an audio, given a fie name
	"""
	try:
		rate,data=io.wavfile.read(filename)
		sd.play(data,rate)
		sd.wait() #Wait for it to finish playing audio
	except Exception  as e:
		console.text.insert(tk.END,f"Error: {str(e)}.\n")
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
		console.text.insert(tk.END,f"Error Occured: {str(e)}\n")
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
		console.text.insert(tk.END,f"Error Occured: {str(e)}\n")

	return np.abs(delay)
def filter(taps,cut_off,rate,plot=False,pass_zero=True):
    """
        Function that computes the impulse response of the filter
    
    """
    h = signal.firwin(taps, cut_off,pass_zero=pass_zero,width=10, fs=rate)
    if plot:
        plt.plot(h,'.-')
        plt.title('Impulse respose of the low pass FIR digital filter')
        plt.show()
    return h

def getTdoA(console=None,verbose=False,filt=True):
	"""
		This function read the wave files, and computes the time delays with mic choosen as reference
	"""
	#try:
	#	if verbose and console is not None:
	#		console.text.insert(tk.END,"Processing signals....\n")
	pi1_data,rate2=read_wav("/home/chabeli/pi1.wav")
	pi2_data,rate1=read_wav("/home/chabeli/pi2.wav")
	pi1_channel1,pi1_channel2=pi1_data[:,0],pi1_data[:,1]
	pi2_channel1,pi2_channel2=pi2_data[:,0],pi2_data[:,1]

		#--------------------------------------------------#
		#Calclulating Time difference of Arrivals 		   #
		#--------------------------------------------------#
	tdoa0=gcc_phat(pi1_channel1,pi1_channel2,rate1)
	tdoa1=gcc_phat(pi1_channel1,pi2_channel1,rate1)
	tdoa2=gcc_phat(pi1_channel1,pi2_channel2,rate1)
		#Computer time delay extimations with filtered signals

	if filt:
		h=filter(len(pi1_channel1),[100,15000],rate1,pass_zero='bandpass')
		pi1_channel1=signal.convolve(h,pi1_channel1)
		pi2_channel2=signal.convolve(h,pi2_channel2)

		pi1_channel2=signal.convolve(h,pi1_channel2)

		pi2_channel1=signal.convolve(h,pi2_channel1)

			#Find time delays
		tdoa0_1=gcc_phat(pi1_channel1,pi1_channel2,rate1)
		tdoa1_1=gcc_phat(pi1_channel1,pi2_channel1,rate1)	
		tdoa2_1=gcc_phat(pi1_channel1,pi2_channel2,rate1)

		delay0=f"Delay0(sec) \t{tdoa0}\t\t {tdoa0_1}\n"
		delay1=f"Delay0(sec) \t{tdoa1}\t\t {tdoa1_1}\n"
		delay2=f"Delay0(sec) \t{tdoa2}\t\t {tdoa2_1}\n"
		description+=description+delay0+delay1+delay2
		return np.array([[tdoa0,tdoa1,tdoa2],[tdoa0_1,tdoa1_1,tdoa2_1]])

		#if verbose:
		#	console.text.insert(tk.END,"Time delay Estimation Done.\n")

	return np.array([tdoa0,tdoa1,tdoa2])

		
	#except Exception as e:
	#	console.text.insert(tk.END,f"Error Occured:{str(e)}\n")


def main():
	print('Calculating time delay estimations.....')
	tdoas=getTdoA()
	print(description)
if __name__ == '__main__':
	main()
