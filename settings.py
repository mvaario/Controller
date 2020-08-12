# User settings

import pygame as pg
from pynput.keyboard import Key, Controller

keyboard = Controller()

# FPS limit
FPS = 30

# Random calibration
cal_x = 0.04
cal_y = 0

# Controller number
joy_id = 0

# Sensitivity
sens = 30

# Axis numbers
axis_x = 5
axis_y = 4
left_x = 0
left_y = 1

# Left Stick keys
s_up = 'w'
s_down = 's'
s_right = 'd'
s_left = 'a'

# triggers
r_r = 3
l_r = 2
multiplier = 9

# button configs
a = 'f'
b = '1'
x = 'q'
y = '2'

r_sb = 'a'
l_sb = 's'

start = Key.esc
back = 'm'

# d_pad
up = 'w'
down = 's'
left = 'a'
right = 'd'



class settings:
    def controller_check(self):
        try:
            pg.display.init()
            pg.joystick.init()
            pg.joystick.Joystick(self.joy_id).init()

            # Prints the joystick's name
            name = pg.joystick.Joystick(self.joy_id).get_name()
            print("")
            print("Controller name:", name)
            running = True
            return running

        except:

            print("No controller found with number:", self.joy_id)
            i = int(input("Change controller number to: "))
            if i < 10:
                self.joy_id = i
                running = settings.controller_check(self)
            else:
                print("Error")
                quit()

        return running