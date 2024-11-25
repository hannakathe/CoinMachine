# Controla el buzzer

# buzzer_control.py

from machine import Pin, PWM
import time

class BuzzerControl:
    def __init__(self, buzzer_pin):
        self.buzzer = PWM(Pin(buzzer_pin))
        self.buzzer.duty(0)  # Asegura que el buzzer comience apagado

    def _play_tone(self, frequency, duration):
        """Reproduce un tono en una frecuencia dada por un tiempo específico."""
        self.buzzer.freq(frequency)
        self.buzzer.duty(512)
        time.sleep(duration)
        self.buzzer.duty(0)  # Apaga el buzzer
        time.sleep(0.05)  # Pausa corta entre tonos

    def play_start_sound(self):
        # Melodía de inicio del juego
        tones = [
            (261, 0.1),  # C4
            (294, 0.1),  # D4
            (329, 0.1),  # E4
            (392, 0.15),  # G4
            (440, 0.15)  # A4
        ]
        for freq, dur in tones:
            self._play_tone(freq, dur)
    
    def play_win_sound(self):
        # Melodía de ganancia
        tones = [
            (523, 0.2),  # C5
            (392, 0.1),  # G4
            (440, 0.2),  # A4
            (349, 0.15), # F4
            (523, 0.3),  # C5
            (392, 0.25)  # G4
        ]
        for freq, dur in tones:
            self._play_tone(freq, dur)

