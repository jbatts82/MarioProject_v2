###############################################################################
# File Name  : joystick.py
# Date       : 12/23/2022
# Description: Input from nes style joystick
###############################################################################

import pygame.joystick
pygame.joystick.init()

nes_controller_keybindings = {
    'action': 2,
    'jump': 1,
    'x_axis': 0,
    'y_axis': 4,
    'start': 9,
    'select': 8
}


class JoyStick:
    def __init__(self, config=0, name='JoyStick_object'):
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        print(self.joysticks)
        self.configuration = None
        if config == 0:
            self.configuration = nes_controller_keybindings

    def handle_button(self, buttons):
        if pygame.joystick.Joystick(0).get_button(self.configuration['jump']):
            print("Pressed Button A")
        if pygame.joystick.Joystick(0).get_button(self.configuration['action']):
            print("Pressed Button B")
        if pygame.joystick.Joystick(0).get_button(self.configuration['start']):
            print("Pressed Button Start")
        if pygame.joystick.Joystick(0).get_button(self.configuration['select']):
            print("Pressed Button Select")

    def get_configuration(self):
        return self.configuration

    def handle_d_pad():
        x_speed = round(pygame.joystick.Joystick(0).get_axis(0))
        y_speed = round(pygame.joystick.Joystick(0).get_axis(4))
