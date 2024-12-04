from machine import Pin, PWM
import time

class CoinRelease:
    """
    Clase que controla la liberación de monedas.
    
    Atributos:
    servo : PWM
        Controlador PWM del servo.
    min_duty : int
        Deber mínimo para el ángulo del servo.
    max_duty : int
        Deber máximo para el ángulo del servo.
    """
    def __init__(self, servo_pin):
        self.servo = PWM(Pin(servo_pin))
        self.servo.freq(50)
        self.min_duty = 1800
        self.max_duty = 8200

    def set_servo_angle(self, angle):
        """
        Establece el ángulo del servo.
        
        Parámetros:
        angle : int
            Ángulo deseado para el servo.
        """
        angle = max(0, min(180, angle))
        duty = self.min_duty + int((self.max_duty - self.min_duty) * (angle / 180))
        self.servo.duty_u16(duty)

    def open_coin_release(self):
        """Abre la liberación de monedas."""
        self.set_servo_angle(90)

    def close_coin_release(self):
        """Cierra la liberación de monedas."""
        self.set_servo_angle(180)
