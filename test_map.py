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
    TileType.GROUND: defines.brown,  # Brown for ground
    TileType.WATER: defines.blue,  # Blue for water
    TileType.TREE: defines.green,  # Green for trees
    TileType.WALL: defines.gray,  # Gray for walls
}

# Game map class with customized drawing and walkable checks
class TestGameMap:
    def __init__(self, width, height, tile_size):
        self.width = width  # Number of tiles wide
        self.height = height  # Number of tiles tall
        self.tile_size = tile_size  # Size of each tile in pixels
        self.tiles = [[TileType.GROUND for _ in range(width)] for _ in range(height)]

        # Add borders (walls) around the edges
        self.add_borders()

    def add_borders(self):
        # Add walls to the top and bottom edges
        for col in range(self.width):
            self.tiles[0][col] = TileType.WALL  # Top wall
            self.tiles[self.height - 1][col] = TileType.WALL  # Bottom wall

        # Add walls to the left and right edges
        for row in range(self.height):
            self.tiles[row][0] = TileType.WALL  # Left wall
            self.tiles[row][self.width - 1] = TileType.WALL  # Right wall

    def is_walkable(self, tile_x, tile_y):
        # Check if a tile is walkable (ground only)
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            tile = self.tiles[tile_y][tile_x]
            return tile == TileType.GROUND
        return False

    def get_tile_effect(self, tile_x, tile_y):
        # Return the effect of the tile on movement
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            tile = self.tiles[tile_y][tile_x]
            if tile == TileType.WATER:
                return 0.5  # Half speed
            elif tile == TileType.TREE or tile == TileType.WALL:
                return 0.0  # No movement
        return 1.0  # Normal speed for ground

    def draw(self, screen, camera):
        # Draw only visible tiles to improve performance
        start_col = max(0, camera.offset_x // self.tile_size)
        end_col = min(self.width, (camera.offset_x + screen.get_width()) // self.tile_size + 1)
        start_row = max(0, camera.offset_y // self.tile_size)
        end_row = min(self.height, (camera.offset_y + screen.get_height()) // self.tile_size + 1)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile_type = self.tiles[row][col]
                color = TILE_COLORS.get(tile_type, defines.brown)  # Default to brown
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
