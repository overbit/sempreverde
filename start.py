from event import *
from data import *
from moisture import *

new_reading_event = Event()

repo = SensorRepository(new_reading_event)
moistureSensor = Sensor(new_reading_event)
moistureSensor.Start(new_reading_event)