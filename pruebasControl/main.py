# main.py -- put your code here!




from machine import Pin, PWM
import time

# Configuración del pin PWM para el servomotor
servo_pin = 15  # Cambia este número si tu servo está en otro pin
servo = PWM(Pin(servo_pin), freq=50)  # Frecuencia estándar para servos

# Función para mover el servomotor a un ángulo específico
def set_servo_angle(angle):
    # Convertimos el ángulo (0-180) a un valor de duty que el servo pueda usar
    min_duty = 1024     # Valor de duty para 0 grados
    max_duty = 5120     # Valor de duty para 180 grados
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty(duty)

# Posiciones de la palanca
def abrir_palanca():
    set_servo_angle(90)  # Mueve la palanca a 90 grados para abrir

def semi_abrir_palanca():
    set_servo_angle(45)  # Mueve la palanca a 45 grados para semi-abrir

def cerrar_palanca():
    set_servo_angle(0)   # Mueve la palanca a 0 grados para cerrar

def cerrar_completamente():
    set_servo_angle(180) # Mueve la palanca a 180 grados para cerrar completamente

# Ejemplo de cómo usar las funciones
while True:
    cerrar_palanca()
    time.sleep(2)  # Espera de 2 segundos
    semi_abrir_palanca()
    time.sleep(2)
    abrir_palanca()
    time.sleep(2)
    cerrar_completamente()
    time.sleep(2)
