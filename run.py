import bme280
import smbus2
from time import sleep
import pandas as pd

port = 1
address = 0x77 # Adafruit BME280 address.
bus = smbus2.SMBus(port)

readings_data = pd.DataFrame(columns=['humidity', 'pressure', 'temperature'])

bme280.load_calibration_params(bus,address)

try:
    while True:
          bme280_data = bme280.sample(bus,address)
          humidity  = bme280_data.humidity
          pressure  = bme280_data.pressure
          temperature = bme280_data.temperature
          print(humidity, pressure, temperature)
          print("Press any key to stop measurements...")
          readings_data.append([humidity, pressure, temperature])
          sleep(1)
except KeyboardInterrupt:
    pass

readings_data.to_csv('./sensor_data.csv')
