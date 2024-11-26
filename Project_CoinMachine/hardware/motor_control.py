# Controla la rotación de los motores
import time
from machine import Pin, PWM  # Importa los módulos necesarios

class MotorControl:
    def __init__(self, PIN_LEFT, PIN_RIGHT, PIN_VELOCITY):
        #TODO corregir como funciona el motor
        self.motor = PWM(Pin(PIN_LEFT, PIN_RIGHT, PIN_VELOCITY))
        self.current_position = 0
    
    def start_spin(self):
        # Lógica para iniciar la rotación
        self.motor.duty(512)  # Ajusta la velocidad

    def stop_spin(self):
        # Lógica para detener la rotación
        self.motor.duty(0)

    def turn_initial_position(self):
        self.current_position = 0

        self.start_spin()
        #TODO Calcular cuanto tiempo girar para volver a la posición inicial
        time.sleep(2)
        #TODO Calcular cuanto tiempo girar para volver a la posición inicial
        self.stop_spin

    def get_position(self):
        return self.current_position