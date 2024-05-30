import pygame
import math


# Define a class to represent a bullet in the game
class Bullet:
    def __init__(self, x, y, angle):
        # Initialize the bullet's position, size, and direction
        self.rect = pygame.Rect(x, y, 5, 5)  # Create a rectangle to represent the bullet's position and size
        self.speed = 400  # Set the bullet's speed in pixels per second
        self.angle = angle  # Set the bullet's direction in radians
        # Calculate the bullet's horizontal and vertical speed components based on the angle
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed
        self.spawn_time = pygame.time.get_ticks()  # Record the time the bullet was spawned

    # Update the bullet's position based on the time elapsed since the last update
    def update(self, dt):
        # Move the bullet by its speed multiplied by the time elapsed
        self.rect.x += self.dx * dt
        self.rect.y += self.dy * dt
        # Check if the bullet has existed for more than 1 second
        if pygame.time.get_ticks() - self.spawn_time > 1000:
            # If so, remove the bullet from the game
            self.kill()

    # Remove the bullet from the game
    def kill(self):
        # Delete the bullet object
        del self
