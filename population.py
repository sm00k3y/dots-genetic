from dot import Dot


class Population():

    def __init__(self, num_of_dots):
        self.num_of_dots = num_of_dots
        self.dots = [Dot() for i in range(num_of_dots)]

    def update(self, win_width, win_height):
        for dot in self.dots:
            dot.update(win_width, win_height)

    def draw(self, window):
        for dot in self.dots:
            dot.draw(window)
