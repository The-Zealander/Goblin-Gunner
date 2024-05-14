import pygame
import random
from enum import Enum
import defines

# Define different tile types
class TileType(Enum):
    GROUND = 0
    WATER = 1
    TREE = 2
    WALL = 3

# Colors for different tile types
TILE_COLORS = {
    TileType.GROUND: defines.brown,  # Brown
    TileType.WATER: defines.blue,  # Blue
    TileType.TREE: defines.green,  # Green
    TileType.WALL: defines.gray,  # Gray
}

class GameMap:
    def __init__(self, width: int, height: int, tile_size: int):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles = [[TileType.GROUND for _ in range(width)] for _ in range(height)]
        self.add_borders()

    def add_borders(self):
        self.tiles[0] = [TileType.WALL] * self.width
        self.tiles[-1] = [TileType.WALL] * self.width
        for row in range(self.height):
            self.tiles[row][0] = TileType.WALL
            self.tiles[row][-1] = TileType.WALL

    def is_walkable(self, tile_x: int, tile_y: int) -> bool:
        map_center_x = self.width // 2
        map_center_y = self.height // 2
        array_x = tile_x + map_center_x
        array_y = tile_y + map_center_y
        if 0 <= array_x < self.width and 0 <= array_y < self.height:
            return self.tiles[array_y][array_x] == TileType.GROUND
        return False

    def draw(self, screen: pygame.Surface, camera):
        start_col = max(0, camera.offset_x // self.tile_size - self.width // 2)
        end_col = min(self.width, (camera.offset_x + screen.get_width()) // self.tile_size - self.width // 2 + 1)
        start_row = max(0, camera.offset_y // self.tile_size - self.height // 2)
        end_row = min(self.height, (camera.offset_y + screen.get_height()) // self.tile_size - self.height // 2 + 1)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                array_x = col + self.width // 2
                array_y = row + self.height // 2
                tile_type = self.tiles[array_y][array_x]
                color = TILE_COLORS.get(tile_type, (255, 255, 255))  # Default to white

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