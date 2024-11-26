from core.game import Game
from services.mqtt_server import MqttClient
from services.wifi import Wifi
from services.validate_connection import ValidateConnection

wifi = Wifi()
mqtt = MqttClient()
validate_connection = ValidateConnection(mqtt, wifi)

while True:
    validate_connection.validate_connection()
    game = Game(mqtt, validate_connection)
    game.start_game()