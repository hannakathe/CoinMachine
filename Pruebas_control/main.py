# main.py -- put your code here!
from machine import Pin, PWM
import time

class ServoMotor:
    def __init__(self, pin, min_angle=0, max_angle=180, freq=50):
        self.pin = Pin(pin, Pin.OUT)  # Pin de salida para el servo
        self.pwm = PWM(self.pin, freq=freq)  # Genera señal PWM en el pin
        self.min_angle = min_angle  # Ángulo mínimo del servomotor
        self.max_angle = max_angle  # Ángulo máximo del servomotor
        self.min_duty = 40  # Valor de "duty cycle" para el ángulo mínimo (puede variar según el servo)
        self.max_duty = 115  # Valor de "duty cycle" para el ángulo máximo (puede variar según el servo)

    def angle_to_duty(self, angle):
        """
        Convierte un ángulo a un valor de 'duty cycle' para el servo.
        El valor de duty cycle está entre 0 y 1023.
        """
        if angle < self.min_angle:
            angle = self.min_angle
        elif angle > self.max_angle:
            angle = self.max_angle
        # Mapea el ángulo a un rango de duty cycle
        return int(self.min_duty + (angle - self.min_angle) * (self.max_duty - self.min_duty) / (self.max_angle - self.min_angle))

    def set_angle(self, angle):
        """
        Establece el ángulo del servo.
        """
        duty = self.angle_to_duty(angle)
        self.pwm.duty(duty)  # Establece el valor del duty cycle

# Configuración del servomotor
servo = ServoMotor(pin=23)  # Usa el pin 13 para el control del servomotor

# Mueve el servomotor a varios ángulos
angles = [90, 180]
while True:
    for angle in angles:
        print(f"Moviendo el servo a {angle} grados.")
        servo.set_angle(angle)
        time.sleep(1)  # Espera 1 segundo entre cada movimiento
