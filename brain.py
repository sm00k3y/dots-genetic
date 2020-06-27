import random
import numpy as np


class Brain():

    def __init__(self, num_of_moves, mutation_rate):
        self.size = num_of_moves
        self.movement_vector = np.array([[random.randrange(-5, 6),
                                          random.randrange(-5, 6)] for i in range(num_of_moves)])
        self.mutation_rate = mutation_rate

    def step(self, index):
        return self.movement_vector[index]

    def copy(self, parent_brain):
        for i in range(self.size):
            self.movement_vector[i] = parent_brain.movement_vector[i]

    def mutate(self):
        for i in range(self.size):
            rand = random.random()
            if rand < self.mutation_rate:
                self.movement_vector[i] = [random.randrange(-5, 6), random.randrange(-5, 6)]
