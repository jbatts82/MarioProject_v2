###############################################################################
# File Name  : goomba.py
# Date       : 1/14/2022
# Description:
###############################################################################

import pygame
import data.constants as const
from communityChest.spriteSheet import SpriteSheet


class Goomba(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()
        sprite_tool = SpriteSheet(self.sprite_sheet)

        self.image1 = []
        self.image1.append(sprite_tool.extract_image(187, 894, 16, 16))  # left foot
        self.image1.append(sprite_tool.extract_image(208, 894, 16, 16))  # right root
        self.image1.append(sprite_tool.extract_image(228, 894, 16, 16))  # stomped
        self.image = self.image1[0]
        self.rect = self.image.get_rect(topleft=pos)
