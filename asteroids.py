import pygame
import random
from circleshape import *
from constants import *

class Asteroids(CircleShape):
     def __init__(self, x, y, radius):
       super().__init__(x, y, radius)

     def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

     def update(self, dt):
       self.position += self.velocity * dt
       
     def split(self):
       self.kill()
       if self.radius <= ASTEROID_MIN_RADIUS:
         return
       else:
         random_angle = random.uniform(20, 50)
         vec1 = self.velocity.rotate(random_angle)
         vec2 = self.velocity.rotate(-random_angle)
         new_radius = self.radius - ASTEROID_MIN_RADIUS
         new_asteroid1 = Asteroids(self.position[0], self.position[1], new_radius)
         new_asteroid2 = Asteroids(self.position[0], self.position[1], new_radius)
         new_asteroid1.velocity = vec1 * 1.2
         new_asteroid2.velocity = vec2 * 1.2


