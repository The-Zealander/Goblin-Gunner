from itertools import cycle

import pygame
from player import Player
from camera import Camera
from map import GameMap, TileType

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32

# Colors for different tile types
TILE_COLORS = {
    TileType.GROUND: (100, 100, 100),  # Gray
    TileType.WATER: (0, 0, 255),  # Blue
    TileType.TREE: (0, 128, 0),  # Green
    TileType.WALL: (255, 0, 0),  # Red
}


def game_loop():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Camera Centered on Player")

    # Create large map with some features
    map_width = 50  # In tiles
    map_height = 50  # In tiles
    game_map = GameMap(map_width, map_height, TILE_SIZE)
    game_map.add_forests(5, 5)  # Add some forests
    game_map.add_water_bodies(3, 4)  # Add some water bodies

    # Create a player and a camera
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    clock = pygame.time.Clock()  # Control frame rate
    running = True

    while running:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement logic
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            dx -= 1
            player.move("left")
        if keys[pygame.K_RIGHT]:
            dx += 1
            player.move("right")
        if keys[pygame.K_UP]:
            dy -= 1
            player.move("up")
        if keys[pygame.K_DOWN]:
            dy += 1
            player.move("down")

        # Update player position and animation
        player.rect.x += dx * 5  # Adjust movement speed
        player.rect.y += dy * 5
        player.current_cycle = cycle(player.animations[player.current_animation])  # Reset cycle if needed

        # Update the camera to keep it centered on the player
        camera.update(player)

        # Clear the screen
        screen.fill((0, 0, 0))  # Black background

        # Draw the map
        game_map.draw(screen, camera, TILE_COLORS)

        # Draw the player
        player.draw(screen, camera)

        pygame.display.flip()  # Update the screen with the latest frame

    pygame.quit()


if __name__ == "__main__":
    game_loop()
