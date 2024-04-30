import pygame
import sys
import defines
from player import Player

pygame.init()
screen = pygame.display.set_mode((defines.resolution))
clock = pygame.time.Clock()

# Create the player
player = Player(10, 10, defines.p_speed)

running = True
while running:
    dt = clock.get_time() / 10000  # Delta time in seconds

    # Handle events like quitting and player movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
                player.move(0, 0)  # Stop moving when key is released

    # Update the player position with boundary checks
    player.update(dt)

    # Clear the screen and render the player
    screen.fill("BLACK")  # Black background
    player.draw(screen, 100)

    pygame.display.flip()  # Update the display
    clock.tick(defines.FPS)  # Maintain consistent frame rate

pygame.quit()
sys.exit()
