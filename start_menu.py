import pygame
import sys
import defines

pygame.init()
pygame.mixer.init()  # Initialize sound system

# Constants for button colors
BUTTON_COLOR_INACTIVE = "NAVY"
BUTTON_COLOR_ACTIVE = "BLUE"

# Load sound effect for button click
button_click_sound = pygame.mixer.Sound(defines.BUTTON_CLICK_SOUND)


class Button:
    def __init__(self, text, position, size, font_size=30, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        # Draw button with hover effect
        color = self.hover_color if self.hovered() else self.color
        pygame.draw.rect(screen, color, self.rect)

        # Render text
        text_surface = self.font.render(self.text, True, "WHITE")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def hovered(self):
        # Check if mouse is over the button
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                pygame.mixer.Sound.play(button_click_sound)  # Play sound on click
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True  # Button click action
            self.clicked = False
        return False


class MainMenu:
    def __init__(self):
        # Get current screen width and height
        screen_width, screen_height = defines.resolution

        # Initialize buttons with relative positions
        button_width = 200
        button_height = 50
        button_offset = 60  # Offset between buttons

        start_y = screen_height - 330  # Starting Y-position for buttons

        self.play_button = Button(
            "START",
            (screen_width // 2 - button_width // 2, start_y),
            (button_width, button_height)
        )
        self.settings_button = Button(
            "SETTINGS",
            (screen_width // 2 - button_width // 2, start_y + button_offset),
            (button_width, button_height)
        )
        self.quit_button = Button(
            "EXIT",
            (screen_width // 2 - button_width // 2, start_y + 3 * button_offset),
            (button_width, button_height)
        )

    def handle_events(self, events):
        # Handle events for each button
        for event in events:
            if self.play_button.handle_event(event):
                return "start_game"
            if self.settings_button.handle_event(event):
                return "open_settings"
            if self.quit_button.handle_event(event):
                return "quit"
            if event.type == pygame.QUIT:
                return "quit"
        return None

    def update(self):
        # Currently, no additional update logic
        pass

    def render(self, screen):
        # Clear the screen
        screen.fill("WHITE")

        # Draw buttons
        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.quit_button.draw(screen)


def main():
    pygame.init()  # Initialize pygame
    screen_width, screen_height = defines.resolution  # Get screen dimensions

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Menu")

    # Initialize main menu
    main_menu = MainMenu()

    running = True
    while running:
        events = pygame.event.get()

        # Handle events and check transitions
        action = main_menu.handle_events(events)
        if action == "quit":
            running = False
        elif action == "start_game":
            print("Starting game...")
            # Logic to transition to the game scene
        elif action == "open_settings":
            print("Opening settings...")
            # Logic to transition to the settings scene

        # Update and render menu
        main_menu.update()
        main_menu.render(screen)

        pygame.display.flip()  # Refresh display

    pygame.quit()
    sys.exit()  # Exit when done
