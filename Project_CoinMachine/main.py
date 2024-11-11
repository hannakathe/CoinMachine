# Archivo principal donde se importa

from motor_control import MotorControl
from button_control import ButtonControl
from buzzer_control import BuzzerControl
from prize_detection import PrizeDetection
from Project_CoinMachine.coin_release import CoinRelease

# Inicialización de los componentes
motor1 = MotorControl(motor_pin=5)
motor2 = MotorControl(motor_pin=18)
motor3 = MotorControl(motor_pin=19)

button1 = ButtonControl(button_pin=21)
buzzer = BuzzerControl(buzzer_pin=22)
prize_detector = PrizeDetection()
coin_mechanism = CoinRelease(release_pin=23)

# Ejecución del flujo de juego
def start_game():
    button1.wait_for_press()  # Espera a que se presione el botón
    
    buzzer.play_start_sound()
    
    # Inicio del giro de los rodillos
    motor1.start_spin()
    motor2.start_spin()
    motor3.start_spin()
    
    # Simulación de la detención progresiva de cada motor
    motor1.stop_spin()
    motor2.stop_spin()
    motor3.stop_spin()
    
    # Verificación de ganancia
    reel_positions = [1, 1, 1]  # Ejemplo de posiciones de rodillos
    if prize_detector.check_winner(reel_positions):
        buzzer.play_win_sound()
        coin_mechanism.release_coins()
    else:
        print("No hay ganancia")
    
    coin_mechanism.stop_release()

# Llama a la función de inicio del juego
start_game()
