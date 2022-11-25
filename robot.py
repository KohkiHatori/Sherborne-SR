from sr.robot3 import *


#distance = R.ruggeduino.pins[A5].analogue_read()
#print(f"Rear ultrasound distance: {distance} meters")

def init():
    R = Robot()
    return R


def halt(R):
    change_motor_power(R, (0,0))

def change_motor_power(R, powers: tuple):
    R.motor_board.motors[0].power = powers[0]
    R.motor_board.motors[1].power = powers[1]

def move(R, duration):
    R.sleep(duration)

def main():
    R = init()
    change_motor_power(R, (1, 1))
    move(R, 1)
    change_motor_power(R, (1, 0))
    move(R, 1)
    change_motor_power(R, (0, 1))
    move(R, 1)
    change_motor_power(R, (-1, -1))
    move(R, 1)
    change_motor_power(R, (-1, 0))
    move(R, 1)
    change_motor_power(R, (0, -1))
    move(R, 1)
    halt(R)

main()
