import pygame

import constants as const
from player import Player


def main() -> None:
    pygame.init()

    print('Starting asteroids!')
    print(f'Screen width: {const.SCREEN_WIDTH}')
    print(f'Screen height: {const.SCREEN_HEIGHT}')

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

    player = Player(const.SCREEN_WIDTH / 2, const.SCREEN_HEIGHT / 2)

    updatable.add(player)
    drawable.add(player)

    while True:
        screen.fill(0)
        
        for item in updatable:
            item.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(const.TICKRATE) / 1000


if __name__ == '__main__':
    main()
