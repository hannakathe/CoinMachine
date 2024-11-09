# Controla la liberación de monedas

from machine import Pin

class CoinRelease:
    def __init__(self, release_pin):
        self.release = Pin(release_pin, Pin.OUT)
    
    def release_coins(self):
        # Activar mecanismo de liberación
        self.release.on()
    
    def stop_release(self):
        # Detener el mecanismo de liberación
        self.release.off()
