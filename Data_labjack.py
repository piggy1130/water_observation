from wlm import *
from wavemeter_class import *
from sliceQTC_class import *
from DOCUMENT_class import *
from ADC_class import *
import time

wavemeter = WAVEMETER()
slice = SLICE_QTC()
document = DOCUMENT()
adc = ADC()

# the file you want to save your data
filename = "test_JL.txt"

fileobject = open(filename, "a")
fileobject.write("temp")
fileobject.write('\t')
fileobject.write("wavelength")
fileobject.write('\t')
fileobject.write("voltage")
fileobject.write('\n')


for i in range (1):
    # start & end temperature
    start = 15.400
    stop = 15.800
    step = .02
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
        voltage = adc.get_voltage()
        print("voltage: ", voltage)
        fileobject.write(str(voltage))
        time.sleep(1)
        fileobject.write('\n')

        # update the temp
        need_temp = need_temp + step

