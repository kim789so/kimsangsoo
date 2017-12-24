import game_framework
import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

from pico2d import *

# fill state here
import start_state
import main_state
import pause_state



#open_canvas()
game_framework.run(start_state)
#game_framework.run(main_state)
#game_framework.run(pause_state)

#close_canvas()