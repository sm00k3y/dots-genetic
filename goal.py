import pygame

COLOR_RED = (255, 0, 0)
RADIUS = 10

class Goal():

    def __init__(self, x, y):
        self.pos = (x, y)

    def draw(self, window):
        pygame.draw.circle(window, COLOR_RED, self.pos, RADIUS)
