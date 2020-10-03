import RPi.GPIO as GPIO # This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time

# Define the GPIO pin that we have our digital output from our sensor connected to
MOISTURE_SENSOR_GPIO = 17
PUMP_RELAY_GPIO = 22

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin to an input
GPIO.setup(MOISTURE_SENSOR_GPIO, GPIO.IN)
GPIO.setup(PUMP_RELAY_GPIO, GPIO.OUT, initial=GPIO.HIGH)
# time.sleep(0.5)
# GPIO.output(PUMP_RELAY_GPIO, GPIO.LOW) # switch off 

def switch_pump(value):
	if value == "ON":
		print ("Switch pump on")
		GPIO.output(PUMP_RELAY_GPIO, GPIO.LOW) 
	elif value == "OFF":
		print ("Switch pump off")
		GPIO.output(PUMP_RELAY_GPIO, GPIO.HIGH) 

def moisture_callback(channel): 
	if GPIO.input(channel):
		print ("LED off")
		switch_pump("ON")
	else:
		print ("LED on")
		switch_pump("OFF")

moisture_callback(MOISTURE_SENSOR_GPIO)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(MOISTURE_SENSOR_GPIO, GPIO.BOTH, bouncetime=100)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(MOISTURE_SENSOR_GPIO, moisture_callback)

try:
	# This is an infinte loop to keep our script running
	while True:
		# This line simply tells our script to wait 0.1 of a second, this is so the script does not hog all of the CPU
		time.sleep(1)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	print("Keyboard interrupt")
	GPIO.cleanup() # cleanup all GPIO 

finally:
	print("clean up") 
