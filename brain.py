import random


class Brain():

    def __init__(self, num_of_moves):
        self.size = num_of_moves
        self.movement_vector = [[random.randrange(-5, 6), random.randrange(-5, 6)] for i in range(num_of_moves)]

    def step(self, index):
        return self.movement_vector[index]
