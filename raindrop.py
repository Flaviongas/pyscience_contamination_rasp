import RPi.GPIO as GPIO
import time

RAIN_PIN = 27  # Usa el GPIO que conectaste

GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_PIN, GPIO.IN)

try:
    print("⏳ Iniciando sensor de lluvia...")
    while True:
        estado = GPIO.input(RAIN_PIN)

        if estado == 0:
            print("💧 Lluvia detectada!")
        else:
            print(" ")
        
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nPrograma detenido.")
