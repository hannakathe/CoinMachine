import time
import config.setting as setting

from hardware.joystick_control import JoystickControl

# Clase que gestiona la validacion de detectar que ha ingresado una moneda
class ReserveMoney:
    def __init__(self):
        print("Push Money")
        self.money_detected = False
        self.joystick = JoystickControl(x_pin=setting.JOYSTICK_PIN_X_1, y_pin=setting.JOYSTICK_PIN_Y_1)

    def push_money_to_reserve(self):
        self.money_detected = True

    def remove_money_from_reserve(self):
        self.money_detected = False

    def is_money_in_reserve(self):
        return self.money_detected


    def await_for_money_in_reserve(self):
        print("Esperando que se ingrese una moneda...")
        self.joystick.wait_for_press();
        self.push_money_to_reserve()
        print("¡Moneda ingresada! Iniciando el juego.")

