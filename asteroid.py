import pygame

from circleshape import CircleShape
from constants import ASTEROID_THICKNESS


class Asteroid(CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_THICKNESS)

    def update(self, dt):
        self.position += (self.velocity * dt)