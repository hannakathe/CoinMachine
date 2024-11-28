# Lógica de detección de combinaciones ganadoras
import config.setting as setting


class PrizeDetection:

    def __init__(self, reel_positions: list):
        self.reserve_money = reserve_money
        self.storage_money = storage_money
        self.game_started = False
        self.joystick = JoystickControl(x_pin=setting.JOYSTICK_PIN_X_1, y_pin=setting.JOYSTICK_PIN_Y_1)
        self.reel_positions = reel_positions
        #self.coin_release = CoinRelease(setting.SERVO_PIN_RESERVE) 
        #TODO RETIRAR PRIMER SERVO 

    def check_winner(self):
        if (self.reel_positions[0] == self.reel_positions[1] == self.reel_positions[2]): 
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