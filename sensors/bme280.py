import time
import smbus2
import bme280
from abstract import AbstractSensor


class BME280Sensor(AbstractSensor):
    def __init__(self, name: str, address: int = 0x76):
        self.name = name
        self.address = address
        self.bus = smbus2.SMBus(1)
        self.calibration_params = bme280.load_calibration_params(
            self.bus, self.address)

    def read(self):
        while True:
            try:
                data = bme280.sample(self.bus, self.address,
                                     self.calibration_params)

                temperature_celsius = data.temperature
                pressure = data.pressure
                humidity = data.humidity

                print(" ")
                print("Temperature: {:.2f} °C ".format(
                    temperature_celsius))
                print("Pressure: {:.2f} hPa".format(pressure))
                print("Humidity: {:.2f} %".format(humidity))

                # Tiempo de espera entre lecturas
                time.sleep(2)

            except KeyboardInterrupt:
                print('Program stopped')
                break
            except Exception as e:
                print('An unexpected error occurred:', str(e))
                break
