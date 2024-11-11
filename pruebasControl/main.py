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
        self.set_servo_angle(90)

    def close_coin_release(self):
        self.set_servo_angle(180)


#Ejemplo de uso de clase
while True:
    time_release=1

    servo1=CoinRelease(servo_pin=27)
    servo2=CoinRelease(servo_pin=26)

    servo1.open_coin_release()
    time.sleep(time_release)
    servo1.close_coin_release()
    time.sleep(time_release)

    servo2.open_coin_release()
    time.sleep(time_release)
    servo2.close_coin_release()
    time.sleep(time_release)