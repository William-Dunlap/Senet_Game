import pygame


def draw_board():
    height = 450
    width = 1350
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Senet")
    bg_color = (255, 255, 255)
    screen.fill(bg_color)
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, i * (height / 3)), (width, i * (height / 3)), 5)
    for i in range(1, 11):
        pygame.draw.line(screen, (0, 0, 0), (i * (width / 10), 0), (i * (width / 10), height), 5)
    return screen


def main():
    x_co = 400
    y_co = 300
    screen = draw_board()
    while True:
        for event in pygame.event.get():
            pygame.draw.rect(screen, (0, 0, 255), (x_co, y_co, 100, 100))
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
