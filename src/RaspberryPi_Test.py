#!/usr/bin/python3

#RaspberryPi program that blinks LEDS(Just to test connectivity to Raspberry Pi)

#-------------------------Imports-----------------------------#
import RPi.GPIO as io 										  #
import time													  #
#-------------------------------------------------------------#



#-------------------------Variables---------------------------#
led1=27 			#sets the value 27 to led1 varaible
led2=22 			#set the value 22 to led2 variable

io.setmode(io.BCM)  #Changes GPIO pin's specific mode to Broadcom SOC channel(BCM).
# It specifies that GPIO pin number will be used instead of pin numbers

io.setup(led1,io.OUT)	#configure led1 as output mode
io.setupt(led2,io.OUT) #configure led2 as output

while(True):
	io.output(led1,True)
	io.output(led2,False)
	time.sleep(1)
	io.output(led1,False)
	io.output(led2,True)
	time.sleep(1)