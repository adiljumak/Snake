import pygame
from random import randrange as rand

from point import Point

class Snake:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    radius = 10
    color = (255, 0, 0)

    def __init__(self):
        self.snake = [Point(rand(self.radius, width- self.radius, 2*self.radius), rand(self.radius, height - self.radius, 2*self.radius)]