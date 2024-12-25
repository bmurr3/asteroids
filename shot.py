import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_THICKNESS


class Shot(CircleShape):
    containers = ()
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_THICKNESS)

    def update(self, dt):
        self.position += (self.velocity * dt)