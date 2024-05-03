import pygame
import random
import defines
import calc

class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = defines.e_speed
        self.direction = pygame.Vector2(0, 0)
        self.change_direction()

    def change_direction(self):
        # Randomize the direction (up, down, left, right, or stay still)
        self.direction.x = random.choice([-1, 0, 1])
        self.direction.y = random.choice([-1, 0, 1])

    def update(self, dt, player_pos):
        # Move based on direction
        self.pos += self.direction * self.speed * dt

        # Randomly change direction
        if random.random() < 0.02:
            self.change_direction()

        # Move toward the player if within detection radius
        distance = calc.calculate_distance(self.pos, player_pos)
        if distance < defines.detec_rad:
            direction_to_player = pygame.Vector2(player_pos) - self.pos
            direction_to_player.normalize_ip()
            self.direction = direction_to_player

    def draw(self, screen):
        pygame.draw.rect(
            screen, (255, 0, 0),
            pygame.Rect(
                self.pos.x * defines.map_tile_size,
                self.pos.y * defines.map_tile_size,
                defines.map_tile_size,
                defines.map_tile_size
            )
        )
