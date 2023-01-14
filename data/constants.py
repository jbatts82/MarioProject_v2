###############################################################################
# File Name  : constants.py
# Date       : 12/17/2022
# Description: Game constants
###############################################################################

# screen constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
MAIN_CAPTION = 'Mario Project v2'
FPS = 60

# controller configs
CONFIG_1 = 0
CONFIG_2 = 1
NES_1 = 0


# sprite locations
MARIO_SPRITE_SHEET_LOC = 'resources/graphics/mario_bros.png'
BACKGROUND_PNG_LOC = 'resources/graphics/level_1.png'
MISC3_LOC = 'resources/graphics/misc-3.gif'

# sprite attributes
SIZE_MULTIPLIER = 4
ANIMATION_COOLDOWN = 150

# mario states
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
GETTING_BIGGER = 'small to big'
GETTING_SMALLER = 'big to small'
DEATH_JUMP = 'death jump'

# hex colors codes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
UNUSED_COLOR = (255, 0, 255)

# camera
# borders within
# SCREEN_WIDTH and SCREEN_HEIGHT
CAMERA_BORDERS = {
    'left': 100,
    'right': 200,
    'top': 100,
    'bottom': 150
}

TILE_SIZE = 64
# x = column index * width
# y = row index * height
LEVEL_MAP = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X       M                              X',
    'X                                     X',
    'X                                     X',
    'X                                     X',
    'X                                     X',
    'X                                     X',
    'X                                     X',
    'X                                     X',
    'X  G    X                             X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


