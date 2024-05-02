import pygame
from player import Player, Direction
from camera import Camera
import map
import test_map
import defines

# Set to True for test mode, False for regular mode
map_test_mode = True
#player_test_mode = False
#camera_test_mode = False
#enemy_test_mode = False
#calculations_test_mode = False


def game_loop():
    pygame.init()

    screen = pygame.display.set_mode(defines.resolution)
    pygame.display.set_caption(defines.GAME_NAME)

    # Create the correct map based on the mode
    if map_test_mode:
        game_map = test_map.TestGameMap(defines.test_map_width, defines.test_map_height, defines.map_tile_size)
    else:
        game_map = map.GameMap(defines.map_width, defines.map_height, defines.map_tile_size)

    # Create a player and a camera centered on the map
    player = Player(game_map.width * game_map.tile_size // 2, game_map.height * game_map.tile_size // 2)
    camera = Camera(defines.resolution[0], defines.resolution[1])

    clock = pygame.time.Clock()  # Control frame rate
    running = True

    while running:
        dt = clock.tick(defines.FPS) / 1000.0  # Delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement logic
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            dx -= 1
            player.move(Direction.LEFT, dt)  # Update animation
        if keys[pygame.K_RIGHT]:
            dx += 1
            player.move(Direction.RIGHT, dt)  # Update animation
        if keys[pygame.K_UP]:
            dy -= 1
            player.move(Direction.UP, dt)  # Update animation
        if keys[pygame.K_DOWN]:
            dy += 1
            player.move(Direction.DOWN, dt)  # Update animation

        # Calculate new pixel coordinates
        new_x = player.rect.x + dx * defines.p_speed
        new_y = player.rect.y + dy * defines.p_speed

        # Convert to tile coordinates
        tile_x = new_x // defines.map_tile_size
        tile_y = new_y // defines.map_tile_size

        # If the new position is walkable, update player's position
        if game_map.is_walkable(tile_x, tile_y):
            player.rect.x = new_x
            player.rect.y = new_y

        # Update the camera to keep it centered on the player
        camera.update(player)

        # Clear the screen
        screen.fill(defines.black)  # Black background

        # Draw the map
        game_map.draw(screen, camera, map.TILE_COLORS)

        # Draw the player
        player.draw(screen, camera)

        pygame.display.flip()  # Update the screen with the latest frame

    pygame.quit()


if __name__ == "__main__":
    game_loop()
