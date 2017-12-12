import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import map3


name = "map2 state"

mouse = None
background = None
font = None

drawstart = None

class Background:
    def __init__(self):
        self.background_image = load_image('background.png')
        self.start_image = load_image('Start.png')
        self.x = 1

    def draw(self):
        self.background_image.draw(400, 300)
        if drawstart == 0:
            self.start_image.draw(130, 130)
            self.draw_bb()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    #def resetdrawbb(self):
    #    self.drawbb = 0

    def get_bb(self):
        return 80, 110, 180, 150

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
        global drawstart
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, 600 - event.y
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.x, self.y = event.x, 600 - event.y
            if self.x > 80 and self.x < 180 and self.y > 110 and self.y < 180:
                drawstart = 1


    def setpos(self):
        SDL_WarpMouseInWindow(None, 145, 470)

class vertical_bar:
    def __init__(self,x,y, incre, end):
        self.x, self.y = x, y
        self.incre = incre
        self.end = end
        self.image = load_image('bar_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x , self.y - self.incre)
        self.image.draw(self.x, self.y + self.end)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 50 - self.incre, self.x + 10, self.y + 50 + self.end

class horizontal_bar:
    def __init__(self, x, xend, incre, y):
        self.x, self.y, = x,y
        self.incre = incre
        self.xend = self.x + xend
        self.image = load_image('bar_2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + self.incre, self.y)
        self.image.draw(self.xend, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 10, self.xend + 50, self.y + 10

class Obstacle:
    def __init__(self, x, y, type):
        self.x, self.y = x, y
        self.minx, self.maxx = x - 100 , x + 100
        self.image = load_image('obstacle.png')
        self.type = type

    def update(self):
        if self.type == 0:
            self.x += 1
            if self.x > self.maxx:
                self.type = 1
        elif self.type == 1:
            self.x -= 1
            if self.x < self.minx:
                self.type = 0
    def draw(self):
        self.image.draw(self.x , self.y)
        #self.image.draw(self.x + 200, self.y + 120)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 21, self.y - 71, self.x + 19, self.y + 71


def enter():
    global mouse, background, end, bar_1, bar_2, bar_3, bar_4, bar_5, bar_6, bar_7, bar_8, bar_9, bar_10, bar_11, bar_12, obstacle, obstacle2
    global drawstart
    drawstart = 0
    mouse = Mouse()
    end = End()
    background = Background()
    # 아래쪽 가로
    bar_1 = horizontal_bar(110, 120, 90, 310)
    bar_2 = horizontal_bar(400, 450, 100, 200)
    bar_3 = horizontal_bar(600, 450, 100, 300)
    # 위쪽 가로
    bar_4 = horizontal_bar(110, 190, 90, 100)
    bar_5 = horizontal_bar(330, 100, 10, 410)
    bar_6 = horizontal_bar(510, 190, 90, 520)
    # 위쪽 세로
    bar_7 = vertical_bar(70, 170, 10, 100)
    bar_8 = vertical_bar(280, 360, 10, 10)
    bar_9 = vertical_bar(470, 470, 20, 10)
    bar_10 = vertical_bar(740, 370, 10, 100)
    # 위쪽 아래
    bar_11 = vertical_bar(340, 150, 10, 10)
    bar_12 = vertical_bar(550, 250, 10, 10)

    obstacle = Obstacle(400,300, 0)
    obstacle2 = Obstacle(600,420, 1)
    mouse.setpos()

def exit():
    global mouse, background, end, bar_1, bar_2, obstacle, obstacle2
    del(mouse)
    del(background)
    del(end)
    del(bar_1)
    del(bar_2)
    del(obstacle)
    del (obstacle2)


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_framework.push_state(map3)
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
    global  end, bar_1, bar_2, obstacle,  obstacle2, mouse
    #mouse.update()
    if drawstart == 1:
        obstacle.update()
        obstacle2.update()
    update_canvas()

    if drawstart == 1:
        if collide(end, mouse):
            game_framework.push_state(map3)
        if collide(obstacle, mouse):
            mouse.setpos()
        if collide( obstacle2, mouse):
            mouse.setpos()
    if collide(bar_1, mouse):
        mouse.setpos()
    if collide(bar_2, mouse):
        mouse.setpos()
    if collide(bar_3, mouse):
        mouse.setpos()
    if collide(bar_4, mouse):
        mouse.setpos()
    if collide(bar_5, mouse):
        mouse.setpos()
    if collide(bar_6, mouse):
        mouse.setpos()
    if collide(bar_7, mouse):
        mouse.setpos()
    if collide(bar_8, mouse):
        mouse.setpos()
    if collide(bar_9, mouse):
         mouse.setpos()
    if collide(bar_10, mouse):
        mouse.setpos()
    if collide(bar_11, mouse):
        mouse.setpos()
    if collide(bar_12, mouse):
        mouse.setpos()


def draw_main_scene():
    background.draw()
    end.draw()
    mouse.draw()
    bar_1.draw()
    bar_3.draw()
    bar_2.draw()
    bar_4.draw()
    bar_5.draw()
    bar_6.draw()
    bar_7.draw()
    bar_8.draw()
    bar_9.draw()
    bar_10.draw()
    bar_11.draw()
    bar_12.draw()
    if drawstart == 1:
        obstacle.draw()
        obstacle2.draw()

    #bar_1.draw_bb()
    #bar_2.draw_bb()
    end.draw_bb()
    #mouse.draw_bb()


def draw():
    hide_cursor()
    clear_canvas()
    draw_main_scene()
    update_canvas()






