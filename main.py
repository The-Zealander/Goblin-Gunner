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
class Quit_Button:
    def __init__(self, text, position, size, color=(0, 255, 0), hover_color=(0, 200, 0), font_size=30):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.hovered() else self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                self.clicked = True
                print("you clicked quit")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


#play_button = Play_Button("Exit", (100, 100), (200, 50))
#Settings_button = Settings_Button("Exit", (100, 100), (200, 50))
#Unknown_button = Unknown_Button("Exit", (100, 100), (200, 50))
quit_button = Quit_Button("Exit", (100, 100), (200, 50))

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
            #play_button.handle_event(event)
            #settings_button.handle_event(event)
            #Credits_button.handle_event(event)
            quit_button.handle_event(event)



        # Clear the screen
        screen.fill(WHITE)

        # Draw buttons
        # play_button.draw(screen)
        # settings_button.draw(screen)
        # credits_button.draw(screen)
        quit_button.draw(screen)

        # Version indicator
        draw_text(screen, "Version 1.0", BLACK, 10, SCREEN_HEIGHT - 40)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()