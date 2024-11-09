# Lógica de detección de combinaciones ganadoras

class PrizeDetection:
    def check_winner(self, reel_positions):
        # Lógica para verificar combinación ganadora
        return reel_positions[0] == reel_positions[1] == reel_positions[2]
