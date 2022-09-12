import pygame
import sys
from sprites.space import Space

pygame.init()

# Константы
WIDTH = 600
HEIGHT = 700
FPS = 60

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("zombies")
clock = pygame.time.Clock()


def main():
    # Спрайты
    space = Space()
    running = True
    while running:
        # Частота обновления экрана
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Рендеринг
        space.draw(screen)
                                    #   slide 8
        # Обновление спрайтoB
        space.update()

        # Обновление экрана
        pygame.display.update()


if __name__ == "__main__":
    main()

