import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time
import notification as Notification
from datetime import datetime

# Define the GPIO pin that we have our digital output from our sensor connected to
PUMP_RELAY_GPIO = 22

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin to an input
GPIO.setup(PUMP_RELAY_GPIO, GPIO.OUT, initial=GPIO.HIGH)
# time.sleep(0.5)
# GPIO.output(PUMP_RELAY_GPIO, GPIO.LOW) # switch off 

def switch_pump(value):
	return
	if value == "ON":
		print ("Switch pump on")
		GPIO.output(PUMP_RELAY_GPIO, GPIO.LOW) 
	elif value == "OFF":
		print ("Switch pump off")
		GPIO.output(PUMP_RELAY_GPIO, GPIO.HIGH) 

# Channel of the relay, time in seconds to keep pump running
def watering(channel: str, wateringtime: int):
	print("Start watering")
	switch_pump("ON")
	time.sleep(wateringtime)
	switch_pump("OFF")
	print("Stop watering")

	now = datetime.now()
	current_time = now.strftime("%D %H:%M:%S")
	Notification.send("Watering plant completed at " + current_time)

watering(PUMP_RELAY_GPIO, 1)
GPIO.cleanup() # cleanup all GPIO 