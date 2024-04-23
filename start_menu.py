import pygame
import sys
import defines

pygame.init()
pygame.mixer.init()  # Initialize the mixer for sound playback

# Load sound effect from defines
button_click_sound = pygame.mixer.Sound(defines.BUTTON_CLICK_SOUND)

# Constants for button colors
BUTTON_COLOR_INACTIVE = "NAVY"
BUTTON_COLOR_ACTIVE = "BLUE"

class Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE, font_size=30):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hovered() and self.hover_color or self.color, self.rect)
        text_surface = self.font.render(self.text, True, "WHITE")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                pygame.mixer.Sound.play(button_click_sound)  # Play the sound on button click
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


class MainMenu:
    def __init__(self):
        # Initialize buttons
        self.play_button = Button("START", (defines.SCREEN_WIDTH / 2 - 100, defines.SCREEN_HEIGHT - 330), (200, 50))
        self.settings_button = Button("SETTINGS", (defines.SCREEN_WIDTH / 2 - 100, defines.SCREEN_HEIGHT - 270), (200, 50))
        self.quit_button = Button("EXIT", (defines.SCREEN_WIDTH / 2 - 100, defines.SCREEN_HEIGHT - 150), (200, 50))


    def handle_events(self, events):
        # Handle events for each button
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"
            if self.play_button.handle_event(event):
                return "start_game"
            if self.settings_button.handle_event(event):
                return "open_settings"
            if self.quit_button.handle_event(event):
                sys.exit()
        return None

    def update(self):
        # If there's no specific update logic, you can leave this method empty.
        pass

    def render(self, screen):
        # Clear the screen and draw elements
        screen.fill("WHITE")

        # Draw buttons
        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.quit_button.draw(screen)


def main():
    # Set up pygame
    pygame.init()
    screen = pygame.display.set_mode((defines.SCREEN_WIDTH, defines.SCREEN_HEIGHT))
    pygame.display.set_caption("Main Menu")

    # Initialize main menu
    main_menu = MainMenu()

    running = True
    while running:
        # Handle events
        events = pygame.event.get()
        action = main_menu.handle_events(events)

        if action == "quit":
            running = False
        elif action == "start_game":
            print("Starting game...")
            # Transition to game scene or another state
        elif action == "open_settings":
            print("Opening settings...")
            # Transition to settings scene or another state

        # Call the `update` method (even if it does nothing for now)
        main_menu.update()

        # Render the menu
        main_menu.render(screen)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
