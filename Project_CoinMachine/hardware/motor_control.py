# Controla la rotación de los motores
import time
from machine import Pin, PWM  # Importa los módulos necesarios
import random

class MotorControl:
    """
    Clase que controla la rotación de los motores.
    
    Atributos:
    motor : PWM
        Controlador PWM del motor.
    velocity_pin : PWM
        Pin de control de la velocidad.
    current_position : int
        Posición actual del motor.
    MOTOR_SPEED : int
        Velocidad del motor.
    """
    def __init__(self, PIN_MOTOR, PIN_VELOCITY, MOTOR_SPEED=256):
        self.motor = PWM(Pin(PIN_MOTOR))
        self.velocity_pin = PWM(Pin(PIN_VELOCITY))
        self.current_position = 0
        self.MOTOR_SPEED = MOTOR_SPEED

    def start_spin(self):
        """Inicia la rotación del motor."""
        self.velocity_pin.duty(self.MOTOR_SPEED)  # Ajusta la velocidad

    def stop_spin(self):
        """Detiene la rotación del motor y establece una posición aleatoria."""
        self.velocity_pin.duty(0)
        self.current_position = random.randint(0, 4)

    def random_spin(self):
        """Hace girar el motor por un tiempo aleatorio entre 3 y 5 segundos."""
        random_time = random.uniform(3, 5)
        self.start_spin()
        time.sleep(random_time)
        self.stop_spin()

    def turn_initial_position(self):
        """Devuelve el motor a la posición inicial."""
        self.current_position = 0
        self.start_spin()
        time.sleep(2)  # TODO: Calcular tiempo real para volver a posición inicial
        self.stop_spin()

    def get_position(self):
        """Retorna la posición actual del motor."""
        return self.current_position
