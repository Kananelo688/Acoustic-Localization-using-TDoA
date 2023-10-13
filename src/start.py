#Script the start aquisition


#Author: Kananelo Chabeli

import RPi.GPIO as io
import time
import os
from gpio import Button



pin4=4			#GPIO4 (interrupt line)
pin22=22		#GPIO22,red  LED(blinked to indicate synchronization)
pin27=27		#GPIO27

io.setmode(io.BCM)
io.setup(led,io.OUT)

button=Button(pin4) #Set pin 4 to listen to button press
def record_command():
	"""
		Functin that is invoked when an interrupt is received to start the recording
	"""
	os.system("arecord -D plughw:0 -c2 -r 48000 -f -d 25 S32_LE -t wav -V stereo -v file_stereo.wav") #Record command

def blink():
	#Function that conyinuesly blink led at pin 22
	while(True):
		time.sleep(1)
		io.output(led22,True)
		time.sleep(1)
		io.output(led22,False)

def main():
	io.output(led27,True) # turn on green LED (to indicate that Pi is ready to start sampling)

	buttn.wait_for_press() #Function that waits until button is pressed

	record_command() 		#Call record command when the button is pressed

	blink()				#Call functin that blinks red LED at the same time