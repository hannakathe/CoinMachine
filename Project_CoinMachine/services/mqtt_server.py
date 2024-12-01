from machine import Pin
from umqtt.simple import MQTTClient
import time
import config.setting as setting

class MqttClient :
    def __init__(self):
      MQTT_CLIENT_ID = setting.MQTT_CLIENT_ID
      MQTT_BROKER    = setting.MQTT_BROKER
      MQTT_USER      = setting.MQTT_USER
      MQTT_PASSWORD  = setting.MQTT_PASSWORD

      led = Pin(setting.MQTT_LED, Pin.OUT)
      led.value(0)

      def connect(): 
        print("Conectando a MQTT... ", end="")
        client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
        client.connect()
        led.value(1)
        return client

      while True:
        try:
          self.client = connect()
          break
        except:
          print("Connection failed, retrying in 2 seconds...")
          time.sleep(2)

    def publishMoney(self, msg):
        self.client.publish(setting.MQTT_TOPIC_MONEY, msg)

    def resetMoney(self, msg):
        self.client.publish(setting.MQTT_TOPIC_MONEY_RESET, msg)

    def publishWin(self, msg):
        self.client.publish(setting.MQTT_TOPIC_WINS, msg)

    def validate_connection(self):
        print("Validating connection...")
        #todo