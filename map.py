import pygame

import defines
from terrain import TILE_PROPERTIES, TileType
from defines import map_width, map_height, map_tile_size

class GameMap:
    def __init__(self):
        self.ground_layer = []  # For ground tiles
        self.top_layer = []  # For objects like trees and buildings
        self.bottom_layer = []  # For objects like water
        self.width = map_width
        self.height = map_height
        self.tile_size = map_tile_size
        self.tiles = self.generate_map()

    def generate_map(self):
        tiles = [[TileType.GROUND for _ in range(self.width)] for _ in range(self.height)]

        # Add walls around the edges
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    tiles[y][x] = TileType.WALL

        # Predefined tile locations
        grass_locations = [(5, 5), (5, 6), (5, 7)]
        water_locations = [(10, 10), (10, 11), (10, 12)]
        tree_locations = [(15, 15), (15, 16), (15, 17)]

        # Place grass tiles
        for x, y in grass_locations:
            tiles[y][x] = TileType.GRASS

        # Place water tiles
        for x, y in water_locations:
            tiles[y][x] = TileType.WATER

        # Place tree tiles
        for x, y in tree_locations:
            tiles[y][x] = TileType.TREE

        return tiles

    def place_tile(self, x, y, tile_type):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_type

    def draw(self, screen, camera):
        start_x = max(0, camera.rect.left // self.tile_size)
        start_y = max(0, camera.rect.top // self.tile_size)
        end_x = min(self.width, (camera.rect.right + self.tile_size - 1) // self.tile_size)
        end_y = min(self.height, (camera.rect.bottom + self.tile_size - 1) // self.tile_size)

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                tile = self.tiles[y][x]
                tile_prop = TILE_PROPERTIES[tile]
                # Check om koordinat er lige eller ulige og vælg farve ud fra det.
                if (x + y) % 2 == 0:
                    color = tile_prop["color"]
                else:
                    color = defines.gray
                rect = pygame.Rect(
                    x * self.tile_size - camera.rect.left,
                    y * self.tile_size - camera.rect.top,
                    self.tile_size, self.tile_size
                )
                pygame.draw.rect(screen, color, rect)
