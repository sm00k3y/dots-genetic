from dot import Dot
import random


class Population():

    def __init__(self, num_of_dots):
        self.num_of_dots = num_of_dots
        self.dots = [Dot() for _ in range(num_of_dots)]
        self.generation = 1
        self.fitness_sum = 0

    def update(self, win_width, win_height, goal):
        for dot in self.dots:
            dot.update(win_width, win_height, goal)

    def draw(self, window):
        for dot in self.dots:
            dot.draw(window)

    def calculate_fitness(self, goal):
        for dot in self.dots:
            dot.calculate_fitness(goal)
            self.fitness_sum += dot.fitness

    def all_dead(self):
        for dot in self.dots:
            if not dot.is_dead and not dot.reached_goal:
                return False
        return True

    def natural_selection(self):
        new_dots = [Dot() for _ in range(self.num_of_dots)]

        for new in new_dots:
            # select parent based on fitness
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            # get baby from parent and mutate
            # new.cross_over(parent1, parent2)
            # new.cross_over2(parent1, parent2)
            new.cross_over3(parent1, parent2)
            # new.copy(parent1)
            new.brain.mutate()

        self.dots = new_dots
        self.generation += 1
        self.fitness_sum = 0

    def select_parent(self):
        rand = random.uniform(0, self.fitness_sum)

        running_sum = 0
        for dot in self.dots:
            running_sum += dot.fitness
            if running_sum > rand:
                return dot

        return None
