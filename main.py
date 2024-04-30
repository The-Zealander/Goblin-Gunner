import pygame
import sys
import defines
from player import Player
from enemy import Enemy
from map import Map
from camera import Camera

# Initialize Pygame and create a game window
pygame.init()
screen = pygame.display.set_mode(defines.resolution)
pygame.display.set_caption("Goblin Gunner")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Create game objects
game_map = Map()
camera = Camera(*defines.resolution)
player = Player(10, 10)  # Starting position for the player
enemy = Enemy(15, 15)  # Starting position for the enemy

# Game loop
running = True
while running:
    dt = clock.get_time() / 1000  # Delta time in seconds

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls for the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move(0, -1)  # Move up
            elif event.key == pygame.K_s:
                player.move(0, 1)  # Move down
            elif event.key == pygame.K_a:
                player.move(-1, 0)  # Move left
            elif event.key == pygame.K_d:
                player.move(1, 0)  # Move right

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
                player.move(0, 0)  # Stop moving

    # Update player position with boundary checks
    player.update(dt)

    # Update enemy with player position for tracking
    enemy.update(dt, player.pos)

    # Update the camera to follow the player
    camera.update((player.pos.x * defines.map_tile_size, player.pos.y * defines.map_tile_size))

    # Clear the screen with a color
    colors = defines.get_colors()
    screen.fill(colors["BLACK"])  # Black background

    # Render the map, player, and enemy with the camera adjustment
    game_map.draw(screen, camera)
    player.draw(screen)
    enemy.draw(screen)

    # Update the display
    pygame.display.flip()

    # Maintain a steady frame rate
    clock.tick(defines.FPS)

# Exit Pygame
pygame.quit()
sys.exit()
