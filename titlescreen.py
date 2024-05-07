import pygame
import defines


class TitleScreen:
    def __init__(self):
        # Load an image for the title screen
        try:
            self.image = pygame.image.load("images/Goblincampimagepixels.png")
        except FileNotFoundError:
            print("Title screen image not found. Defaulting to black screen.")
            self.image = pygame.Surface(defines.resolution)
            self.image.fill(defines.black)

        # Position image at the center of the screen
        self.image_rect = self.image.get_rect(center=(defines.resolution[0] / 2, defines.resolution[1] / 2))

        # Title text setup
        self.font_title = defines.TITLE_FONT
        self.title_text = self.font_title.render("GOBLIN GUNNER", True, "GREEN")
        self.title_text_rect = self.title_text.get_rect(center=(defines.resolution[0] / 2, 100))  # Positioned at top-center

        # Instruction text setup
        self.font_instructions = defines.SMALL_FONT
        self.instruction_text = self.font_instructions.render("Press Enter to Start", True, "WHITE")
        self.instruction_text_rect = self.instruction_text.get_rect(center=(defines.resolution[0] / 2, defines.resolution[1] - 100))  # Positioned near the bottom

        # Retrieve version information
        version_info = defines.get_version_info()
        version_lines = [
            f"Program Version: {version_info['program_version']} {version_info['program_state']}",
            f"Title Screen Version: {version_info['title_version']}",
            f"Main Menu Version: {version_info['menu_version']}",
        ]

        # Create a list to hold the rendered text surfaces and their rects for version info
        self.version_texts = []
        version_font = defines.VERSION_FONT

        # Initial position for version info
        start_x = 10  # Bottom-left corner
        start_y = defines.resolution[1] - 10

        # Create each text surface and position it
        for line in version_lines:
            text_surface = version_font.render(line, True, "WHITE")
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (start_x, start_y)

            # Add to the list of version texts
            self.version_texts.append((text_surface, text_rect))

            # Adjust for the next line
            start_y -= text_rect.height + 5  # Adjust spacing

    def handle_events(self, events):
        # Handle events like quitting or switching scenes
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "main_menu"  # Transition to main menu
        return None

    def update(self):
        # No specific updates required for this static title screen
        pass

    def render(self, screen):
        # Fill the screen with black to avoid artifacts
        screen.fill("BLACK")

        # Draw the background image
        screen.blit(self.image, self.image_rect)

        # Draw the title and instruction text
        screen.blit(self.title_text, self.title_text_rect)
        screen.blit(self.instruction_text, self.instruction_text_rect)

        # Render the version info text at the bottom-left corner
        for text_surface, text_rect in self.version_texts:
            screen.blit(text_surface, text_rect)
