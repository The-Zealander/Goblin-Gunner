import pygame
import terrain


# Game map class with tile-based logic
class TestGameMap:
    def __init__(self, width, height, tile_size):
        self.width = width  # Number of tiles wide
        self.height = height  # Number of tiles tall
        self.tile_size = tile_size  # Size of each tile in pixels
        self.tiles = [[terrain.TileType.GROUND for _ in range(width)] for _ in range(height)]

        # Add borders (walls) around the edges
        self.add_borders()

    def add_borders(self):
        # Add walls to the top, bottom, left, and right edges
        for col in range(self.width):
            self.tiles[0][col] = terrain.TileType.WALL  # Top wall
            self.tiles[self.height - 1][col] = terrain.TileType.WALL  # Bottom wall
        for row in range(self.height):
            self.tiles[row][0] = terrain.TileType.WALL  # Left wall
            self.tiles[row][self.width - 1] = terrain.TileType.WALL  # Right wall

    def add_water(self, x, y, width, height):
        # Ensure water is added within map boundaries
        for row in range(y, y + height):
            for col in range(x, x + width):
                if 0 <= col < self.width and 0 <= row < self.height:
                    self.tiles[row][col] = terrain.TileType.WATER

    def add_forest(self, x, y, width, height):
        # Ensure water is added within map boundaries
        for row in range(y, y + height):
            for col in range(x, x + width):
                if 0 <= col < self.width and 0 <= row < self.height:
                    self.tiles[row][col] = terrain.TileType.TREE

    def is_walkable(self, tile_x, tile_y):
        # Check if a tile is walkable based on the terrain properties
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            tile = self.tiles[tile_y][tile_x]
            return terrain.TILE_PROPERTIES[tile]["walkable"]
        return False

    def get_speed_modifier(self, tile_x, tile_y):
        # Return the speed modifier based on the tile type
        if 0 <= tile_x < self.width and 0 <= tile_y < self.height:
            tile = self.tiles[tile_y][tile_x]
            return terrain.TILE_PROPERTIES[tile]["speed_modifier"]
        return 0.0  # If out of bounds, default to no speed

    def draw(self, screen, camera):
        # Draw only visible tiles based on the camera's offset
        start_col = max(0, camera.offset_x // self.tile_size)
        end_col = min(self.width, (camera.offset_x + screen.get_width()) // self.tile_size + 1)
        start_row = max(0, camera.offset_y // self.tile_size)
        end_row = min(self.height, (camera.offset_y + screen.get_height()) // self.tile_size + 1)

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                tile = self.tiles[row][col]
                color = terrain.TILE_PROPERTIES[tile]["color"]
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
