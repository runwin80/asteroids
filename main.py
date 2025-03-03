import pygame
from constants import *

def main():
    # print("Starting Asteroids!")
    # print("Screen width: {0}".format(constants.SCREEN_WIDTH))
    # print("Screen height: {0}".format(constants.SCREEN_HEIGHT))

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()
