import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state



name = "MainState"

boy = None
grass = None
block = None
font = None


#배경
class Grass:
    def __init__(self):
        self.image = load_image('main_stage.png')

    def draw(self):
        #좌표를 => 400,300
        self.image.draw(400, 300)


# 캐릭터(블럭)
class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

# ㅜ
class Block:
    def __init__(self):
        self.x, self.y = 400, 560
        self.image = None
        self.dir = 0  # 기본상태 방향
        self.fall_speed = 30

    def draw(self):
        if(self.dir == 0):                   #처음상태
            self.image = load_image('qwe.png')
            self.image.draw(self.x,self.y)
        elif(self.dir == 1):                 #한번 돌렸을 때
            self.image= load_image('qwe.png')
            self.image.draw(self.x, self.y)
        elif(self.dir == 2):                 #두번 돌렸을 때
            self.image = load_image('qwe.png')
            self.image.draw(self.x, self.y)
        elif(self.dir == 3):                 #세번 돌렸을 때
            self.image = load_image('qwe.png')
            self.image.draw(self.x, self.y)

    def rotate(self):
        print('rotate')
        self.dir +=1
        if (self.dir > 3):
            self.dir = 0

    #블럭 떨어지는 속도?
    def update(self):
        self.y -= 0.3  #속도
        self.y = max(40,self.y)

    def handel_events(self,event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #print('space')
            self.rotate()
            #self.dir += 1
            #if(self.dir > 3):
            #    self.dir = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.x -= 5


#ㄴ
class Block2:
    pass

#ㅡ
class Block3:
    pass

#ㅁ
class Block4:
    pass


#
##

def enter():
    global boy, grass, block
    boy = Boy()
    grass = Grass()
    block = Block()


def exit():
    global boy, grass,block
    del(boy)
    del(grass)
    del(block)


def pause():
    pass


def resume():
    pass


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            block.handel_events(event)



def update():
    boy.update()
    block.update()
    update_canvas()


def draw_main_scene():
    grass.draw()
    boy.draw()
    block.draw()



def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()






