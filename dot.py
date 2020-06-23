import pygame
import numpy as np
import random
import pdb
from brain import Brain

BLACK = (0, 0, 0)
RADIUS = 3
X_VEL = 1
Y_VEL = 1
INITIAL_X = 400
INITIAL_Y = 750
BRAIN_SIZE = 400


class Dot():
    def __init__(self):
        self.pos = np.array([INITIAL_X, INITIAL_Y])
        self.vel = np.array([X_VEL, Y_VEL])
        self.acc = np.array([0, 0])
        self.brain = Brain(BRAIN_SIZE)
        self.counter = 0
        self.is_dead = False

    def move(self):
        self.acc = self.brain.step(self.counter)
        self.counter += 1
        if self.counter >= BRAIN_SIZE:
            self.is_dead = True
        self.vel += self.acc
        self.vel = np.clip(self.vel, -5, 5)
        self.pos += self.vel

    def update(self, win_width, win_height):
        if not self.is_dead:
            self.move()
            if self.pos[0] <= RADIUS or self.pos[0] + RADIUS >= win_width \
               or self.pos[1] <= RADIUS  or self.pos[1] + RADIUS >= win_height:
                self.is_dead = True

    def draw(self, window):
        pygame.draw.circle(window, BLACK, self.pos, RADIUS)
