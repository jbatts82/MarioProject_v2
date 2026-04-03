###############################################################################
# File Name  : mario.py
# Date       : 4/2/2026
# Description: Mario player class
###############################################################################

import pygame
import data.constants as const
from communityChest.spriteSheet import SpriteSheet


class Mario(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)

        # sprite setup
        sprite_sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()
        sprite_tool = SpriteSheet(sprite_sheet)

        self.right_standing = sprite_tool.extract_image(23, 507, 13, 16)
        self.left_standing = pygame.transform.flip(self.right_standing, True, False)

        self.right_jump = sprite_tool.extract_image(139, 507, 17, 16)
        self.left_jump = pygame.transform.flip(self.right_jump, True, False)

        self.right_walk_frames = [
            sprite_tool.extract_image(85,  507, 12, 16),
            sprite_tool.extract_image(100, 507, 14, 16),
            sprite_tool.extract_image(117, 507, 16, 16),
        ]
        self.left_walk_frames = [pygame.transform.flip(f, True, False) for f in self.right_walk_frames]

        self.image = self.right_standing
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.old_rect = self.rect.copy()

        # physics
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = const.MARIO_SPEED
        self.gravity = const.GRAVITY
        self.jump_vel = const.JUMP_VEL
        self.on_floor = False

        self.collision_sprites = collision_sprites

        # animation
        self.frame_idx = 0
        self.last_update = pygame.time.get_ticks()
        self.facing_right = True
        self.state = const.STAND

    def get_input(self, keys):
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
            if self.on_floor:
                self.state = const.WALK
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
            if self.on_floor:
                self.state = const.WALK
        else:
            self.direction.x = 0
            if self.on_floor:
                self.state = const.STAND

        if keys[pygame.K_m] and self.on_floor:
            self.direction.y = self.jump_vel
            self.on_floor = False
            self.state = const.JUMP

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                    self.pos.x = self.rect.x
                elif self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x

    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if self.state == const.STAND:
            self.image = self.right_standing if self.facing_right else self.left_standing
        elif self.state == const.WALK:
            if current_time - self.last_update >= const.ANIMATION_COOLDOWN:
                self.frame_idx = (self.frame_idx + 1) % len(self.right_walk_frames)
                self.last_update = current_time
            frames = self.right_walk_frames if self.facing_right else self.left_walk_frames
            self.image = frames[self.frame_idx]
        elif self.state in (const.JUMP, const.FALL):
            self.image = self.right_jump if self.facing_right else self.left_jump

    def update(self, keys):
        self.get_input(keys)

        # horizontal
        self.pos.x += self.direction.x * self.speed
        self.rect.x = round(self.pos.x)
        self.horizontal_collisions()

        # vertical
        self.apply_gravity()
        self.vertical_collisions()

        self.update_animation()
