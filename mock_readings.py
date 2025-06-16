from abstract import AbstractReading
import random


class MockReadings(AbstractReading):
    def __init__(self, name: str):
        super().__init__(name)

    def readDHT22(self) -> float:
        while True:
            random_temperature_c = random.uniform(
                15.0, 30.0)  # Simulate temperature in Celsius
            # Simulate humidity in percentage
            random_humidity = random.uniform(30.0, 70.0)
            print(f"Temp:{random_temperature_c:.1f} C    Humidity: {
                  random_humidity:.1f}% ")

    def readBME280(self) -> float:
        while True:
            random_temperature_c = random.uniform(
                15.0, 30.0)
            random_pressure = random.uniform(950.0, 1050.0)
            random_humidity = random.uniform(30.0, 70.0)
            print(f"Temp:{random_temperature_c:.1f} C    Pressure: {
                  random_pressure:.1f} hPa    Humidity: {random_humidity:.1f}% ")

    def readMH_RD(self) -> float:
        while True:
            random_rain = random.randrange(0, 1)
            print(f"Rain Detected: {'Yes' if random_rain else 'No'}")

    def readSound(self) -> float:
        while True:
            random_sound = random.randrange(0, 1)
            print(f"Sound Detected: {'Yes' if random_sound else 'No'}")
