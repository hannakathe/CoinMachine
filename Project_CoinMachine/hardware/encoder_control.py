from machine import Pin
import time

class EncoderControl:
    """
    Clase que gestiona el control de un encoder óptico incremental.

    Atributos:
    encoder_pin : Pin
        Pin de entrada del encoder.
    brake_button : Pin
        Pin de entrada del botón de frenado.
    pulse_count : int
        Contador de pulsos del encoder.
    pulses_end : int
        Número de pulsos que representa el final del recorrido.
    brake_triggered : bool
        Estado del botón de frenado.
    """
    def __init__(self, encoder_pin, brake_button_pin, pulses_end):
        self.encoder_pin = Pin(encoder_pin, Pin.IN)
        self.encoder_pin.irq(trigger=Pin.IRQ_RISING, handler=self._pulse_count)

        self.brake_button = Pin(brake_button_pin, Pin.IN, Pin.PULL_UP)
        self.brake_button.irq(trigger=Pin.IRQ_FALLING, handler=self._brake_button_pressed)

        self.pulse_count = 0
        self.pulses_end = pulses_end
        self.brake_triggered = False

    def _pulse_count(self, pin):
        """Manejador de interrupción que cuenta los pulsos del encoder."""
        self.pulse_count += 1

    def _brake_button_pressed(self, pin):
        """Manejador de interrupción para el botón de frenado."""
        if self.is_at_start():
            self.brake_triggered = True
            print("Frenado iniciado por el botón de retorno.")

    def reset_position(self):
        """Restablece el contador de pulsos a 0."""
        self.pulse_count = 0
        self.brake_triggered = False

    def is_at_start(self):
        """Verifica si el motor está en la posición inicial."""
        return self.pulse_count == 0

    def is_at_end(self):
        """Verifica si el motor está en la posición final."""
        return self.pulse_count >= self.pulses_end

    def get_position(self):
        """Retorna la posición actual en base a los pulsos contados."""
        return self.pulse_count

    def wait_until_end(self):
        """Espera hasta que el motor llegue a la posición final."""
        while not self.is_at_end():
            time.sleep(0.01)
        print("Posición final alcanzada.")

    def wait_until_start(self):
        """Espera hasta que el motor llegue a la posición inicial."""
        while not self.is_at_start():
            time.sleep(0.01)
        print("Posición inicial alcanzada.")

    def has_brake_triggered(self):
        """Verifica si el botón de frenado fue presionado al retornar a la posición inicial."""
        return self.brake_triggered
