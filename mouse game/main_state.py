import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state



name = "MainState"

mouse = None
background = None
font = None


class Background:
    def __init__(self):
        self.background_image = load_image('background.png')
        self.start_image = load_image('Start.png')

    def draw(self):
        self.background_image.draw(400, 300)
        self.start_image.draw(100, 100)

    def update(self):
        pass

class End:
    def __init__(self):
        self.x, self.y = 700, 500
        self.end_image = load_image('End.png')
    def draw(self):
        self.end_image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y-30, self.x + 40, self.y + 30


class Mouse:
    def __init__(self):
        self.x, self.y = 100, 100
        self.image = load_image('mouse.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def handle_events(self,event):
        events = get_events()
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, 600 - event.y




def enter():
    global mouse, background, end
    mouse = Mouse()
    end = End()
    background = Background()


def exit():
    global mouse, background, end
    del(mouse)
    del(background)
    del(end)


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global  Mouse

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else :
            mouse.handle_events(event)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True


def update():
    global  endv
    mouse.update()
    update_canvas()

    if collide(end, mouse):
        end.stop(0)


def draw_main_scene():
    background.draw()
    end.draw()
    mouse.draw()

    end.draw_bb()
    mouse.draw_bb()

def draw():
    hide_cursor()
    clear_canvas()
    draw_main_scene()
    update_canvas()






