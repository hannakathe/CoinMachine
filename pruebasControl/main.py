# main.py -- put your code here!

from machine import Pin
import time

# Configura el pin 2 como salida
led = Pin(2, Pin.OUT)

# Enciende el LED
led.value(1)  # 1 para encender, 0 para apagar

# Mantiene el LED encendido por 5 segundos
time.sleep(5)

# Apaga el LED
led.value(0)
