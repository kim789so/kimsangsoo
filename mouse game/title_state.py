import game_framework
from pico2d import *
import main_state


name = "TitleState"
image = None

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
            global image
            global mouse
            self.x, self.y = event.x, 600 - event.y
            # start
            if self.x > 340 and self.x < 470 and self.y > 195 and self.y < 240:
                image = load_image('start-check.png')
                draw()
            # ranking
            elif self.x > 310 and self.x < 500 and self.y > 130 and self.y < 185:
                image = load_image('ranking-check.png')
                draw()
            # exit
            elif self.x > 350 and self.x < 450 and self.y > 75 and self.y < 120:
                image = load_image('exit-check.png')
                draw()
            else:
                image = load_image('main.png')
                draw()
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.x, self.y = event.x, 600 - event.y
            # start
            if self.x > 340 and self.x < 470 and self.y > 195 and self.y < 240:
                game_framework.change_state(main_state)
            # ranking
            elif self.x > 310 and self.x < 500 and self.y > 130 and self.y < 185:
                #image = load_image('ranking-check.png')
                draw()
            # exit
            elif self.x > 350 and self.x < 450 and self.y > 75 and self.y < 120:
                game_framework.quit()


def enter():
    global image
    global mouse
    mouse = Mouse()
    image = load_image('main.png')

def start():
    global image
    image = load_image('start.png')

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
        else :
            mouse.handle_events(event)


def draw():
    clear_canvas()
    image.draw(400, 300)
    hide_cursor()
    mouse.draw()
    mouse.draw_bb()
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






