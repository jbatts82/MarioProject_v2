###############################################################################
# File Name  : debug_sprite_viewer.py
# Description: Visual sprite verification tool - run this to check frames
###############################################################################

import pygame
import data.constants as const
from communityChest.spriteSheet import SpriteSheet

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Sprite Viewer - Close window to exit')
clock = pygame.time.Clock()
font = pygame.font.SysFont('consolas', 13)

sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()
tool = SpriteSheet(sheet)

frames = [
    ('stand',  tool.extract_image(23,  507, 13, 16)),
    ('walk1',  tool.extract_image(85,  507, 12, 16)),
    ('walk2',  tool.extract_image(100, 507, 14, 16)),
    ('walk3',  tool.extract_image(117, 507, 16, 16)),
    ('jump',   tool.extract_image(139, 507, 17, 16)),
]
left_frames = [(f'L-{n}', pygame.transform.flip(img, True, False)) for n, img in frames]
all_frames = frames + left_frames

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((100, 149, 237))  # sky blue

    label = font.render('Mario Sprite Frames  (ESC to close)', True, (255, 255, 255))
    screen.blit(label, (10, 10))

    cols = 5
    cell_w = 90
    cell_h = 110
    for i, (name, img) in enumerate(all_frames):
        col = i % cols
        row = i // cols
        x = 10 + col * cell_w
        y = 40 + row * cell_h
        pygame.draw.rect(screen, (50, 50, 80), (x - 2, y - 2, img.get_width() + 4, img.get_height() + 4))
        screen.blit(img, (x, y))
        for j, line in enumerate(name.split('\n')):
            lbl = font.render(line, True, (255, 255, 0))
            screen.blit(lbl, (x, y + img.get_height() + 4 + j * 14))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
