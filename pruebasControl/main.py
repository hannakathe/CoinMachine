from machine import Pin, PWM
import time

# Configuración del pin PWM para el servomotor
servo_pin = 27  # Cambia este número si tu servo está en otro pin
servo = PWM(Pin(servo_pin))
servo.freq(50)  # Frecuencia de 50 Hz, estándar para servos

# Función para mover el servomotor a un ángulo específico de forma rápida
def set_servo_angle(angle):
    # Ajuste de duty cycle para los ángulos en tu servomotor
    min_duty = 1800     # Ajusta el valor para 0 grados
    max_duty = 8200     # Ajusta el valor para 180 grados
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty_u16(duty)  # Mueve el servo de manera instantánea

# Posiciones de la palanca
def abrir_palanca():
    set_servo_angle(90)  # Mueve la palanca a 90 grados para abrir


def cerrar_palanca():
    set_servo_angle(180)   # Mueve la palanca a 0 grados para cerrar


# Ejemplo de cómo usar las funciones rápidamente sin demoras
while True:
    cerrar_palanca()
    time.sleep(1)  # Pausa para que el servo alcance la posición
    abrir_palanca()
    time.sleep(1)
  
