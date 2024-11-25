from reserveMoney import ReserveMoney
from storageMoney import StorageMoney
import time

class Palanca:
    def __init__(self, reserve_money: ReserveMoney, storage_money: StorageMoney):
        self.reserve_money = reserve_money
        self.storage_money = storage_money
        self.game_started = False
    
    def wait_for_press(self):
        print("Esperando que se baje la palanca...")

        while True:
            time.sleep(1)
            #TODO verificar si se presiono la palanca
            self.press_palanca()
            break

        print("¡Palanca abajo! Iniciando el juego.")

    def press_palanca(self):
        print("Se ha precionado la palanca")
        self.reserve_money.remove_money_from_reserve()
        self.storage_money.add_money_to_storage()
        self.game_started = True

    def return_money(self):
        print("Se ha devuelto la moneda de reserva")
        self.reserve_money.remove_money_from_reserve()