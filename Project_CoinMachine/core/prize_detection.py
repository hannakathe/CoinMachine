# Lógica de detección de combinaciones ganadoras
import config.setting as setting
from adapters.storageMoney import StorageMoney
from adapters.reserveMoney import ReserveMoney
from hardware.joystick_control import JoystickControl

class PrizeDetection:
    """
    Clase que gestiona la detección de combinaciones ganadoras.

    Atributos:
    reel_positions : list
        Lista con las posiciones de los carretes.
    reserve_money : StorageMoney
        Instancia para manejar el almacenamiento de dinero.
    storage_money : ReserveMoney
        Instancia para manejar el dinero en reserva.
    game_started : bool
        Estado que indica si el juego ha comenzado.
    joystick : JoystickControl
        Controlador del joystick para detectar movimientos.
    """
    def __init__(self, reel_positions: list):
        self.reserve_money = ReserveMoney()
        self.storage_money = StorageMoney()
        self.game_started = False
        self.joystick = JoystickControl(x_pin=setting.JOYSTICK_PIN_X_1, y_pin=setting.JOYSTICK_PIN_Y_1)
        self.reel_positions = reel_positions
    

    def check_winner(self):
        """
        Verifica si hay una combinación ganadora.

        Retorno:
        bool: Verdadero si hay una combinación ganadora, Falso en caso contrario.
        """
        if self.reel_positions[0] == self.reel_positions[1] == self.reel_positions[2]: 
            print("Premio mayor")
            return True

        '''
        if (self.reel_positions[0] == self.reel_positions[1]):
            print("Premio intermedio")
            return setting.WINNER_TIME_MIDDLE;

        if (self.reel_positions[0] == self.reel_positions[2]):
            print("Premio intermedio")
            return setting.WINNER_TIME_MIDDLE;

        if (self.reel_positions[1] == self.reel_positions[2]):
            print("Premio intermedio")
            return setting.WINNER_TIME_MIDDLE;
        '''

        return False
