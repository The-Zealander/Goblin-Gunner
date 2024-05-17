import pygame
from defines import map_tile_size

GROUND_IMG = pygame.image.load('assets/dirt.jpg')
TREE_IMG = pygame.image.load('assets/tree.png')
WATER_IMG = pygame.image.load('assets/water.jpg')

class GameMap:
    def __init__(self, map_file, tile_size):
        self.tile_size = tile_size
        with open(map_file) as f:
            self.map_data = [list(line.strip()) for line in f]

    def draw(self, screen, camera):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == '0':
                    screen.blit(GROUND_IMG, (x * self.tile_size - camera.offset_x, y * self.tile_size - camera.offset_y))
                elif tile == '1':
                    screen.blit(TREE_IMG, (x * self.tile_size - camera.offset_x, y * self.tile_size - camera.offset_y))
                elif tile == '2':
                    screen.blit(WATER_IMG, (x * self.tile_size - camera.offset_x, y * self.tile_size - camera.offset_y))
