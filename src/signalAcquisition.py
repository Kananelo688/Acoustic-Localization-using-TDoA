import RPi.GPIO as GPIO
from time as sleep



pinLED=4


GPIO.setMode(GPIO.BCM)
GPIO.setwarning(False)
GPIO.setup(pinLED,GPIO.OUT)

while True:
	GPIO.output(piLED,GPIO.HIGH)
	sleep(1)
	GPIO.output(pinLED,GPIO.LOW)
	sleep(1)
	