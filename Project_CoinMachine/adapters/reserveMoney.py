from hardware.coin_sensor import CoinSensor

class ReserveMoney:
    """
    Clase que gestiona la validación de detectar que ha ingresado una moneda.

    Atributos:
    money_detected : bool
        Indica si se ha detectado dinero en reserva.
    coin_sensor : CoinSensor
        Sensor utilizado para detectar monedas.
    counter_money : int
        Contador de monedas en reserva.
    """
    def __init__(self):
        print("Push Money")
        self.money_detected = False
        self.coin_sensor = CoinSensor()
        self.counter_money = 0

    def push_money_to_reserve(self):
        self.counter_money += 1
        self.money_detected = True

    def remove_money_from_reserve(self):
        self.counter_money = 0
        self.money_detected = False

    def is_money_in_reserve(self):
        return self.money_detected

    def await_for_money_in_reserve(self, times=0):
        """
        Espera a que se ingrese una moneda en la reserva.

        Parámetros:
        times : int
            Número de veces que se verificará la presencia de monedas.
        """
        print("Esperando que se ingrese una moneda...")
        while not self.coin_sensor.detect_coin(times):
            time.sleep(0.1)  # Pausar brevemente para evitar sobrecargar el CPU
        self.push_money_to_reserve()
        print("¡Moneda ingresada! Iniciando el juego.")
