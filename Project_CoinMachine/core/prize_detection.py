# Lógica de detección de combinaciones ganadoras
import config.setting as setting


class PrizeDetection:
    def check_winner(self, reel_positions: list):
        if (reel_positions[0] == reel_positions[1] == reel_positions[2]): 
            print("Premio mayor")
            return setting.WINNER_TIME_BIG;

        if (reel_positions[0] == reel_positions[1]):
            print("Premio intermedio")
            return setting.WINNER_TIME_MIDDLE;

        if (reel_positions[0] == reel_positions[2]):
            print("Premio intermedio")
            return setting.WINNER_TIME_MIDDLE;

        if (reel_positions[1] == reel_positions[2]):
            print("Premio intermedio")
            return setting.WINNER_TIME_MIDDLE;

        return 0;