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
        self.start_image.draw(130, 130)

    def update(self):
        pass

class End:
    def __init__(self):
        self.x, self.y = 700, 480
        self.end_image = load_image('End.png')
    def draw(self):
        self.end_image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y-20, self.x + 30, self.y + 20


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

class Bar_1:
    def __init__(self):
        self.x, self.y = 70, 170
        self.image = load_image('bar_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x , self.y - 10)
        self.image.draw(self.x, self.y + 100)
        self.image.draw(self.x + 290, self.y - 30)
        self.image.draw(self.x + 200, self.y + 200)
        self.image.draw(self.x + 470, self.y + 90)
        self.image.draw(self.x + 400, self.y + 300)
        self.image.draw(self.x + 670, self.y + 190)
        self.image.draw(self.x + 670, self.y + 290)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 50, self.x + 10, self.y + 50

class Bar_2:
    def __init__(self):
        self.x, self.y = 200, 100
        self.image = load_image('bar_2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - 90, self.y)
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + 100, self.y)
        self.image.draw(self.x - 70, self.y + 210 )
        self.image.draw(self.x +30 , self.y + 210 )
        self.image.draw(self.x + 200, self.y + 100)
        self.image.draw(self.x + 300, self.y + 100)
        self.image.draw(self.x + 130, self.y + 310)
        self.image.draw(self.x + 230, self.y + 310)
        self.image.draw(self.x + 400, self.y + 200)
        self.image.draw(self.x + 500, self.y + 200)
        self.image.draw(self.x + 330, self.y + 410)
        self.image.draw(self.x + 430, self.y + 410)
        self.image.draw(self.x + 500, self.y + 410)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 10, self.x + 50, self.y + 10

class Obstacle:

    def __init__(self):
        self.x, self.y = 400, 300
        self.image = load_image('obstacle.png')
        self.type = 0

    def update(self):
        if self.type == 0:
            self.x += 1
            if self.x >500:
                self.type = 1
        elif self.type == 1:
            self.x -= 1
            if self.x < 300:
                self.type = 0





    def draw(self):
        self.image.draw(self.x , self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 21, self.y - 71, self.x + 19, self.y + 71


def enter():
    global mouse, background, end, bar_1, bar_2, obstacle
    mouse = Mouse()
    end = End()
    background = Background()
    bar_1 = Bar_1()
    bar_2 = Bar_2()
    obstacle = Obstacle()

def exit():
    global mouse, background, end, bar_1, bar_2, obstacle
    del(mouse)
    del(background)
    del(end)
    del(bar_1)
    del(bar_2)
    del(obstacle)


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
    global  end, bar_1, bar_2, obstacle
    #mouse.update()
    obstacle.update()
    update_canvas()


    if collide(end, mouse):
        end.stop(0)
    if collide(obstacle, mouse):
        obstacle.stop(0)
    #elif collide(bar, end):
       # bar.stop(0)


def draw_main_scene():
    background.draw()
    end.draw()
    mouse.draw()
    bar_1.draw()
    bar_2.draw()
    obstacle.draw()

    #bar_1.draw_bb()
    #bar_2.draw_bb()
    end.draw_bb()
    mouse.draw_bb()
    obstacle.draw_bb()

def draw():
    hide_cursor()
    clear_canvas()
    draw_main_scene()
    update_canvas()






