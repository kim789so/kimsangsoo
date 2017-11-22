import game_framework
from pico2d import *

import title_state
import main_state

name = "PauseState"
image = None
logo_time = 0.0
counter = 0

def enter():
    global image
    #open_canvas()
    image = load_image('movPause.png')


def exit():
    global image
    del(image)
    #close_canvas()


def update():
    #counter = image delay
    global counter
    counter = (counter + 1) % 100
    pass

def draw():

    global image, counter
    clear_canvas()
    main_state.draw_main_scene()
    if counter < 50:
        image.draw(400,300)
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            #if keydown 'p' return to previous state
            game_framework.pop_state()

    pass


def pause(): pass


def resume(): pass