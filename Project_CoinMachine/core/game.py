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
    """
    Clase que representa el juego de la máquina tragamonedas.

    Atributos:
    mqtt : MqttClient
        Cliente MQTT para la comunicación de datos.
    reserve_money : ReserveMoney
        Instancia para manejar el dinero en reserva.
    storage_money : StorageMoney
        Instancia para manejar el almacenamiento del dinero.
    palanca : Palanca
        Controlador de la palanca.
    ruleta : Ruleta
        Controlador de la ruleta.
    """
    def __init__(self, mqtt: MqttClient, validate_connection: ValidateConnection):
        print("Iniciando el juego...")
        self.mqtt = mqtt
        self.reserve_money = ReserveMoney()
        self.storage_money = StorageMoney(mqtt)
        self.palanca = Palanca(self.reserve_money, self.storage_money)
        self.ruleta = Ruleta()

    def start_game(self):
        """Inicia el juego ejecutando las etapas iniciales."""
        self.step_1_await_for_money()
        self.step_3_reel()

    def step_1_await_for_money(self):
        """Espera que entre una moneda a la reserva."""
        self.reserve_money.await_for_money_in_reserve()
        self.step_2_await_for_press_palanca()

    def step_2_await_for_press_palanca(self):
        """Espera que se presione la palanca para iniciar el juego."""
        self.palanca.wait_for_press()

        # Validar si el juego ha comenzado
        if not self.palanca.game_started:
            # Verificar si hay una moneda en la reserva
            if not self.reserve_money.is_money_in_reserve():
                self.step_1_await_for_money()
            else:
                self.step_2_await_for_press_palanca()

    def step_3_reel(self):
        """Gira la ruleta y maneja el resultado."""
        spin_response = self.ruleta.spin_response()
        if spin_response:
            self.mqtt.publishWin("1")
            self.storage_money.drop_money_from_storage()
