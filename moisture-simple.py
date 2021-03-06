#!/usr/bin/python

# Start by importing the libraries we want to use

import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time
# This is our callback function, this function will be called every time there is a change on the specified GPIO channel, in this example we are using 17

def callback_action(channel):  
	if GPIO.input(channel):
		print "LED off"
		# sendEmail(message_dead)
	else:
		print "LED on"
		# sendEmail(message_alive)

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
sensor_channel = 17
# Set the GPIO pin to an input
GPIO.setup(sensor_channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(sensor_channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(sensor_channel, callback_action)

# This is an infinte loop to keep our script running
while True:
	# This line simply tells our script to wait 0.1 of a second, this is so the script does not hog all of the CPU
	time.sleep(0.5)


GPIO.cleanup()