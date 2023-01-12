import RPi.GPIO as GPIO
from mygpio import mygpio
import time
from BOARD import DFRobot_Expansion_Board_IIC as Board
from pynput.keyboard import Key, Listener

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

board = Board(1, 0x10)

s = board.detecte()
print("Board list conform:")
print(s)
while board.begin() != board.STA_OK:
    print("board begin failed!")
    time.sleep(2)
print("board begin success!")
board.set_pwm_enable()                # Pwm channel need external power
# board.set_pwm_disable()
board.set_pwm_frequency(1000)
board.set_pwm_duty(0, 0)
board.set_pwm_duty(1, 0)
board.set_pwm_duty(2, 0)
board.set_pwm_duty(3, 0)

def on_press(key):
    # 当按下esc，结束监听
    if key == Key.esc:
        print(f"你按下了esc，监听结束")
        g.stop()
        return False
    if key==key.up:
        print("forward---^")
        board.set_pwm_duty(0, 60)
        board.set_pwm_duty(1, 60)
        board.set_pwm_duty(2, 60)
        board.set_pwm_duty(3, 60)
        g.forward()
    elif key == key.down:
        print("backup---V")
        board.set_pwm_duty(0, 60)
        board.set_pwm_duty(1, 60)
        board.set_pwm_duty(2, 60)
        board.set_pwm_duty(3, 60)
        g.backup()
    elif key == key.left:
        print("left<---")
        board.set_pwm_duty(0, 60)
        board.set_pwm_duty(1, 60)
        board.set_pwm_duty(2, 60)
        board.set_pwm_duty(3, 60)
        g.left()
    elif key == key.right:
        print("right--->")
        board.set_pwm_duty(0, 60)
        board.set_pwm_duty(1, 60)
        board.set_pwm_duty(2, 60)
        board.set_pwm_duty(3, 60)
        g.right()
    elif key == key.left:
        print("left<---")
        board.set_pwm_duty(0, 60)
        board.set_pwm_duty(1, 60)
        board.set_pwm_duty(2, 60)
        board.set_pwm_duty(3, 60)
        g.left()
    elif key == key.page_up:
        print("r_rotate<---")
        board.set_pwm_duty(0, 60)
        board.set_pwm_duty(1, 60)
        board.set_pwm_duty(2, 60)
        board.set_pwm_duty(3, 60)
        g.r_rotate()
    elif key == key.page_down:
        print("l_lotate<---")
        board.set_pwm_duty(0, 60)
        board.set_pwm_duty(1, 60)
        board.set_pwm_duty(2, 60)
        board.set_pwm_duty(3, 60)
        g.l_rotate()
    print(f"你按下了{key}键")


def on_release(key):
    board.set_pwm_duty(0, 0)
    board.set_pwm_duty(1, 0)
    board.set_pwm_duty(2, 0)
    board.set_pwm_duty(3, 0)
    print(f"你松开了{key}键")

g = mygpio()

if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
        



