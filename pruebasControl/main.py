from machine import Pin, time_pulse_us
import time
import boot  # Importa la clase Oled desde oled.py

# Configura el pin donde está conectado el sensor inductivo
sensor_pin = Pin(15, Pin.IN)  # Asegúrate de que este pin corresponda con tu conexión

# Duraciones de las señales de los diferentes tipos de moneda (en microsegundos)
# Estos valores son ejemplos y deben ser ajustados según las pruebas
TIMER_THRESHOLD_200 = 3000  # Duración mínima de la señal para la moneda de 200
TIMER_THRESHOLD_500 = 5000  # Duración mínima de la señal para la moneda de 500
TIMER_THRESHOLD_1000 = 7000  # Duración mínima de la señal para la moneda de 1000

# Inicializa la pantalla OLED
oled_display = boot.Oled()
oled_screen = oled_display.obtener_oled()

# Función para leer el pulso del sensor y devolver la duración en microsegundos
def read_pulse(sensor):
    # Lee el pulso de la señal del sensor en microsegundos
    pulse_time = time_pulse_us(sensor, 1)  # 1 significa que queremos detectar el pulso HIGH
    return pulse_time

# Función para identificar el tipo de moneda basado en el tiempo del pulso
def detect_coin():
    pulse_time = read_pulse(sensor_pin)
    print(f"Duración del pulso: {pulse_time} microsegundos")
    oled_screen.fill(0)  # Limpia la pantalla OLED
    
    # Determinar el tipo de moneda según la duración del pulso
    if pulse_time > TIMER_THRESHOLD_1000:
        message = "Moneda de 1000 pesos"
    elif pulse_time > TIMER_THRESHOLD_500:
        message = "Moneda de 500 pesos"
    elif pulse_time > TIMER_THRESHOLD_200:
        message = "Moneda de 200 pesos"
    else:
        message = "Moneda no reconocida"
    
    print(message)
    oled_screen.text(message, 0, 0)  # Muestra el mensaje en la pantalla OLED
    oled_screen.show()

# Bucle principal para detectar la moneda continuamente
while True:
    detect_coin()
    time.sleep(1)  # Espera un segundo antes de hacer otra lectura
