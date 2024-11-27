from hardware.coin_sensor import CoinSensor

# Clase que gestiona la validacion de detectar que ha ingresado una moneda
class ReserveMoney:
    def __init__(self):
        print("Push Money")
        self.money_detected = False
        self.coin_sensor = CoinSensor()
        self.counter_money = 0

    def push_money_to_reserve(self):
        self.counter_money += 1
        self.money_detected = True

    def remove_money_from_reserve(self):
        self.counter_money = 0
        self.money_detected = False

    def is_money_in_reserve(self):
        return self.money_detected


    def await_for_money_in_reserve(self, times = 0):
        print("Esperando que se ingrese una moneda...")
        if self.coin_sensor.detect_coin(times):
            self.push_money_to_reserve()
            print("¡Moneda ingresada! Iniciando el juego.")
            self.await_for_money_in_reserve(10)
