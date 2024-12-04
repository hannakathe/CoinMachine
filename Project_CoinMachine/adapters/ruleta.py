import config.setting as setting
import time
import random
from hardware.motor_control import MotorControl
from core.prize_detection import PrizeDetection

class Ruleta:
    def __init__(self):
        print("Ruleta")
        self.motor1 = MotorControl(PIN_MOTOR=setting.MOTOR_PIN_1, PIN_VELOCITY=setting.MOTOR_PIN_1_VELOCITY)
        self.motor2 = MotorControl(PIN_MOTOR=setting.MOTOR_PIN_2, PIN_VELOCITY=setting.MOTOR_PIN_2_VELOCITY)
        self.motor3 = MotorControl(PIN_MOTOR=setting.MOTOR_PIN_3, PIN_VELOCITY=setting.MOTOR_PIN_3_VELOCITY)

    def spin_response(self):
        # Girar los motores durante tiempos diferentes (entre 3 y 5 segundos)
        print("Girando ruleta...")
        
        # Los motores giran por un tiempo aleatorio entre 3 y 5 segundos
        motor1_time = random.uniform(3, 5)  # Tiempo aleatorio entre 3 y 5 segundos
        motor2_time = random.uniform(3, 5)  # Tiempo aleatorio entre 3 y 5 segundos
        motor3_time = random.uniform(3, 5)  # Tiempo aleatorio entre 3 y 5 segundos

        # Iniciar el giro de los motores
        self.motor1.random_spin()
        self.motor2.random_spin()
        self.motor3.random_spin()

        # Esperar el tiempo necesario para cada motor antes de proceder
        # Esta espera garantiza que el código no avance hasta que todos los motores terminen
        time.sleep(max(motor1_time, motor2_time, motor3_time))

        # Detectar la posición de los motores
        print("Detectando posicion")
        prize_detector = PrizeDetection([
            self.motor1.get_position(),
            self.motor2.get_position(),
            self.motor3.get_position()
        ])

        # Volver a la posición inicial de los motores
        print("Volviendo a la posición inicial")
        self.motor1.turn_initial_position()
        self.motor2.turn_initial_position()
        self.motor3.turn_initial_position()

        return prize_detector.check_winner()
