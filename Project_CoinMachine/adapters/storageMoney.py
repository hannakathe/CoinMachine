import config.setting as setting
import time

from hardware.coin_release import CoinRelease
from services.mqtt_server import MqttClient

class StorageMoney:
    """
    Clase que gestiona el almacenamiento de dinero en la máquina tragamonedas.

    Atributos:
    drop_money : CoinRelease
        Controlador del liberador de monedas.
    mqtt : MqttClient
        Cliente MQTT para la comunicación de datos.
    """
    def __init__(self, mqtt: MqttClient):
        self.drop_money = CoinRelease(setting.SERVO_PIN)
        self.mqtt = mqtt
    
    def add_money_to_storage(self, counter_money):
        """
        Añade el conteo de dinero a la base de datos mediante MQTT.

        Parámetros:
        counter_money : int
            Número de monedas a añadir.
        """
        print("Añadiendo moneda a la base de datos...")
        self.mqtt.publishMoney(str(counter_money))

    def drop_money_from_storage(self):
        """
        Suelta las monedas del almacenamiento y resetea la base de datos.

        """
        print("Soltando monedas...")
        self.drop_money.open_coin_release()
        time.sleep(1)
        self.drop_money.close_coin_release()

        print("Eliminando moneda de la base de datos...")
        self.mqtt.resetMoney("Resetear")
