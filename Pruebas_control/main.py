# main.py -- put your code here!

from machine import Pin
import time

led = Pin(18, Pin.OUT)  # El pin 2 es común para el LED integrado en las ESP32

led.value(0)
""" while True:
    led.value(1)  # Enciende el LED
    time.sleep(1)  # Espera 1 segundo
    led.value(0)  # Apaga el LED
    time.sleep(1)  # Espera 1 segundo """
