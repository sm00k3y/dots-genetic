from dot import Dot
import random


class Population():

    def __init__(self, num_of_dots):
        self.num_of_dots = num_of_dots
        self.dots = [Dot() for _ in range(num_of_dots)]
        self.generation = 1
        self.fitness_sum = 0
        self.max_steps = self.dots[0].brain.size - 1

    def update(self, win_width, win_height, goal):
        for dot in self.dots:
            dot.update(win_width, win_height, goal, self.max_steps)

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
        new_dots = [Dot() for _ in range(self.num_of_dots - 1)]

        for new in new_dots:
            # select parent based on fitness
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            # get baby from parents and mutate
            new.cross_over(parent1, parent2)
            new.brain.mutate()

        best_dot = Dot()
        best_dot.brain.copy(self.best_dot().brain)
        best_dot.is_best = True
        new_dots.append(best_dot)

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

    def best_dot(self):
        max_fitness = 0.0
        best_dot = None
        for dot in self.dots:
            if dot.fitness > max_fitness:
                max_fitness = dot.fitness
                best_dot = dot
        if best_dot.reached_goal:
            self.max_steps = best_dot.step_counter
        return best_dot
