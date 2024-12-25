import pygame

import constants as const


def main() -> None:
    pygame.init()

    print('Starting asteroids!')
    print(f'Screen width: {const.SCREEN_WIDTH}')
    print(f'Screen height: {const.SCREEN_HEIGHT}')

    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

    while True:
        screen.fill(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()


if __name__ == '__main__':
    main()
