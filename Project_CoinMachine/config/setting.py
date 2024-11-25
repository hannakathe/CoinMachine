
# Pines de los motores
MOTOR_PIN_1 = 5
MOTOR_PIN_2 = 18
MOTOR_PIN_3 = 19

# Pin palanca (detectar movimiento de paralanca inicio del juego)
JOYSTICK_PIN_X_1 = 30
JOYSTICK_PIN_Y_1 = 33

# Pin buzzer (sonido)
BUZZER_PIN = 22

# Pin servo motor (liberacion de monedas)
SERVO_PIN = 23


#Segundos para liberar monedas
WINNER_TIME_BIG = 3
WINNER_TIME_MIDDLE = 1.5

#Wifi settings
WIFI_USERNAME = "Hannah"
WIFI_PASSWORD = "hanna2024"

#MQTT settings
MQTT_CLIENT_ID = "coin_machine"
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""

MQTT_TOPIC_MONEY = "monedas/dato"
MQTT_TOPIC_WINS = "wins/dato"
