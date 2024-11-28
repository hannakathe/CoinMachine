import config.setting as setting
from hardware.joystick_control import JoystickControl
from adapters.reserveMoney import ReserveMoney
from adapters.storageMoney import StorageMoney
from hardware.coin_release import CoinRelease
import time

class Palanca:
    def __init__(self, reserve_money: ReserveMoney, storage_money: StorageMoney):
        self.reserve_money = reserve_money
        self.storage_money = storage_money
        self.game_started = False
        self.joystick = JoystickControl(x_pin=setting.JOYSTICK_PIN_X_1, y_pin=setting.JOYSTICK_PIN_Y_1)
        #self.coin_release = CoinRelease(setting.SERVO_PIN_RESERVE) 
        #TODO RETIRAR PRIMER SERVO 
    
    def wait_for_press(self):
        print("Esperando que se baje la palanca...")

        while True:
            time.sleep(0.1)
            if self.joystick.joystick_is_down():
                self.press_palanca()
                break

        print("¡Palanca abajo! Iniciando el juego.")

    def press_palanca(self):
        print("Se ha precionado la palanca")

        #TODO RETIRAR PRIMER SERVO
        """ self.coin_release.open_coin_release() 
        time.sleep(1)
        self.coin_release.close_coin_release() """

        self.storage_money.add_money_to_storage(self.reserve_money.counter_money)
        self.reserve_money.remove_money_from_reserve()
        self.game_started = True

    def return_money(self):
        print("Se ha devuelto la moneda de reserva")
        self.reserve_money.remove_money_from_reserve()