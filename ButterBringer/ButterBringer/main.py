#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



# Create your objects here.
ev3 = EV3Brick()
touchSens1 = TouchSensor(Port.S1)
touchSens2 = TouchSensor(Port.S2)
colourBlindBoi = ColorSensor(Port.S3)
sonic = UltrasonicSensor(Port.S4)
mediumBoi = Motor(Port.A)
bigBoi1 = Motor(Port.B)
bigBoi2 = Motor(Port.C)

#Program writing for testing
def program():
    while not touchSens1.pressed():
        while not touchSens2.pressed():
            bigBoi1.stop()
            bigBoi2.stop()
            mediumBoi.stop()

        bigBoi1.run(speed = 20)
        bigBoi2.run(speed = 20)
        mediumBoi.run(speed = 20)
    
    ev3.speaker.beep()
program()

