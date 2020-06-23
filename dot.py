import pygame
import numpy as np
import random
import pdb

BLACK = (0, 0, 0)
RADIUS = 3
X_VEL = 1
Y_VEL = 1


class Dot():
    def __init__(self, initial_x, initial_y):
        self.pos = np.array([initial_x, initial_y])
        self.vel = np.array([X_VEL, Y_VEL])
        self.acc = np.array([0, 0])
        self.movement_vector = [[0, 0]]
        for i in range(400):
            self.movement_vector.append([random.randrange(-5, 6), random.randrange(-5, 6)])
        self.counter = 0
        self.is_dead = False

    def move(self):
        self.acc = self.movement_vector[self.counter]
        self.counter += 1
        if self.counter >= 400:
            self.is_dead = True
        self.vel += self.acc
        # pdb.set_trace()
        # self.vel = np.round((self.vel / (self.vel.max() / 5))).astype(np.int64)
        self.vel = np.clip(self.vel, -5, 5)
        self.pos += self.vel

    def draw(self, window):
        if self.pos[0] - RADIUS < 0 or self.pos[0] + RADIUS >= window.get_width() \
           or self.pos[1] - RADIUS <= 0 or self.pos[1] + RADIUS >= window.get_height():
            self.is_dead = True
        pygame.draw.circle(window, BLACK, self.pos, RADIUS)
