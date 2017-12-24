import game_framework
from pico2d import *
import main_state
import title_state
import rank_state

name = "TitleState"
image = None
font = None
rank = None
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
            # exit
            if self.x > 350 and self.x < 450 and self.y > 75 and self.y < 120:
                #image = load_image('exit-check.png')
                draw()
            else:
                image = load_image('background.png')
                draw()
        if event.type == SDL_MOUSEBUTTONDOWN:
            self.x, self.y = event.x, 600 - event.y
            # start
            if self.x > 340 and self.x < 470 and self.y > 195 and self.y < 240:
                game_framework.change_state(main_state)
            # ranking
            elif self.x > 310 and self.x < 500 and self.y > 130 and self.y < 185:
                game_framework.change_state(rank_state)
            # exit
            elif self.x > 350 and self.x < 450 and self.y > 75 and self.y < 120:
                game_framework.quit()


def enter():
    global image
    global mouse
    mouse = Mouse()
    image = load_image('background.png')

def start():
    global image
    image = load_image('background.png')

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
        else :
            mouse.handle_events(event)


def draw():
    global font, rank
    clear_canvas()
    image.draw(400, 300)
    rank = game_framework.get_rank()
    font = load_font('ENCR10B.TTF', 40)
    font.draw(300,550,'[RANKING]',(255,0,0))
    y = 0
    for ranking in rank:
         font.draw(200,450-50*y, "[No.%d] Time:%4.1f" % (y + 1, ranking), (255,255,255))
         y += 1
         if y > 4:
             break
    hide_cursor()
    mouse.draw()
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






