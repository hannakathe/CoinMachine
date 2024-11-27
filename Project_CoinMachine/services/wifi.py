from machine import Pin
import network
import time

import config.setting as setting


class Wifi:
    def __init__(self):
        led = Pin(setting.WIFI_LED, Pin.OUT)
        led.value(0)

        print("Conectando al WiFi", end="")
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect(setting.WIFI_USERNAME, setting.WIFI_PASSWORD)
        # sta_if.connect('FAMILIA CAMARGO', 'FAMILIA.CASTELLANOS1013')
        while not sta_if.isconnected():
            print(".", end="")
            time.sleep(0.1)
        print(" Connected!")
        led.value(1)

    def validate_connection(self):
        print("Validating connection...")
        #todo