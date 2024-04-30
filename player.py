import pygame
import defines

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = defines.p_speed
        self.direction = pygame.Vector2(0, 0)

    def update(self, dt):
        # Calculate new position
        new_pos = self.pos + self.direction * self.speed * dt

        # Ensure the player doesn't move outside the screen
        # Check horizontal bounds
        if new_pos.x < 0:
            new_pos.x = 0
        elif new_pos.x > SCREEN_WIDTH / TILE_SIZE - 1:
            new_pos.x = SCREEN_WIDTH / TILE_SIZE - 1

        # Check vertical bounds
        if new_pos.y < 0:
            new_pos.y = 0
        elif new_pos.y > SCREEN_HEIGHT / TILE_SIZE - 1:
            new_pos.y = SCREEN_HEIGHT / TILE_SIZE - 1

        self.pos = new_pos

    def draw(self, screen):
        pygame.draw.rect(
            screen, (0, 255, 0),
            (self.pos.x * TILE_SIZE, self.pos.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

    def move(self, dx, dy):
        self.direction = pygame.Vector2(dx, dy)
