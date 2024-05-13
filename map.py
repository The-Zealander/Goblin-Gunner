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
    TileType.GROUND: defines.brown,  # Gray
    TileType.WATER: defines.blue,  # Blue
    TileType.TREE: defines.green,  # Green
    TileType.WALL: defines.gray,  # Gray
}


# Game map class with centered coordinates
class GameMap:
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
        """Check if a tile is walkable (not a wall, water, or tree)"""
        # Adjust for the new coordinate system (centered origin)
        map_center_x = self.width // 2
        map_center_y = self.height // 2

        # Convert centered coordinates to array index
        array_x = tile_x + map_center_x
        array_y = tile_y + map_center_y

        if 0 <= array_x < self.width and 0 <= array_y < self.height:
            return self.tiles[array_y][array_x] == TileType.GROUND
        return False

    def draw(self, screen, camera):
        """Draw only visible tiles to improve performance"""
        map_center_x = self.width // 2
        map_center_y = self.height // 2

        # Adjust the rendering to account for the centered coordinate system
        start_col = max(0, camera.offset_x // self.tile_size - map_center_x)
        end_col = min(self.width, (camera.offset_x + screen.get_width()) // self.tile_size - map_center_x + 1)
        start_row = max(0, camera.offset_y // self.tile_size - map_center_y)
        end_row = min(self.height, (camera.offset_y + screen.get_height()) // self.tile_size - map_center_y + 1)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                # Convert centered coordinates to array index
                array_x = col + map_center_x
                array_y = row + map_center_y

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
