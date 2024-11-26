from adapters.reserveMoney import ReserveMoney
from adapters.storageMoney import StorageMoney
from adapters.palanca import Palanca
from adapters.ruleta import Ruleta

from hardware.coin_release import CoinRelease
from services.mqtt_server import MqttClient
from services.validate_connection import ValidateConnection

import config.setting as setting
import time


class Game:
    def __init__(self, mqtt: MqttClient, validate_connection: ValidateConnection):
        print("Iniciando el juego...")
        self.mqtt = mqtt
        self.reserve_money = ReserveMoney()
        self.storage_money = StorageMoney(mqtt)
        self.palanca = Palanca(self.reserve_money, self.storage_money)
        self.ruleta = Ruleta()


    def start_game(self):
        self.step_1_await_for_money()
        self.step_3_reel()


    #Esperar que entre una moneda a la reserva
    def step_1_await_for_money(self):
        self.reserve_money.await_for_money_in_reserve()
        self.step_2_await_for_press_palanca()


    #Esperar que se presione la palanca
    def step_2_await_for_press_palanca(self):
        self.palanca.wait_for_press()

        #Validamos por que el juego no ha empezado
        if (self.palanca.game_started == False):
            #Validamos si hay una moneda en la reserva
            if (self.reserve_money.is_money_in_reserve() == False):
                self.step_1_await_for_money()
            else: 
                self.step_2_await_for_press_palanca()


    def step_3_reel(self):
        spin_response = self.ruleta.spin_response()
        if (spin_response):
            self.mqtt.publishWin("1")
            self.storage_money.drop_money_from_storage()