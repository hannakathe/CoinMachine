import config.setting as setting
import time

from hardware.coin_release import CoinRelease
from services.mqtt_server import MqttClient

class StorageMoney:
    def __init__(self, mqtt: MqttClient):
        self.drop_money = CoinRelease(setting.SERVO_PIN)
        self.mqtt = mqtt
    
    def add_money_to_storage(self, counter_money):
        print("Añadiendo moneda a la base de datos...")
        self.mqtt.publishMoney(str(counter_money))

    def drop_money_from_storage(self):
        print("Soltando monedas...")
        self.drop_money.open_coin_release()
        time.sleep(10)
        self.drop_money.close_coin_release()

        print("Eliminando moneda de la base de datos...")
        self.mqtt.resetMoney("Resetear")
