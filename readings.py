from abstract import AbstractReading
import board
from dht22 import DHT22Sensor
from bme280 import BME280Sensor
from mh_rd import MH_RD_Sensor
from sound import SoundSensor


class Readings(AbstractReading):
    def __init__(self, name: str):
        super().__init__(name)

    def readDHT22(self) -> float:
        dht22_sensor = DHT22Sensor("DHT22", board.D4)
        dht22_sensor.read()

    def readBME280(self) -> float:
        bme280_sensor = BME280Sensor("BME280", address=0x76)
        bme280_sensor.read()

    def readMH_RD(self) -> float:
        rain_sensor = MH_RD_Sensor("MH_RD", 27)
        rain_sensor.read()

    def readSound(self) -> float:
        sound_sensor = SoundSensor("Sound Sensor", 17)
        sound_sensor.read()
