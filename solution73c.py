import pygame
import random

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    fps = 100
    clock = pygame.time.Clock()
    running = True
    x1, y1, w, h = 0, 0, 0, 0
    myevent = pygame.USEREVENT + 1
    pygame.time.set_timer(myevent, 5000)
    flag = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == myevent:
                print('!!!!!')
            if event.type == pygame.MOUSEBUTTONUP:
                flag = False
                pygame.draw.circle(screen, (0, 0, 30), event.pos, 20)
            if event.type == pygame.MOUSEMOTION and flag:
                pygame.draw.circle(screen, (0, 0, 25), event.pos, 20)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    flag = True

        for i in range(1000):

            screen.fill(pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                        (random.random() * width,
                         random.random() * height, 1, 1))

        pygame.display.flip()
        clock.tick(fps)