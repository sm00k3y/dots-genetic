import pygame
from population import Population
from goal import Goal

WIDTH = 800
HEIGHT = 800
FPS = 30
COLOR_WHITE = (255, 255, 255)

pygame.init()


def main_loop():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_loop = True

    dots = Population(100)
    goal = Goal(int(WIDTH / 2), 20)

    while game_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        dots.update(WIDTH, HEIGHT)

        draw_window(screen, dots, goal)
        clock.tick(FPS)


def draw_window(screen, dots, goal):
    screen.fill(COLOR_WHITE)
    dots.draw(screen)
    goal.draw(screen)
    pygame.display.update()


if __name__ == "__main__":
    main_loop()
