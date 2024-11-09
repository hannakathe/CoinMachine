# Controlado mediante el movimiento 

from machine import Pin
import time

class ButtonControl:
    def __init__(self, button_pin):
        # button_pin=21
        self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
    
    def is_button_pressed(self):
        # Verifica si el botón está presionado
        return self.button.value() == 0  # 0 para presionar (PULL_UP)
    
    def wait_for_press(self):
        # Espera hasta que el botón sea presionado
        print("Esperando que se presione el botón para iniciar el juego...")
        while not self.is_button_pressed():
            time.sleep(0.1)  # Evita un bucle muy rápido
        print("¡Botón presionado! Iniciando el juego.")


prueba=ButtonControl()