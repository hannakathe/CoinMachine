from services.mqtt_server import MqttClient
from services.wifi import Wifi

class ValidateConnection:
    """
    Clase que valida la conexión de servicios MQTT y WiFi.
    
    Atributos:
    mqtt : MqttClient
        Cliente MQTT para la comunicación de datos.
    wifi : Wifi
        Cliente WiFi para la conexión de red.
    """
    def __init__(self, mqtt: MqttClient, wifi: Wifi):
        self.mqtt = mqtt
        self.wifi = wifi

    def validate_connection(self):
        """
        Valida las conexiones de WiFi y MQTT.
        """
        self.wifi.validate_connection()
        self.mqtt.validate_connection()
