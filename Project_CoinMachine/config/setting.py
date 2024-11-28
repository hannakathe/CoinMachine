
# Pines de los motores
MOTOR_PIN_1_LEFT = 2
MOTOR_PIN_1_RIGHT = 4
MOTOR_PIN_1_VELOCITY = 27

MOTOR_PIN_2_LEFT = 33
MOTOR_PIN_2_RIGHT = 32
MOTOR_PIN_2_VELOCITY = 25

MOTOR_PIN_3_LEFT = 3
MOTOR_PIN_3_RIGHT = 1
MOTOR_PIN_3_VELOCITY = 26

# Pin palanca (detectar movimiento de paralanca inicio del juego)
JOYSTICK_PIN_X_1 = 36
JOYSTICK_PIN_Y_1 = 39

# Pin buzzer (sonido)
BUZZER_PIN = 5  #TODO revisar pin

# Pin servo motor (liberacion de monedas)
SERVO_PIN = 22
SERVO_PIN_RESERVE = 23

# Pin sensor de monedas
COIN_SENSOR_PIN = 15


#Segundos para liberar monedas
WINNER_TIME_BIG = 3
WINNER_TIME_MIDDLE = 1.5

#Wifi settings
WIFI_LED = 19
WIFI_USERNAME = "Hannah"
WIFI_PASSWORD = "hanna2024"

#MQTT settings
MQTT_LED = 18
MQTT_CLIENT_ID = "coin_machine"
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""

MQTT_TOPIC_MONEY = "monedas/dato"
MQTT_TOPIC_MONEY_RESET = "monedas/resetear"
MQTT_TOPIC_WINS = "wins/dato"
