import pygame
import random

import defines
import map

class Enemy:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = defines.small_enemey_size
        self.color = (255, 0, 0)  # Red color
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = 1  # Adjust speed as needed

    def draw(self, screen, camera):
        pygame.draw.rect(screen, self.color, (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y, self.size, self.size))

    def update(self, dt, player_pos):
        # Randomly choose a direction to move
        direction = random.choice(["up", "down", "left", "right"])

        # Update enemy position based on the chosen direction
        if direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed
        elif direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed

        # Ensure enemy stays within map boundaries
        self.rect.x = max(0, min(self.rect.x, defines.map_width - self.size))
        self.rect.y = max(0, min(self.rect.y, defines.map_height - self.size))
