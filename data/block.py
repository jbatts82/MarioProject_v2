###############################################################################
# File Name  : block.py
# Date       : 1/14/2022
# Description:
###############################################################################

import pygame
import data.constants as const
from communityChest.spriteSheet import SpriteSheet


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()
        sprite_tool = SpriteSheet(self.sprite_sheet)
        self.image1 = []
        self.image1.append(sprite_tool.extract_image(373, 142, 16, 16))
        self.image = self.image1[0]
        self.image.set_colorkey(const.UNUSED_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
