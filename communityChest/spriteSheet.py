###############################################################################
# File Name  : spriteSheet.py
# Date       : 11/12/2022
# Description: Sprite Sheet Class
###############################################################################

import pygame
import data.constants as const


class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def extract_image(self, x_pos, y_pos, width, height):
        image = pygame.Surface([width, height])
        rect = image.get_rect()
        image.blit(self.sheet, (0, 0), (x_pos, y_pos, width, height))
        image.set_colorkey(const.BLACK)
        image = pygame.transform.scale(image,
                                       (int(rect.width * const.SIZE_MULTIPLIER),
                                        int(rect.height * const.SIZE_MULTIPLIER)))
        return image
