import math
from pico2d import *
import os

os.chdir('C:\\Users\\PC\Desktop\\python\\DRILL--1')

pico2d.open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
z = 0
while(1):
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,90)
        x += 4
        delay(0.01)

    while(y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(790,y)
        y += 4
        delay(0.01)

    while (x > 10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,580)
        x -= 4
        delay(0.01)

    while (y > 100):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(10,y)
        y -= 4
        delay(0.01)
    
close_canvas()
