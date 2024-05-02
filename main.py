from itertools import cycle

import pygame
from player import Player
from camera import Camera
from map import GameMap, TileType
import defines

# Colors for different tile types
TILE_COLORS = {
    TileType.GROUND: defines.brown,  # Gray
    TileType.WATER: defines.blue,  # Blue
    TileType.TREE: defines.green,  # Green
    TileType.WALL: defines.red,  # Red
}


def game_loop():
    pygame.init()

    screen = pygame.display.set_mode(defines.resolution)
    pygame.display.set_caption(defines.GAME_NAME)

    clock = pygame.time.Clock()  # Define the clock here

    # Create a large map with some features
    map_width = 1920  # In tiles
    map_height = 1080  # In tiles
    game_map = GameMap(map_width, map_height, defines.map_tile_size)
    game_map.add_forests(5, 5)  # Add some forests
    game_map.add_water_bodies(3, 4)  # Add some water bodies

    # Create a player and a camera
    player = Player(defines.resolution[0] // 2, defines.resolution[1] // 2)
    camera = Camera(defines.resolution[0], defines.resolution[1])

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
        player.rect.x += dx * defines.p_speed  # Adjust movement speed
        player.rect.y += dy * defines.p_speed
        player.current_cycle = cycle(player.animations[player.current_animation])  # Reset cycle if needed

        # Update the camera to keep it centered on the player
        camera.update(player)

        # Clear the screen
        screen.fill(defines.black)  # Black background

        # Draw the map
        game_map.draw(screen, camera, TILE_COLORS)

        # Draw the player
        player.draw(screen, camera)

        pygame.display.flip()  # Update the screen with the latest frame

    pygame.quit()


if __name__ == "__main__":
    game_loop()
