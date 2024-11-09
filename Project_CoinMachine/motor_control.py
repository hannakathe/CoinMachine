# Controla la rotación de los motores


from machine import Pin, PWM  # Importa los módulos necesarios

class MotorControl:
    def __init__(self, motor_pin):
        self.motor = PWM(Pin(motor_pin))
    
    def start_spin(self):
        # Lógica para iniciar la rotación
        self.motor.duty(512)  # Ajusta la velocidad

    def stop_spin(self):
        # Lógica para detener la rotación
        self.motor.duty(0)
