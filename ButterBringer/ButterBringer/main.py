#!/usr/bin/env pybricks-micropython
from ev3dev.ev3 import *
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, LargeMotor, MediumMotor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#Program writing for testing
touchSens1 = TouchSensor(Port.S1)
touchSens2 = TouchSensor(Port.S2)
colourBlindBoi = ColorSensor(Port.S3)
sonic = UltrasonicSensor(Port.S4)
mediumBoi = MediumMotor(Port.A)
bigBoi1 = LargeMotor(Port.B)
bigBoi2 = LargeMotor(Port.C)

Sound.tone(1500, 2000)

while (touchSens1.value() == 1) or (touchSens2.value() == 1):
    bigBoi1.run_forever(speed_sp = 20)
    bigBoi2.run_forever(speed_sp = 20)
    mediumBoi.run_forever(speed_sp = 20)

bigBoi1.stop(stop_action='brake')
bigBoi2.stop(stop_action='brake')
mediumBoi.stop(stop_action='brake')

