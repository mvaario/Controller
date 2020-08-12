# Script to use controller inputs as mouse and keyboard

from settings import *
import pygame as pg
import win32api, win32con
from pynput.keyboard import Key, Controller
import time

class controller:
    def __init__(self):
        self.joy_id = joy_id

        # Velocyty
        self.vel_x = 0
        self.vel_y = 0
        # Speed
        self.x = 0
        self.y = 0

        # precision
        self.sens = sens

        # Hold
        self.left_click = 0
        self.right_click = 0

    def precision(self):
        right = float(pg.joystick.Joystick(self.joy_id).get_axis(r_r))
        left = float(pg.joystick.Joystick(self.joy_id).get_axis(l_r))

        right = right + 1
        left = -left - 1
        pre = left + right
        pre = pre * multiplier
        self.sens = sens + pre
        if self.sens < 0.5:
            self.sens = 0.5

        return

    def r_axis(self):
        # x-axis
        x = float(pg.joystick.Joystick(self.joy_id).get_axis(1))
        x1 = round(x * 10, 2) * 1.77778

        print(x)
        self.x = self.x + x1
        if abs(self.x) > self.sens:
            if self.x > self.sens:
                self.x = self.sens
            elif self.x < -self.sens:
                self.x = -self.sens

        self.x = self.x * abs(x) + cal_x
        if -0.03 <= self.x <= 0.03:
            self.x = 0

        # y-axis
        y = float(pg.joystick.Joystick(self.joy_id).get_axis(axis_y))
        y1 = round(y * 10, 2)

        self.y = self.y + y1
        if abs(self.y) > self.sens:
            if self.y > self.sens:
                self.y = self.sens
            elif self.y < -self.sens:
                self.y = -self.sens

        self.y = self.y * abs(y) + cal_y
        if -0.005 < self.y < 0.005:
            self.y = 0

        x_p, y_p = win32api.GetCursorPos()
        x = x_p + self.x
        x = int(x)

        y = y_p + self.y
        y = int(y)

        win32api.SetCursorPos((x, y))
        return x, y

    def l_axis(self):
        x = float(pg.joystick.Joystick(self.joy_id).get_axis(left_x))
        y = float(pg.joystick.Joystick(self.joy_id).get_axis(left_y))
        if x > .5:
            keyboard.press(s_right)
            keyboard.release(s_left)
        elif x < -.5:
            keyboard.press(s_left)
            keyboard.release(s_right)
        else:
            keyboard.release(s_right)
            keyboard.release(s_left)
        if y > .5:
            keyboard.press(s_down)
            keyboard.release(s_up)
        elif y < -.5:
            keyboard.press(s_up)
            keyboard.release(s_down)
        else:
            keyboard.release(s_down)
            keyboard.release(s_up)

        return

    def buttons(self):
        # Xbox controller buttons
        a = pg.joystick.Joystick(self.joy_id).get_button(0)
        b = pg.joystick.Joystick(self.joy_id).get_button(1)
        x = pg.joystick.Joystick(self.joy_id).get_button(2)
        y = pg.joystick.Joystick(self.joy_id).get_button(3)

        # Bumbers
        r_b = pg.joystick.Joystick(self.joy_id).get_button(5)
        l_b = pg.joystick.Joystick(self.joy_id).get_button(4)

        # Stick buttons
        r_sb = pg.joystick.Joystick(self.joy_id).get_button(9)
        l_sb = pg.joystick.Joystick(self.joy_id).get_button(8)

        # start / back
        start = pg.joystick.Joystick(self.joy_id).get_button(7)
        back = pg.joystick.Joystick(self.joy_id).get_button(6)

        buttons = a, b, x, y, r_b, l_b, r_sb, l_sb, start, back

        if any(buttons) != 0:
            print(buttons)


        return buttons

    def keyboard(self, buttons):
        if any(t > 0 for t in buttons):
            # Buttons
            if buttons[0] == 1:
                keyboard.press(a)
            if buttons[1] == 1:
                keyboard.press(b)
            if buttons[2] == 1:
                keyboard.press(x)
            if buttons[3] == 1:
                keyboard.press(y)

            # Stick buttons
            if buttons[6] == 1:
                keyboard.press(l_sb)
            if buttons[7] == 1:
                keyboard.press(l_sb)

            # Start and back
            if buttons[8] == 1:
                keyboard.press(start)
            if buttons[9] == 1:
                keyboard.press(back)

            time.sleep(0.1)

        if buttons[8] == 1 and buttons[9] == 1:
            running = False
        else:
            running = True



        # Bumbers / Mouse click
        # Left Click
        if buttons[4] == 1:
            if self.left_click == 0:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                self.left_click = 1
        elif self.left_click == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            self.left_click = 0

        # Right Click
        if buttons[5] == 1:
            if self.right_click == 0:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
                self.right_click = 1
        elif self.right_click == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
            self.right_click = 0

        return running

    def d_pad(self):
        d_pad = pg.joystick.Joystick(self.joy_id).get_hat(0)
        if any(t != 0 for t in d_pad):
            if d_pad[0] == 1:
                keyboard.press(right)
            else:
                keyboard.release(right)
            if d_pad[0] == -1:
                keyboard.press(left)
            else:
                keyboard.release(left)
            if d_pad[1] == 1:
                keyboard.press(up)
            else:
                keyboard.release(up)
            if d_pad[1] == -1:
                keyboard.press(down)
            else:
                keyboard.release(down)

            time.sleep(.1)

        else:
            keyboard.release(up)
            keyboard.release(down)
            keyboard.release(right)
            keyboard.release(left)
        return

    def release(self, buttons):
        # Buttons
        if buttons[0] == 1:
            keyboard.release(a)
        if buttons[1] == 1:
            keyboard.release(b)
        if buttons[2] == 1:
            keyboard.release(x)
        if buttons[3] == 1:
            keyboard.release(y)

        # Stick buttons
        if buttons[6] == 1:
            keyboard.release(l_sb)
        if buttons[7] == 1:
            keyboard.release(l_sb)

        # Start and back
        if buttons[8] == 1:
            keyboard.release(start)
        if buttons[9] == 1:
            keyboard.release(back)
        return


if __name__ == '__main__':
    clock = pg.time.Clock()
    keyboard = Controller()
    controller = controller()



    print("")
    print("Using controller to send mouse and keyboard inputs")
    running = settings.controller_check(controller)
    if running:
        print("press start and back to quit")

    while running:
    # for i in range(1000):
        pg.event.pump()

        # controller.precision()
        controller.r_axis()

        # controller.l_axis()

        # Buttons
        # buttons = controller.buttons()
        # running = controller.keyboard(buttons)
        # controller.release(buttons)

        # D_pad
        controller.d_pad()

        clock.tick(FPS)

    print("")
    print("Program closed")
    input("Press enter to close")