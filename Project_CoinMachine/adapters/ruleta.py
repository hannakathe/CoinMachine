import config.setting as setting
import time

from hardware.motor_control import MotorControl
from hardware.buzzer_control import BuzzerControl
from core.prize_detection import PrizeDetection

class Ruleta:
    def __init__(self):
        print("Ruleta")
        self.motor1 = MotorControl(motor_pin=setting.MOTOR_PIN_1)
        self.motor2 = MotorControl(motor_pin=setting.MOTOR_PIN_2)
        self.motor3 = MotorControl(motor_pin=setting.MOTOR_PIN_3)


    def spin_response(self):
        print("Girando ruleta...")
        self.motor1.start_spin()
        self.motor2.start_spin()
        self.motor3.start_spin()

        time.sleep(2)

        self.motor1.stop_spin()
        self.motor2.stop_spin()
        self.motor3.stop_spin()

        prize_detector = PrizeDetection([
            self.motor1.get_position(),
            self.motor2.get_position(),
            self.motor3.get_position()
        ])

        self.motor1.turn_initial_position()
        self.motor2.turn_initial_position() 
        self.motor3.turn_initial_position()

        if (prize_detector.check_winner() > 0):
            buzzer = BuzzerControl(buzzer_pin=setting.BUZZER_PIN)
            buzzer.play_win_sound()

        return prize_detector.check_winner()
