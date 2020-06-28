import pygame
from population import Population
from goal import Goal

pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 30
BG_COLOR = (255, 255, 255)


def main_loop():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("dejavusansmono", 17)
    clock = pygame.time.Clock()
    game_loop = True

    dots = Population(400)
    goal = Goal(int(WIDTH / 2), 20)

    generation = font.render("Population: 1", True, (0, 0, 0))
    gen_rect = generation.get_rect()
    gen_rect.center = (WIDTH - 90, 15)

    while game_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        if dots.all_dead():
            dots.calculate_fitness(goal)
            dots.natural_selection()
            generation = font.render("Population: {}".format(dots.generation), True, (0, 0, 0))
        else:
            dots.update(WIDTH, HEIGHT, goal)
            draw_window(screen, dots, goal, generation, gen_rect)

        clock.tick(FPS)


def draw_window(screen, dots, goal, generation, gen_rect):
    screen.fill(BG_COLOR)
    goal.draw(screen)
    dots.draw(screen)
    screen.blit(generation, gen_rect)
    pygame.display.update()


if __name__ == "__main__":
    main_loop()
