# Controlado mediante el movimiento 

from machine import Pin, ADC
import time


class JoystickControl:
    def __init__(self, x_pin, y_pin,THRESHOLD_DOWN = 1000):
        self.x_pin = ADC(Pin(x_pin))
        self.y_pin = ADC(Pin(y_pin))
        
        self.threshold_down = THRESHOLD_DOWN  

        self.x_pin.atten(ADC.ATTN_11DB)  
        self.y_pin.atten(ADC.ATTN_11DB)
        
    def joystick_is_down(self):
        y_value = self.y_pin.read()
        return y_value < self.THRESHOLD_DOWN

    def wait_for_press(self):
        print("Esperando que se baje la palanca...")
        while not self.joystick_is_down():
            time.sleep(0.1)  # Evita un bucle muy rápido
        print("¡Palanca abajo! Iniciando el juego.")

    def get_position(self):
        x_value = self.x_pin.read()
        y_value = self.y_pin.read()
        return x_value, y_value
    
prueba=PalancaControl()