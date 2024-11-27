# Controla la liberación de monedas parte superior

from machine import Pin, PWM
import time

class CoinRelease:
    def __init__(self,servo_pin):
        self.servo=PWM(Pin(servo_pin))
        self.servo.freq(50)
        self.min_duty=1800
        self.max_duty=8200

    def set_servo_angle(self, angle):
        angle=max(0,min(180,angle))
        duty=self.min_duty + int((self.max_duty - self.min_duty) * (angle/180))
        self.servo.duty_u16(duty)

    #Posiciones de la palanca

    def open_coin_release(self):
        self.set_servo_angle(0)

    def close_coin_release(self):
        self.set_servo_angle(180)



