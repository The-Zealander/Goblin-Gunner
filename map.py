import pygame
from terrain import TILE_PROPERTIES, TileType


class GameMap:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles = [[TileType.GROUND for _ in range(width)] for _ in range(height)]
        self.add_borders()

    def add_borders(self):
        for col in range(self.width):
            self.tiles[0][col] = TileType.WALL
            self.tiles[self.height - 1][col] = TileType.WALL
        for row in range(self.height):
            self.tiles[row][0] = TileType.WALL
            self.tiles[row][self.width - 1] = TileType.WALL

    def is_walkable(self, tile_x, tile_y):
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            return TILE_PROPERTIES[self.tiles[tile_y][tile_x]]["walkable"]
        return False

    def draw(self, screen, camera):
        start_col = max(0, camera.offset_x // self.tile_size)
        end_col = min(self.width, (camera.offset_x + screen.get_width()) // self.tile_size + 1)
        start_row = max(0, camera.offset_y // self.tile_size)
        end_row = min(self.height, (camera.offset_y + screen.get_height()) // self.tile_size + 1)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile_type = self.tiles[row][col]
                color = TILE_PROPERTIES[tile_type]["color"]
                pygame.draw.rect(
                    screen,
                    color,
                    (
                        col * self.tile_size - camera.offset_x,
                        row * self.tile_size - camera.offset_y,
                        self.tile_size,
                        self.tile_size,
                    ),
                )
