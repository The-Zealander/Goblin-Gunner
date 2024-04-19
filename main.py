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
BUTTON_COLOR_INACTIVE = (50, 250, 50)
BUTTON_COLOR_ACTIVE = (100, 200, 100)

# define different fonts
version_font = pygame.font.SysFont(None, 20)

#Other variables or constatnts
Menu_Version = "0.2"
Settings_Version = "0.0"
Game_Version = "0.0"

# Function to draw text on screen
def draw_text(surface, text, color, x, y):
    text_surface = version_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


# Function to create buttons

class Play_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE,
                 font_size=30):
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
        text_surface = self.font.render(self.text, True, WHITE)
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
                print("you clicked start")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


class Settings_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE,
                 font_size=30):
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
        text_surface = self.font.render(self.text, True, WHITE)
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
                print("you clicked Settings")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


class Unknown_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE,
                 font_size=30):
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
        text_surface = self.font.render(self.text, True, WHITE)
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
                print("you clicked unknown")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


class Quit_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE,
                 font_size=30):
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
        text_surface = self.font.render(self.text, True, WHITE)
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
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


play_button = Play_Button("START", (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 330), (200, 50))
settings_button = Settings_Button("SETTINGS", (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 270), (200, 50))
unknown_button = Unknown_Button("UNKNOWN", (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 210), (200, 50))
quit_button = Quit_Button("EXIT", (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 150), (200, 50))


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
            play_button.handle_event(event)
            settings_button.handle_event(event)
            unknown_button.handle_event(event)
            quit_button.handle_event(event)

        # Clear the screen
        screen.fill(WHITE)

        # Draw buttons
        play_button.draw(screen)
        settings_button.draw(screen)
        unknown_button.draw(screen)
        quit_button.draw(screen)

        # Version indicators
        draw_text(screen, f"Game Version {Game_Version}", BLACK, 10, SCREEN_HEIGHT - 75)
        draw_text(screen, f"Settings Version {Settings_Version}", BLACK, 10, SCREEN_HEIGHT - 50)
        draw_text(screen, f"Menu Version {Menu_Version}", BLACK, 10, SCREEN_HEIGHT - 25)
        #make ^ this dependant on the "Version" constant.
        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
