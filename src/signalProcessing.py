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
class Plotter:

	def __init__(self,console=None):
		self.console=console

	def time_axis(Self,samles,step):
		return np.linspace(0,(samples-1)*step,int (samples))
	def freq_axis(self,samples,time_step):
		self.freq_step=1/(samples*time_step)
		if samples % 2 == 0:
			return  np.arange((-samples/2)*self.freq_step,((samples/2))*self.freq_step,self.freq_step)
		return np.arange((-(samples+1)/2)*self.freq_step,((samples-1)/2)*self.freq_step,self.freq_step)
	def time_plot(self,t,xv,title="Time domain graph of the signal",ylab="Magnitude",label="signal1",figure=1):
		if len(t)!=len(xv):
			self.console.text.insert(tk.END,f"Arrays must have same dimensions. Given dimensions {len(t)} and {len(xv)}")
			return
		plt.figure(figure)
		plt.plot(t,xv,label=label)
		plt.ylabel(ylab)
		plt.xlabel("$Time(s)$")
		plt.title(title)
		plt.show()
	def spectral_plot(self,f,xv,time_step,title="Frequency domain plot of the signal",ylab="Amplitude of FT",plot=True):
		if len(f)!=len(xv):
			self.console.text.insert(tk.END,f"Arrays must have same dimensions. Given dimensions {len(f)} and {len(xv)}")
			return
		self.XV=np.fft.fft(xv,n=len(xv))
		self.XV_abs=time_step*np.fft.fftshift(np.abs(self.XV))
		if plot:
			plt.plot(f,self.XV_abs)
			plt.title(title)
			plt.xlabel("Frequency(Hz)")
			plt.ylabel(ylab)
			plt.show()
		return self.XV
	def spectrogral_plot(self,data,rate,title="Spectrogram of the sigal"):
		self.f,self.t,self.Sxx=signal.spectrogram(data,rate)
		plt.pcolormesh(self.t,self.f,self.Sxx)
		plt.title(title)
		plt.ylabel("Frequency(Hz)")
		plt.xlabel("Time(s)")
		plt.colorbar(label="intensity (dB)")
		plt.show()


class AudioReader:

	"""
		This Class represents an object that reads nad play audio file

	"""	
	def __init__(self,console=None):
		self.console=console

	def read_wav(self,filename,play=False):
		self.rate,self.data=io.wavfile.read(filename)
		if play:
			self.console.text.insert(tk.END,f"Playing audio: {filename}\n")
			sd.play(self.data,self.rate)
		return self.data,self.rate
	def record_wav(filename,duration,rate,channels=1):
		self.recording=sd.rec(int(duration*rate),samplerate=rate,channels=channels)
		self.console.text.insert(tk.END,"Recording...\n")
		sd.wait()
		self.console.text.insert(tk.END,"Done.\n")
		io.wavfile.write(filename,rate,recording)
		return self.recording
class TDoA_Estimator:
	
	def __init__(self,console=None):
		self.console=console
	def gcc_phat(self,signal1,signal2,rate=1,plot=False,title="Cross Correleration function between signals",display=False):
		self.N=len(signal1)+len(signal2)
		self.SIGNAL1=np.fft.fft(signal1,n=self.N)
		self.SIGNAL2=np.fft.fft(signal2,n=self.N)
		self.CSD=self.SIGNAL1*np.conj(SIGNAL2)
		self.cc=np.real(np.fft.ifft(self.CSD/np.abs(CSD)))

		self.shift=np.argmax(np.abs(self.cc))-self.N/2

		self.delay=self.shift/rate

		if plot:
			plt.plot(cc)
			plt.title(title)
			plt.xlabel("time lag")
			plt.ylabel("Correltion magnitude")
			plt.show()
		return self.cc, rond(np.abs(self.delay),4)
	

def main():
	print("Hello World")

if __name__ == '__main__':
	main()