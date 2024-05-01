import pygame
import random
from enum import Enum

# Define different tile types
class TileType(Enum):
    GROUND = 0
    WATER = 1
    TREE = 2
    WALL = 3

# Game map class to create and manipulate a simple map
class GameMap:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles = [[TileType.GROUND for _ in range(width)] for _ in range(height)]

    # Add forests to the map
    def add_forests(self, forest_count, forest_size):
        for _ in range(forest_count):
            x = random.randint(0, self.width - forest_size)
            y = random.randint(0, self.height - forest_size)
            for row in range(forest_size):
                for col in range(forest_size):
                    self.tiles[y + row][x + col] = TileType.TREE

    # Add bodies of water to the map
    def add_water_bodies(self, water_count, water_size):
        for _ in range(water_count):
            x = random.randint(0, self.width - water_size)
            y = random.randint(0, self.height - water_size)
            for row in range(water_size):
                for col in range(water_size):
                    self.tiles[y + row][x + col] = TileType.WATER

    # Draw the map based on the camera's position
    def draw(self, screen, camera, tile_colors):
        for row in range(self.height):
            for col in range(self.width):
                tile_type = self.tiles[row][col]
                color = tile_colors.get(tile_type, (255, 255, 255))  # Default to white
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
