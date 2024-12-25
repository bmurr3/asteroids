import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_THICKNESS, ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_SCALE


class Asteroid(CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_THICKNESS)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        left_velocity, right_velocity = (
            self.velocity.rotate(split_angle) * ASTEROID_SPLIT_SPEED_SCALE,
            self.velocity.rotate(-split_angle) * ASTEROID_SPLIT_SPEED_SCALE
        )
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        left_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        left_asteroid.velocity = left_velocity

        right_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        right_asteroid.velocity = right_velocity
