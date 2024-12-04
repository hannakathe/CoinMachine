from machine import Pin, PWM
import time

# Configuración de los pines
in1 = Pin(18, Pin.OUT)  # Pin para IN1 del L298N
en = PWM(Pin(27))       # Pin para ENA del L298N (PWM)
en.freq(1000)           # Frecuencia PWM de 1 kHz

# Velocidad media (aproximadamente 50% del rango)
velocidad_media = 256  # PWM en el rango de 0 a 1023

# Función para mover el motor hacia adelante a velocidad media
def mover_motor_adelante():
    in1.value(1)  # Dirección hacia adelante
    en.duty(velocidad_media)  # Ajustar la velocidad del motor

try:
    while True:
        # Mover el motor hacia adelante
        mover_motor_adelante()
        print("Motor moviendo hacia adelante a velocidad media.")
        time.sleep(1)  # Mantener el motor en movimiento durante 1 segundo

except KeyboardInterrupt:
    print("Deteniendo el motor.")
    in1.value(0)
    en.duty(0)  # Detener el motor
