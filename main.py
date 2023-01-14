###############################################################################
# File Name  : main.py
# Date       : 1/12/2022
# Description: Main Loop - Run from here...
###############################################################################

import sys
import states.app as app

game_manager = app.GameManager()
game_manager.main_loop()
# if game loop breaks
sys.exit()
