import pygame
from population import Population
from goal import Goal

WIDTH = 800
HEIGHT = 800
FPS = 30
BG_COLOR = (255, 255, 255)

pygame.init()


def main_loop():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_loop = True

    dots = Population(200)
    goal = Goal(int(WIDTH / 2), 20)

    while game_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        if dots.all_dead():
            dots.calculate_fitness(goal)
            dots.natural_selection()
            # dots.mutate_those_babies()
        else:
            dots.update(WIDTH, HEIGHT, goal)
            draw_window(screen, dots, goal)

        clock.tick(FPS)


def draw_window(screen, dots, goal):
    screen.fill(BG_COLOR)
    goal.draw(screen)
    dots.draw(screen)
    pygame.display.update()


if __name__ == "__main__":
    main_loop()
