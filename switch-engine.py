#!/usr/bin/python

import sys
import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

relay_channel = 14

GPIO.setup(relay_channel, GPIO.OUT)

# if sys.argv[0] == 0:
#     GPIO.output(relay_channel, GPIO.HIGH) # out
# elif sys.argv[0] == 1:
#     GPIO.output(relay_channel, GPIO.HIGH) # on

print 'switch on'
GPIO.output(relay_channel, GPIO.HIGH) #switch on
time.sleep(5)        # wait 5 seconds

print 'switch off'
GPIO.output(relay_channel, GPIO.LOW) #switch off

GPIO.cleanup()


GPIO.cleanup()