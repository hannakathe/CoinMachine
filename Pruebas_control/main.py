from machine import Pin
import time

# Configuración del módulo L298N
in1 = Pin(18, Pin.OUT)  # Pin IN1 del L298N
enable = Pin(27, Pin.OUT)  # Pin ENA del L298N (habilita el motor)

from machine import Pin
import time

# Configuración del LED 2
led = Pin(2, Pin.OUT)

# Encender y apagar el LED en intervalos
try:
    while True:
        print("Encendiendo LED")
        led.on()  # Encender el LED
        time.sleep(1)  # Esperar 1 segundo
        
        print("Apagando LED")
        led.off()  # Apagar el LED
        time.sleep(1)  # Esperar 1 segundo
except KeyboardInterrupt:
    print("Programa detenido.")
    led.off()  # Asegurarse de apagar el LED al salir


# Función para controlar el motor
def control_motor(state):
    if state == "on":
        enable.on()  # Habilita el motor
        in1.on()     # Activa IN1 para hacer girar el motor
    elif state == "off":
        in1.off()    # Apaga IN1
        enable.off() # Deshabilita el motor

# Prueba del motor
try:
    print("Encendiendo motor...")
    control_motor("on")  # Encender el motor
    time.sleep(2)        # Mantenerlo encendido por 2 segundos

    print("Apagando motor...")
    control_motor("off") # Apagar el motor
    time.sleep(2)        # Esperar 2 segundos

except KeyboardInterrupt:
    control_motor("off") # Asegurarse de apagar el motor si se interrumpe el programa
    print("Motor detenido.")
