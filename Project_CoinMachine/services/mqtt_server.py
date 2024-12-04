from machine import Pin
from umqtt.simple import MQTTClient
import time
import config.setting as setting

class MqttClient:
    """
    Clase que gestiona la conexión y publicación de mensajes mediante MQTT.
    
    Atributos:
    client : MQTTClient
        Cliente MQTT para la comunicación de datos.
    """
    def __init__(self):
        MQTT_CLIENT_ID = setting.MQTT_CLIENT_ID
        MQTT_BROKER = setting.MQTT_BROKER
        MQTT_USER = setting.MQTT_USER
        MQTT_PASSWORD = setting.MQTT_PASSWORD

        led = Pin(setting.MQTT_LED, Pin.OUT)
        led.value(0)

        def connect():
            """
            Conecta al servidor MQTT.
            
            Retorno:
            MQTTClient: Cliente MQTT conectado.
            """
            print("Conectando a MQTT... ", end="")
            client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
            client.connect()
            led.value(1)
            return client

        while True:
            try:
                self.client = connect()
                break
            except Exception as e:
                print(f"Connection failed, retrying in 2 seconds... Error: {e}")
                time.sleep(2)

    def publishMoney(self, msg):
        """
        Publica el mensaje de dinero en el tópico correspondiente.
        
        Parámetros:
        msg : str
            Mensaje a publicar.
        """
        self.client.publish(setting.MQTT_TOPIC_MONEY, msg)

    def resetMoney(self, msg):
        """
        Publica el mensaje para resetear el dinero en el tópico correspondiente.
        
        Parámetros:
        msg : str
            Mensaje a publicar.
        """
        self.client.publish(setting.MQTT_TOPIC_MONEY_RESET, msg)

    def publishWin(self, msg):
        """
        Publica el mensaje de victoria en el tópico correspondiente.
        
        Parámetros:
        msg : str
            Mensaje a publicar.
        """
        self.client.publish(setting.MQTT_TOPIC_WINS, msg)

    def validate_connection(self):
        """
        Valida la conexión con el servidor MQTT.
        """
        print("Validating connection...")
