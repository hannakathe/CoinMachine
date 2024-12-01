
from services.mqtt_server import MqttClient
from services.wifi import Wifi

class ValidateConnection:
    def __init__(self, mqtt: MqttClient, wifi: Wifi):
        self.mqtt = mqtt
        self.wifi = wifi

    def validate_connection(self):
        self.wifi.validate_connection()
        self.mqtt.validate_connection()