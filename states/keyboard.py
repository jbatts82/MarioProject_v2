###############################################################################
# File Name  : keyboard.py
# Date       : 12/23/2022
# Description: Input from keyboard
###############################################################################

import pygame


config1_keybindings = {
    'action': pygame.K_n,
    'jump': pygame.K_m,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'down': pygame.K_DOWN,
    'up': pygame.K_UP
}

config2_keybindings = {
    'action': pygame.K_g,
    'jump': pygame.K_h,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'down': pygame.K_s,
    'up': pygame.K_w
}


class Keyboard:
    def __init__(self, config=0):
        self.configuration = None
        if config == 0:
            self.configuration = config1_keybindings
            print("action button: " + str(self.configuration['action']))
        elif config == 1:
            self.configuration = config2_keybindings

    def get_configuration(self):
        return self.configuration
