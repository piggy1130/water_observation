from wlm import *
from wavemeter_class import *
from sliceQTC_class import *
from DOCUMENT_class import *
from OSCILLOSCOPE import *
import time

import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())

wavemeter = WAVEMETER()
slice = SLICE_QTC()
document = DOCUMENT()
osc_scope = OSCILLOSCOPE()

# the file you want to save your data
filename = "data_tempchange.txt"

fileobject = open(filename, "a")
fileobject.write("temp")
fileobject.write('\t')
fileobject.write("wavelength")
fileobject.write('\t')
fileobject.write("voltage")
fileobject.write('\n')

for i in range (1):
    # start & end temperature
    start = 15.415
    stop = 17.7
    step = 2.283
    need_temp = start
    while need_temp < stop:
        # set temperature
        slice.set_temp(need_temp)
        print("Current Temperature: ", need_temp)
        fileobject.write(str(need_temp))
        fileobject.write('\t')
        time.sleep(4)

        # get wavelength & write to file
        wavelength_value = wavemeter.Read_Wavemeter()
        fileobject.write(str(wavelength_value))
        time.sleep(1)
        fileobject.write('\t')

        # get voltage & write to file
        voltage = osc_scope.get_voltage()
        print("voltage: ", voltage)
        fileobject.write(str(voltage))
        time.sleep(1)
        fileobject.write('\n')

        # update the temp
        need_temp = need_temp + step



