import pico2d
from pico2d import *
import os
import math
open_canvas()
os.getcwd()

grass = load_image('grass.png')
boy = load_image('character.png')


def draw_boy(x,y):
  clear_canvas_now()
  boy.draw_now(x,y)
  delay(0.1)
  
def run_draw_circle():
  print("circle")

  r, cx, cy = 300, 800 // 2, 600 // 2
  for degree in range(0,360,3):# 각도 정의
    theta = math.radians(degree)
    x= r * math.cos(theta) + cx
    y= r * math.sin(theta) + cy
    draw_boy(x,y)

def run_top():
  print('top')
  for x in range(1,800,10):
    draw_boy(x,600)
  pass
def run_right():
  print('right')
  for y in range(600,90,-10):
    draw_boy(800,y)
  pass
def run_bottom():
  for x in range(800,1,-10):
    draw_boy(x,90)
  pass
def run_left():
  for y in range(90,600,10):
    draw_boy(1,y)
  pass
def run_draw_rectangle():
 print("rectangle")
 run_top()
 run_right()
 run_bottom()
 run_left()
 pass#내용이 없는 함수

def coord_calculate(x, x1, y1, x2, y2):
  return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

    
def run_bottom_line():
  print("bottom line")#(700, 50)에서(100, 50)까지
  for x in range(700,100,-10):
    draw_boy(x,50)
  pass
def run_left_line():
  print("left line")#(100, 50)에서(400, 500)까지
  for x in range(100, 400, 10):
    y = coord_calculate(x, 100, 50, 400, 500)
    draw_boy(x,y)
  pass
def run_right_line():
  print("right line")#(400, 500)에서 (700, 50)까지
  for x in range(400, 700, 10):
    y = coord_calculate(x, 400, 500, 700, 50)
    draw_boy(x,y)
  pass
def run_draw_triangle():
  print("triangle")
  run_bottom_line()
  run_left_line()
  run_right_line()
  pass

#뼈대를 잡기
while 1:
 run_draw_rectangle()
 run_draw_circle()
 run_draw_triangle()

close_canvas()