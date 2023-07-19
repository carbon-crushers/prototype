import bme280
import smbus2
from time import sleep
import pandas as pd

port = 1
address = 0x77 # Adafruit BME280 address.
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

data_list = []
index_list = []
idx = 0

try:
    while True:
        val = {}
        bme280_data = bme280.sample(bus,address)
        val["humidity"]  = bme280_data.humidity
        val["pressure"]  = bme280_data.pressure
        val["temperature"] = bme280_data.temperature
        print(val["humidity"], val["pressure"], val["temperature"])
        print("Press any key to stop measurements...")
        data_list.append(val)
        index_list.append(idx)
        sleep(1)
        idx += 1
except KeyboardInterrupt:
    pass

readings_data = pd.DataFrame(data_list, 
                             columns=['humidity', 'pressure', 'temperature'], 
                             index=index_list)
readings_data.to_csv('./sensor_data.csv')
