from machine import Pin, ADC
import time

class JoystickControl:
    """
    Clase que controla el joystick mediante el movimiento.
    
    Atributos:
    x_pin : ADC
        Pin ADC para el eje X del joystick.
    y_pin : ADC
        Pin ADC para el eje Y del joystick.
    threshold_down : int
        Umbral para detectar cuando el joystick está hacia abajo.
    """
    def __init__(self, x_pin, y_pin, THRESHOLD_DOWN=1000):
        self.x_pin = ADC(Pin(x_pin))
        self.y_pin = ADC(Pin(y_pin))
        self.threshold_down = THRESHOLD_DOWN  

        self.x_pin.atten(ADC.ATTN_11DB)  
        self.y_pin.atten(ADC.ATTN_11DB)
        
    def joystick_is_down(self):
        """
        Verifica si el joystick está hacia abajo.
        
        Retorno:
        bool: True si el joystick está hacia abajo, False en caso contrario.
        """
        y_value = self.y_pin.read()
        return y_value < self.threshold_down

    def wait_for_press(self):
        """
        Espera hasta que el joystick se mueva hacia abajo.
        """
        print("Esperando que se baje la palanca...")
        while not self.joystick_is_down():
            time.sleep(0.1)  # Evita un bucle muy rápido
        print("¡Palanca abajo! Iniciando el juego.")

    def get_position(self):
        """
        Obtiene la posición actual del joystick.
        
        Retorno:
        tuple: Valores actuales del eje X y del eje Y.
        """
        x_value = self.x_pin.read()
        y_value = self.y_pin.read()
        return x_value, y_value
