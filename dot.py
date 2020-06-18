import pygame
import random

BLACK = (0, 0, 0)
RADIUS = 3
X_VEL = 1
Y_VEL = 1


class Dot():
    def __init__(self, initial_x, initial_y):
        self.pos = [initial_x, initial_y]
        self.vel = [X_VEL, Y_VEL]

    def move(self):
        self.vel = [random.randrange(-5, 6), random.randrange(-5, 6)]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def draw(self, window):
        pygame.draw.circle(window, BLACK, self.pos, RADIUS)
