import pygame
import defines

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.speed = defines.p_speed
        self.direction = pygame.Vector2(0, 0)

    def update(self, dt):
        new_pos = self.pos + self.direction * self.speed * dt

        # Ensure the player stays within map boundaries
        if new_pos.x < 0:
            new_pos.x = 0
        elif new_pos.x > defines.resolution[0] / defines.map_tile_size - 1:
            new_pos.x = defines.resolution[0] / defines.map_tile_size - 1

        if new_pos.y < 0:
            new_pos.y = 0
        elif new_pos.y > defines.resolution[1] / defines.map_tile_size - 1:
            new_pos.y = defines.resolution[1] / defines.map_tile_size - 1

        self.pos = new_pos

    def draw(self, screen):
        pygame.draw.rect(
            screen, "GREEN",
            pygame.Rect(
                self.pos.x * defines.map_tile_size,
                self.pos.y * defines.map_tile_size,
                defines.map_tile_size,
                defines.map_tile_size
            )
        )

    def move(self, dx, dy):
        self.direction = pygame.Vector2(dx, dy)
