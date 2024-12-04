import config.setting as setting
import time
import random
from hardware.motor_control import MotorControl
from core.prize_detection import PrizeDetection


class Ruleta:
    """ Clase que representa la ruleta de la máquina tragamonedas. 

    Atributos: 
    motor1 : MotorControl 
        Controlador del primer motor de la ruleta. 
    motor2 : MotorControl 
        Controlador del segundo motor de la ruleta. 
    motor3 : MotorControl 
        Controlador del tercer motor de la ruleta. """
    def __init__(self):
        print("Ruleta")
        self.motor1 = MotorControl(PIN_MOTOR=setting.MOTOR_PIN_1, PIN_VELOCITY=setting.MOTOR_PIN_1_VELOCITY)
        self.motor2 = MotorControl(PIN_MOTOR=setting.MOTOR_PIN_2, PIN_VELOCITY=setting.MOTOR_PIN_2_VELOCITY)
        self.motor3 = MotorControl(PIN_MOTOR=setting.MOTOR_PIN_3, PIN_VELOCITY=setting.MOTOR_PIN_3_VELOCITY)

    def spin_response(self):
        """ Gira la ruleta y detecta la posición final de los motores. 
        Retorno: 
        bool: Indica si hay un ganador basado en la detección de premios. """

        print("Girando ruleta...")
        self.motor1.start_spin()
        self.motor2.start_spin()
        self.motor3.start_spin()
        
        time.sleep(max(random.uniform(3, 5), random.uniform(3, 5), random.uniform(3, 5)))  # Tiempo aleatorio

        self.motor1.stop_spin()
        self.motor2.stop_spin()
        self.motor3.stop_spin()

        print("Detectando posición")
        prize_detector = PrizeDetection([
            self.motor1.get_position(),
            self.motor2.get_position(),
            self.motor3.get_position()
        ])

        print("Volviendo a la posición inicial")
        self.motor1.turn_initial_position()
        self.motor2.turn_initial_position()
        self.motor3.turn_initial_position()

        return prize_detector.check_winner()
