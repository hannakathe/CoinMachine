from machine import Pin, time_pulse_us

import config.setting as setting
import time

# Rango de duraciones del pulso para detectar monedas (ajustar según el sensor)
MIN_PULSE_DURATION = 10000  # Duración mínima del pulso (microsegundos)
MAX_PULSE_DURATION = 1000000  # Duración máxima del pulso (microsegundos)

class CoinSensor(): 
    def __init__(self):
        self.sensor_pin = Pin(setting.SENSOR_PIN, Pin.IN)  # Ajusta este pin según tu conexión

    # Función para leer el pulso del sensor y devolver la duración en microsegundos
    def read_pulse(self, sensor):
        try:
            return time_pulse_us(sensor, 1)  # Detecta el pulso HIGH
        except Exception as e:
            print(f"Error al leer el pulso: {e}")
            return -1  # Retorna -1 si hubo un error

    # Función para detectar si hay una moneda dentro del rango de detección
    def detect_coin(self):
        while True:
            time.sleep(0.1)
            pulse_time = self.read_pulse(self.sensor_pin)
            if pulse_time == -1:
                continue  # Si hubo un error en la lectura, no detectamos moneda

            # Verifica si la duración del pulso está dentro del rango
            if MIN_PULSE_DURATION < pulse_time < MAX_PULSE_DURATION:
                break

