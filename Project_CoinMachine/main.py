from core.game import Game
from services.mqtt_server import MqttClient
from services.wifi import Wifi

wifi = Wifi()
mqtt = MqttClient()


while True:
    game = Game(mqtt)
    game.start_game()