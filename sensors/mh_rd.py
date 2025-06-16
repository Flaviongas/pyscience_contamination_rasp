import RPi.GPIO as GPIO
import time
from abstract import AbstractSensor


class MH_RD_Sensor(AbstractSensor):
    def __init__(self, name: str, pin: int):
        super().__init__(name, pin)
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def read(self) -> float:
        try:
            print("⏳ Iniciando sensor de lluvia...")
            while True:
                estado = GPIO.input(self.pin)

                if estado == 0:
                    print("💧 Lluvia detectada!")
                else:
                    print(" ")

                time.sleep(1)

        except KeyboardInterrupt:
            GPIO.cleanup()
            print("\nPrograma detenido.")
