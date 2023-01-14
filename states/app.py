###############################################################################
# File Name  : app.py
# Date       : 12/17/2022
# Description: top level of system
###############################################################################

import pygame
import random
import data.constants as const
import states.joystick
import states.keyboard
from states.level import Level



class GameManager:
    def __init__(self):
        print("main_init")
        self.run_game = True
        pygame.init()
        # init game_objects
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        pygame.display.set_caption(const.MAIN_CAPTION)
        self.keys = None
        keyboard1 = states.keyboard.Keyboard(0)
        keyboard2 = states.keyboard.Keyboard(1)
        random.seed()
        self.level = Level()


    def main_loop(self):
        print("main_loop")
        while self.run_game:
            self.process_events()
            self.screen.fill(const.BLUE)
            self.level.run()
            pygame.display.flip()
            self.clock.tick(const.FPS)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False
            if event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP:
                self.keys = pygame.key.get_pressed()
