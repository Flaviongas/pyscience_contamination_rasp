from abstract import AbstractSensor
import time
import board
import adafruit_dht


class DHT22Sensor(AbstractSensor):
    def __init__(self, name: str, pin: int):
        super().__init__(name, pin)
        self.dhtDevice = adafruit_dht.DHT22(pin)
        # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio. This may be necessary on a Linux single board computer like the Raspberry Pi, but it will not work in CircuitPython.
        # dhtDevice = adafruit_dht.DHT22(pin, use_pulseio=False)

    def read(self) -> float:
        while True:

            try:

                # Print the values to the serial port

                temperature_c = self.dhtDevice.temperature

                temperature_f = temperature_c * (9 / 5) + 32

                humidity = self.dhtDevice.humidity

                print(f"Temp: {
                      temperature_f:.1f} F / {temperature_c:.1f} C    Humidity: {humidity}% ")

            except RuntimeError as error:

                print(error.args[0])

                time.sleep(2.0)

                continue

            except Exception as error:

                self.dhtDevice.exit()

                raise error

            # Tiempo de espera entre lecturas
            time.sleep(2.0)
