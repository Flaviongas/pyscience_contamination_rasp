import RPi.GPIO as GPIO
import time
from abstract import AbstractSensor


class SoundSensor(AbstractSensor):
    def __init__(self, name: str, pin: int):
        super().__init__(name, pin)

    def read(self) -> float:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        try:
            while True:
                if GPIO.input(self.pin):
                    print("Sonido detectado!")
                else:
                    print(" ")
                time.sleep(0.2)
        except KeyboardInterrupt:
            GPIO.cleanup()
