import pygame
import sys
import defines

# Initialize Pygame
pygame.init()

# Set up the screen with a specified size
screen = pygame.display.set_mode(defines.resolution)

# Set the title of the window
pygame.display.set_caption("Black Background Example")

# Set up the clock for a steady frame rate
clock = pygame.time.Clock()
fps = 60

# Game loop
while True:
    # Handle events like quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill("BLACK")

    # Update the display with new content
    pygame.display.flip()

    # Maintain a steady frame rate
    clock.tick(fps)
