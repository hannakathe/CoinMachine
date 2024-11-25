# boot.py -- run on boot-up
from machine import Pin, SoftI2C
import ssd1306

class Oled:
    def __init__(self):
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))  # Ajusta los pines según tu configuración
        oled_width = 128
        oled_height = 64
        self.oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    def obtener_oled(self):
        return self.oled
