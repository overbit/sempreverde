import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from db import *

initDb()

if __name__ == '__main__':
    print("Starting sensor...")


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
channel = AnalogIn(mcp, MCP.P3)

print('| Raw ADC Value  | ADC Voltage ')

import time
while True:
    sensorValue = 0 
    for x in range(50):
        sensorValue = sensorValue + channel.value; 
        time.sleep(0.5)
        print('{} | {}'.format(x, str(channel.value)))
        # print('| {}\t\t | {}V\t\t || {}'.format(str(channel.value), str(round(channel.voltage, 5)), x))


    sensorValue = sensorValue/50.0; 
    print('>>>>>>>>>>>>>> | {}\t\t | <<<<<<<<<<<<<<'.format(str(channel.value)))
    
    reading = SensorReading(sensorName='moisture', value=channel.value, voltage=channel.voltage)
    reading.save()
    # insert_reading("MoistureSensor", channel.value, channel.voltage)
    reading.select()
    time.sleep(5)