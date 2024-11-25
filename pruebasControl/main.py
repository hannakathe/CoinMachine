from machine import Pin, time_pulse_us
import time

# Configura el pin donde está conectado el sensor inductivo
sensor_pin = Pin(15, Pin.IN)  # Asegúrate de que este pin corresponda con tu conexión

# Duraciones de las señales de los diferentes tipos de moneda (en microsegundos)
# Estos valores son ejemplos y deben ser ajustados según las pruebas
TIMER_THRESHOLD_200 = 3000  # Duración mínima de la señal para la moneda de 200
TIMER_THRESHOLD_500 = 5000  # Duración mínima de la señal para la moneda de 500
TIMER_THRESHOLD_1000 = 7000  # Duración mínima de la señal para la moneda de 1000

# Función para leer el pulso del sensor y devolver la duración en microsegundos
def read_pulse(sensor):
    # Lee el pulso de la señal del sensor en microsegundos
    pulse_time = time_pulse_us(sensor, 1)  # 1 significa que queremos detectar el pulso HIGH
    return pulse_time

# Función para identificar el tipo de moneda basado en el tiempo del pulso
def detect_coin():
    pulse_time = read_pulse(sensor_pin)
    print(f"Duración del pulso: {pulse_time} microsegundos")
    
    # Determinar el tipo de moneda según la duración del pulso
    if pulse_time > TIMER_THRESHOLD_1000:
        print("Moneda de 1000 pesos detectada")
    elif pulse_time > TIMER_THRESHOLD_500:
        print("Moneda de 500 pesos detectada")
    elif pulse_time > TIMER_THRESHOLD_200:
        print("Moneda de 200 pesos detectada")
    else:
        print("Moneda no reconocida o fuera del rango esperado")

# Bucle principal para detectar la moneda continuamente
while True:
    detect_coin()
    time.sleep(1)  # Espera un segundo antes de hacer otra lectura
