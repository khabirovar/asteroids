import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_vector_pos = self.velocity.rotate(random_angle)
            new_vector_neg = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            left_asteroid.velocity = new_vector_pos * 1.2
            right_asteroid.velocity = new_vector_neg * 1.2
