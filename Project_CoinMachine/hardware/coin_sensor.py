from machine import Pin, time_pulse_us
import config.setting as setting
import time

MIN_PULSE_DURATION = 10000  # Duración mínima del pulso (microsegundos)
MAX_PULSE_DURATION = 1000000  # Duración máxima del pulso (microsegundos)

class CoinSensor:
    """
    Clase que gestiona el sensor de monedas.

    Atributos:
    sensor_pin : Pin
        Pin de entrada del sensor de monedas.
    """
    def __init__(self):
        self.sensor_pin = Pin(setting.COIN_SENSOR_PIN, Pin.IN)

    def read_pulse(self, sensor):
        """
        Lee el pulso del sensor y devuelve la duración en microsegundos.

        Parámetros:
        sensor : Pin
            Pin del sensor.

        Retorno:
        int: Duración del pulso en microsegundos o -1 si hay un error.
        """
        try:
            return time_pulse_us(sensor, 1)
        except Exception as e:
            print(f"Error al leer el pulso: {e}")
            return -1

    def detect_coin(self, times=0):
        """
        Detecta si hay una moneda dentro del rango de detección.

        Parámetros:
        times : int
            Número de veces que se verificará la presencia de monedas.

        Retorno:
        bool: True si se detecta una moneda, False en caso contrario.
        """
        sub_times = times
        while times == 0 or sub_times > 0:
            sub_times -= 1
            time.sleep(0.1)
            pulse_time = self.read_pulse(self.sensor_pin)
            if pulse_time == -1:
                continue

            if MIN_PULSE_DURATION < pulse_time < MAX_PULSE_DURATION:
                return True

        return False
