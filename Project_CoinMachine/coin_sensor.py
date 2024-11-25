from machine import Pin, time_pulse_us
import time


# Configura el pin donde está conectado el sensor inductivo
sensor_pin = Pin(15, Pin.IN)  # Ajusta este pin según tu conexión

# Rango de duraciones del pulso para detectar monedas (ajustar según el sensor)
MIN_PULSE_DURATION = 10000  # Duración mínima del pulso (microsegundos)
MAX_PULSE_DURATION = 1000000  # Duración máxima del pulso (microsegundos)

# Contador de monedas
coin_count = 0

# Función para leer el pulso del sensor y devolver la duración en microsegundos
def read_pulse(sensor):
    try:
        return time_pulse_us(sensor, 1)  # Detecta el pulso HIGH
    except Exception as e:
        print(f"Error al leer el pulso: {e}")
        return -1  # Retorna -1 si hubo un error

# Función para detectar si hay una moneda dentro del rango de detección
def detect_coin():
    pulse_time = read_pulse(sensor_pin)
    if pulse_time == -1:
        return False  # Si hubo un error en la lectura, no detectamos moneda

    print(f"Duración del pulso: {pulse_time} microsegundos")

    # Verifica si la duración del pulso está dentro del rango
    if MIN_PULSE_DURATION < pulse_time < MAX_PULSE_DURATION:
        return True  # Se detectó una moneda
    else:
        return False  # No se detectó moneda

# Bucle principal para detectar monedas e imprimir el contador en consola
while True:
    if detect_coin():
        coin_count += 1  # Incrementa el contador de monedas
        print(f"Moneda detectada. Total de monedas: {coin_count}")  # Imprime el contador de monedas
    else:
        print("No se detectó moneda.")  # Imprime que no se detectó moneda
    
    time.sleep(0.1)  # Breve pausa antes de la próxima lectura
