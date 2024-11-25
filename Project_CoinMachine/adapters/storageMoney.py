import config.setting as setting
import time

from hardware.coin_release import CoinRelease
from services.mqtt_server import MqttClient

class StorageMoney:
    def __init__(self, mqtt: MqttClient):
        self.drop_money = CoinRelease(release_pin=setting.SERVO_PIN)
        self.mqtt = mqtt
    
    def add_money_to_storage(self):
        print("Añadiendo moneda a la base de datos...")
        self.mqtt.publishMoney("1")

    def drop_money_from_storage(self, seconds = 2):
        print("Soltando monedas...")
        self.drop_money.open_coin_release()
        time.sleep(seconds)
        self.drop_money.close_coin_release()

        print("Eliminando moneda de la base de datos...")
        self.mqtt.publishMoney("-1")
