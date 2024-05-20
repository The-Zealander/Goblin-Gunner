import pygame
import math

class Bullet:
    def __init__(self, x, y, angle):
        self.rect = pygame.Rect(x, y, 5, 5)
        self.speed = 400  # Speed in pixels per second
        self.angle = angle
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed
        self.spawn_time = pygame.time.get_ticks()

    def update(self, dt):
        self.rect.x += self.dx * dt
        self.rect.y += self.dy * dt
        if pygame.time.get_ticks() - self.spawn_time > 1000:  # Bullet disappears after 1 second
            self.kill()

    def kill(self):
        del self
