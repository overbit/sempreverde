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
channels = [0]*8
channels[0] = AnalogIn(mcp, MCP.P0)
channels[1] = AnalogIn(mcp, MCP.P1)
channels[2] = AnalogIn(mcp, MCP.P2)
channels[3] = AnalogIn(mcp, MCP.P3)
channels[4] = AnalogIn(mcp, MCP.P4)
channels[5] = AnalogIn(mcp, MCP.P5)
channels[6] = AnalogIn(mcp, MCP.P6)
channels[7] = AnalogIn(mcp, MCP.P7)

# print('| Raw ADC Value  | ADC Voltage ')
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))

import time
while True:
    print('| {0.value:>4} | {1.value:>4} | {2.value:>4} | {3.value:>4} | {4.value:>4} | {5.value:>4} | {6.value:>4} | {7.value:>4} ||| {3.voltage:>4}'.format(*channels))

    time.sleep(1)