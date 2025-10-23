import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        asteroid = pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)    

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_angle_1 = self.velocity.rotate(angle)
        new_angle_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        sub_1 = Asteroid(self.position[0], self.position[1], new_radius)
        sub_2 = Asteroid(self.position[0], self.position[1], new_radius)
        sub_1.velocity = new_angle_1 * 1.2
        sub_2.velocity = new_angle_2 * 1.2
