import socket
import json
import re
from labjack import ljm

class ADC:
    def __init__(self):
        # Open a connection to the LabJack T7 via USB
        self.handle = ljm.open(ljm.constants.dtT7, ljm.constants.ctUSB, "ANY")
        
    def get_voltage(self, command=":MEASUrement:CH2?"):
        # read voltage
        ain0_voltage = ljm.eReadName(self.handle, "AIN0")
        return ain0_voltage


# Example Usage:
if __name__ == '__main__':
    adc = ADC()

    voltage = adc.get_voltage()
    print("Current Voltage: ", voltage)

    voltage = adc.get_voltage()
    print("Current Voltage: ", voltage)


