import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
    while True:
        if GPIO.input(17):
            print("Sonido detectado!")
        else:
            print(" ")
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
