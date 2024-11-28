from machine import Pin
from time import sleep

# Configuración de pines
led = Pin(2, Pin.OUT)  # Pin donde está conectado el LED
led.value(1)
led.value(0)

