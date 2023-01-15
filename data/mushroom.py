###############################################################################
# File Name  : mushroom.py
# Date       : 1/14/2022
# Description:
###############################################################################

import pygame
import data.constants as const
from communityChest.spriteSheet import SpriteSheet


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()
        sprite_tool = SpriteSheet(self.sprite_sheet)
        self.image1 = []
        self.image1.append(sprite_tool.extract_image(52, 43, 16, 16))
        self.image = self.image1[0]
        self.image.set_colorkey(const.BLACK)

        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.old_rect = self.rect.copy()

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.gravity = 0.8
        self.direction.y = self.gravity
        self.direction.x = 1
        self.collision_sprites = collision_sprites
        self.on_floor = False

    def update(self):
        # x-axis movements
        self.pos.x += self.direction.x * self.speed
        self.rect.x = round(self.pos.x)
        self.horizontal_collisions()

        # y-axis movements
        self.apply_gravity()
        self.vertical_collisions()

    # Collision Notes
    # 1.) The player needs to know where the obstacles are
    # 2.) We need to implement the collision mechanic
    # 3.) Combine the move and collisions methods
    def horizontal_collisions(self):
        self.old_rect = self.rect.copy()
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                print(self.direction.x)
                print(self.pos)
                if self.direction.x > 0:  # moving right
                    # bump left side of mushroom
                    self.rect.right = sprite.rect.left
                    self.pos.x = self.rect.x
                    self.direction.x *= -1
                    print(self.direction.x)
                    print('right side collision')
                elif self.direction.x < 0:  # moving left
                    # bump right side of mushroom
                    self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x
                    self.direction.x *= -1
                    print('left side collision')



    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
