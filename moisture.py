import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import time
from adafruit_mcp3xxx.analog_in import AnalogIn
from data import *

class Reading:
    def __init__(self, value, voltage):
        self.value = value
        self.voltage = voltage
        self.percentage = round(voltage/3.3 * 100, 2)

class Sensor:
    def __init__(self, event):
        self.new_reading_event = event

    def Start(self, event):
        print("Starting sensor...")

        # create the spi bus
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

        # create the cs (chip select)
        cs = digitalio.DigitalInOut(board.D5)

        # create the mcp object
        mcp = MCP.MCP3008(spi, cs)

        # create an analog input channel on pin 0
        channel = AnalogIn(mcp, MCP.P3)

        reading =  Reading(value=channel.value, voltage=channel.voltage)
        self.new_reading_event.notify(reading.value, reading.voltage, reading.percentage)
        # SensorRepository.SaveReading(percentage=reading.percentage, value=reading.value, voltage=reading.voltage)

        while True:
            avg =  [0]*2
            for x in range(50):
                avg[0]= avg[0] + channel.value
                avg[1]= avg[1] + channel.voltage
                time.sleep(0.5)
                # print('{} | {}'.format(x, str(channel.value)))

            avgValue = avg[0] / 50
            avgVoltage = avg[1] / 50

            reading =  Reading(value=avgValue, voltage=avgVoltage)
            self.new_reading_event.notify(reading.value, reading.voltage, reading.percentage)
            # SensorRepository.SaveReading(percentage=reading.percentage, value=reading.value, voltage=reading.voltage)

if __name__ == '__main__':
    Sensor.Start()