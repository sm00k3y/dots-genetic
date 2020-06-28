import pygame

BLUE = (0, 0, 255)


class Obstacle:

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)

    def draw(self, window):
        pygame.draw.rect(window, BLUE, self.rect)


class Obstacle_Generator:

    def __init__(self, level):
        self.obstacles = []
        if level == 1:
            self.obstacles.append(Obstacle(400, 300, 600, 20))
        elif level == 2:
            self.obstacles.append(Obstacle(500, 275, 600, 20))
            self.obstacles.append(Obstacle(300, 525, 600, 20))
        elif level == 3:
            self.obstacles.append(Obstacle(300, 200, 600, 20))
            self.obstacles.append(Obstacle(500, 400, 600, 20))
            self.obstacles.append(Obstacle(300, 600, 600, 20))

    def draw(self, window):
        for obst in self.obstacles:
            obst.draw(window)

    def get_obstacles(self):
        return self.obstacles
