import pygame
import random
import sys


def draw_squares(height, width):
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * i), (600, SQUARE_SIZE * i), LINE_WIDTH)


def main():
    height = 450
    width = 1350
    pygame.init()
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption("Senet")
    x_co = 400
    y_co = 300
    bg_color = (255, 255, 255)
    screen.fill(bg_color)
    while True:
        for event in pygame.event.get():
            pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x_co, y_co, 50, 50))
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button = pygame.key.get_pressed()
        if button[pygame.K_LEFT]:
            x_co -= 5
        if button[pygame.K_RIGHT]:
            x_co += 5
        if button[pygame.K_UP]:
            y_co -= 5
        if button[pygame.K_DOWN]:
            y_co += 5

        if x_co < 0:
            x_co = 0
        if x_co > 800:
            x_co = 750
        if y_co < 0:
            y_co = 0
        if y_co > 600:
            y_co = 550

        pygame.time.Clock().tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()
