import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set font
font = pygame.font.SysFont(None, 36)

# Function to draw text on screen
def draw_text(surface, text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Function to create buttons
def draw_button(surface, text, x, y, width, height):
    pygame.draw.rect(surface, GRAY, (x, y, width, height))
    pygame.draw.rect(surface, BLACK, (x, y, width, height), 2)
    draw_text(surface, text, BLACK, x + 10, y + 10)

# Main function
def main():
    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Start Menu")

    # Main loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw buttons
        draw_button(screen, "Start", 100, 100, 200, 50)
        draw_button(screen, "Options", 100, 200, 200, 50)
        draw_button(screen, "Quit", 100, 300, 200, 50)

        # Version indicator
        draw_text(screen, "Version 1.0", BLACK, 10, SCREEN_HEIGHT - 40)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
