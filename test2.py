import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print(joystick_count)

joystick = pygame.joystick.Joystick(0)
joystick.init()

name = joystick.get_name()
print(name)

while True:

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    name = joystick.get_name()
    # print(name)
    axes = joystick.get_numaxes()
    for i in range(axes):
        axis = joystick.get_axis(i)
        if axis != 0:
            print(i, axis)