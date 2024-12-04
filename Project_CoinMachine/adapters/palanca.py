import config.setting as setting
from hardware.joystick_control import JoystickControl
from adapters.reserveMoney import ReserveMoney
from adapters.storageMoney import StorageMoney
import time

""" Clase que representa la palanca de la máquina tragamonedas. 

Atributos: reserve_money : ReserveMoney 
    Instancia para manejar el dinero en reserva. 
storage_money : StorageMoney 
    Instancia para manejar el almacenamiento del dinero. 
game_started : bool 
    Estado que indica si el juego ha comenzado. 
joystick : JoystickControl 
    Controlador del joystick para detectar movimientos. """

class Palanca:
    def __init__(self, reserve_money: ReserveMoney, storage_money: StorageMoney):
        self.reserve_money = reserve_money
        self.storage_money = storage_money
        self.game_started = False
        self.joystick = JoystickControl(x_pin=setting.JOYSTICK_PIN_X_1, y_pin=setting.JOYSTICK_PIN_Y_1)
    
    def wait_for_press(self):
        print("Esperando que se baje la palanca...")

        while True:
            time.sleep(0.1)
            if self.joystick.joystick_is_down():
                self.press_palanca()
                break

        print("¡Palanca abajo! Iniciando el juego.")

    def press_palanca(self):
        print("Se ha presionado la palanca")

        self.storage_money.add_money_to_storage(self.reserve_money.counter_money)
        self.reserve_money.remove_money_from_reserve()
        self.game_started = True

    def return_money(self):
        print("Se ha devuelto la moneda de reserva")
        self.reserve_money.remove_money_from_reserve()