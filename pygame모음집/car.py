import pygame,os, sys, random
from time import sleep

#게임 화면 정하기
screen_w = 480
screen_h = 800

#색깔
black = (0,0,0)
white = (255,255,255)
gray = (150,150,150)
red = (200,0,0)


current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, "assets")

#게임 전체 변수 정하기
car_count = 3
lane_count = 5
speed = 5
FPS = 60

class Car():
    def __init__(self,  x=0,y=0,dx=0,dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        car_image = p
