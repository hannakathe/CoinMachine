from machine import Pin
import network
import time
import config.setting as setting

class Wifi:
    """
    Clase que gestiona la conexión WiFi.
    
    Atributos:
    led : Pin
        Pin del LED indicador.
    sta_if : network.WLAN
        Interfaz de red WiFi.
    """
    def __init__(self):
        led = Pin(setting.WIFI_LED, Pin.OUT)
        led.value(0)

        print("Conectando al WiFi", end="")
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect(setting.WIFI_USERNAME, setting.WIFI_PASSWORD)
        while not sta_if.isconnected():
            print(".", end="")
            time.sleep(0.1)
        print(" Connected!")
        led.value(1)

    def validate_connection(self):
        """
        Valida la conexión WiFi.
        """
        print("Validating connection...")
        # TODO: Implement validation logic
