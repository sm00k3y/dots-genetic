import pygame
import numpy as np
from brain import Brain
import random

BLACK = (0, 0, 0)
RADIUS = 3
X_VEL = 1
Y_VEL = 1
INITIAL_X = 400
INITIAL_Y = 750

BRAIN_SIZE = 400
MUTATION_RATE = 0.02


class Dot():

    def __init__(self):
        self.pos = np.array([INITIAL_X, INITIAL_Y])
        self.vel = np.array([X_VEL, Y_VEL])
        self.acc = np.array([0, 0])
        self.brain = Brain(BRAIN_SIZE, MUTATION_RATE)
        self.step_counter = 0
        self.is_dead = False
        self.reached_goal = False
        self.fitness = 0

    def move(self):
        self.acc = self.brain.step(self.step_counter)
        self.step_counter += 1
        if self.step_counter >= BRAIN_SIZE:
            self.is_dead = True
        self.vel += self.acc
        self.vel = np.clip(self.vel, -5, 5)
        self.pos += self.vel

    def update(self, win_width, win_height, goal):
        if not self.is_dead and not self.reached_goal:
            self.move()
            if self.pos[0] <= RADIUS or self.pos[0] + RADIUS >= win_width \
               or self.pos[1] <= RADIUS or self.pos[1] + RADIUS >= win_height:
                self.is_dead = True
            elif np.linalg.norm(self.pos - goal.pos, ord=2) < goal.radius:
                self.reached_goal = True

    def draw(self, window):
        pygame.draw.circle(window, BLACK, self.pos, RADIUS)

    def calculate_fitness(self, goal):
        dist_to_goal = np.linalg.norm(self.pos - goal.pos, ord=2)
        # dist_to_goal = math.sqrt((self.pos[0] - goal.pos[0])**2 + (self.pos[1] - goal.pos[1])**2)  # import math
        self.fitness = 1.0 / (dist_to_goal**2)

    def cross_over(self, parent1, parent2):
        for i in range(BRAIN_SIZE):
            rand = random.random()

            if rand < 0.45:
                self.brain.movement_vector[i] = parent1.brain.movement_vector[i]
            elif rand < 0.90:
                self.brain.movement_vector[i] = parent2.brain.movement_vector[i]
            else:
                self.brain.movement_vector[i] = [random.randrange(-5, 6), random.randrange(-5, 6)]

    def cross_over2(self, parent1, parent2):
        for i in range(BRAIN_SIZE):
            self.brain.movement_vector[i] = (parent1.brain.movement_vector[i] + parent2.brain.movement_vector[i]) / 2

    def cross_over3(self, parent1, parent2):
        point = parent1.fitness / (parent1.fitness + parent2.fitness)

        for i in range(BRAIN_SIZE):
            rand = random.random()

            if rand < point:
                self.brain.movement_vector[i] = parent1.brain.movement_vector[i]
            else:
                self.brain.movement_vector[i] = parent2.brain.movement_vector[i]

    def copy(self, parent):
        self.brain.copy(parent.brain)
