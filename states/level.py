###############################################################################
# File Name  : level.py
# Date       : 1/14/2022
# Description: Level Set up
#              1. Create a level class that contains the game
#               a. Contains the sprite groups, responsible for writing assets
#              2. create a class for the player and the level tiles
#              3. convert the layout to an actual level
###############################################################################

import pygame
import data.constants as const
from data.block import Block


class Level:
    def __init__(self):
        # level set up
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()  # draws anything
        self.active_sprites = pygame.sprite.Group()  # updates anything
        self.collision_sprites = pygame.sprite.Group()  # collidbles

        self.setup_level()

    def setup_level(self):
        for row_index, row in enumerate(const.LEVEL_MAP):
            # print(f'{row_index}:{row}-> {index * TILE_SIZE}')
            for col_index, col in enumerate(row):
                x = col_index * const.TILE_SIZE
                y = row_index * const.TILE_SIZE
                if col == 'X':
                    Block((x, y), [self.visible_sprites, self.collision_sprites])

                # if col == 'P':
                #     self.player = Player((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)
                # if col == 'E':
                #     self.enemy = Enemy((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

    def run(self):
        # run the entire game (level)
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        # self.visible_sprites.custom_draw(self.player)
        # self.visible_sprites.custom_draw(self.enemy)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 300)

        # center camera set up
        # get_size() returns an array, [0] picks off the 0 element
        # self.half_width = self.display_surface.get_size()[0] // 2
        # self.half_height = self.display_surface.get_size()[1] // 2

        cam_left = const.CAMERA_BORDERS['left']
        cam_top = const.CAMERA_BORDERS['top']
        cam_width = self.display_surface.get_size()[0] - (cam_left + const.CAMERA_BORDERS['right'])
        cam_height = self.display_surface.get_size()[1] - (cam_top + const.CAMERA_BORDERS['bottom'])

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)

    def custom_draw(self, player):
        # get the player offset
        # self.offset.x = player.rect.centerx - self.half_width
        # self.offset.y = player.rect.centery - self.half_height

        # getting the camera position
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        # camera offset
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - const.CAMERA_BORDERS['left'],
            self.camera_rect.top - const.CAMERA_BORDERS['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
