
# Pines de los motores
MOTOR_PIN_1 = 18
MOTOR_PIN_1_VELOCITY = 33

MOTOR_PIN_2 = 25
MOTOR_PIN_2_VELOCITY = 26

MOTOR_PIN_3 = 32
MOTOR_PIN_3_VELOCITY = 27

#pines de los encoders 

ENCODER_PIN_MOTOR_1 = 14
ENCODER_PIN_MOTOR_2 = 35
ENCODER_PIN_MOTOR_3 = 13

# Pin palanca (detectar movimiento de paralanca inicio del juego)
JOYSTICK_PIN_X_1 = 36
JOYSTICK_PIN_Y_1 = 39

# Pin servo motor (liberacion de monedas)
SERVO_PIN = 22

# Pin sensor de monedas
COIN_SENSOR_PIN = 34


#Segundos para liberar monedas
WINNER_TIME_BIG = 3
WINNER_TIME_MIDDLE = 1.5

#Wifi settings
WIFI_LED = 19
WIFI_USERNAME = "Hannah"
WIFI_PASSWORD = "hanna2024"

#MQTT settings
MQTT_LED = 21
MQTT_CLIENT_ID = "coin_machine"
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""

MQTT_TOPIC_MONEY = "monedas/dato"
MQTT_TOPIC_MONEY_RESET = "monedas/resetear"
MQTT_TOPIC_WINS = "wins/dato"
