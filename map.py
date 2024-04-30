import pygame
import defines
import random  # For generating random map patterns

class Map:
    def __init__(self):
        self.width = defines.map_width
        self.height = defines.map_height
        self.tiles = self.generate_map()

    def generate_map(self):
        # Create a basic map with random walls and open spaces
        # Use '.' for empty space and '#' for walls
        map_data = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if random.random() < 0.1:
                    row.append('#')  # 10% chance for a wall
                else:
                    row.append('.')  # 90% chance for empty space
            map_data.append(row)
        return map_data

    def draw(self, screen, camera):
        # Draw the visible part of the map based on the camera position
        start_x = int(camera.x / defines.map_tile_size)
        start_y = int(camera.y / defines.map_tile_size)
        end_x = start_x + int(camera.width / defines.map_tile_size) + 1
        end_y = start_y + int(camera.height / defines.map_tile_size) + 1

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if 0 <= x < self.width and 0 <= y < self.height:
                    tile = self.tiles[y][x]
                    if tile == '#':
                        pygame.draw.rect(
                            screen, "GREY",
                            pygame.Rect(
                                x * defines.map_tile_size - camera.x,
                                y * defines.map_tile_size - camera.y,
                                defines.map_tile_size, defines.map_tile_size
                            )
                        )
