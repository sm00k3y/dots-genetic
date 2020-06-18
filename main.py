import pygame
from dot import Dot

WIDTH = 800
HEIGHT = 800
FPS = 30
COLOR_WHITE = (255, 255, 255)

pygame.init()


def main_loop():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_loop = True

    dots = []
    for i in range(100):
        dots.append(Dot(WIDTH//2, HEIGHT//2))

    while game_loop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        for dot in dots:
            dot.move()

        draw_window(screen, dots)
        clock.tick(FPS)


def draw_window(screen, dots):
    screen.fill(COLOR_WHITE)
    for dot in dots:
        dot.draw(screen)
    pygame.display.update()


if __name__ == "__main__":
    main_loop()
