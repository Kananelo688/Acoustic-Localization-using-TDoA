#Script the start aquisition

import RPi.GPIO as io
import time
import os
import threading



def blink():
	led=4
	io.setmode(io.BCM)
	io.setup(led,io.OUT)
	while True:
		io.output(led,False)
		

blink()