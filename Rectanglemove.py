import pico2d
import os
from pico2d import *
open_canvas()
os.getcwd()

grass = load_image('grass.png')
boy = load_image('character.png')

open_canvas()

def run_draw_circle():
 print("circle")

 clear_canvas_now()
 boy.draw_now(400,300)
 delay(1)
 pass#내용이 없는 함수



def run_draw_rectangle():
 print("rectangle")
 pass#내용이 없는 함수







#뼈대를 잡기
while True:
 run_draw_rectangle()
 run_draw_circle()



close_canvas()
