import pygame
import defines


class TitleScreen:
    def __init__(self):
        # Load an image for the title screen
        self.image = pygame.image.load("Goblincampimagepixels.png")
        self.image_rect = self.image.get_rect(center=(defines.SCREEN_WIDTH / 2, defines.SCREEN_HEIGHT / 2))

        # Title text setup
        self.font_title = defines.title_font
        self.title_text = self.font_title.render("GOBLIN                     GUNNER", True, "GREEN")
        self.title_text_rect = self.title_text.get_rect(center=(defines.SCREEN_WIDTH / 2, defines.SCREEN_HEIGHT / 2))
        self.title_text_rect.y -= 110  # Adjust this value to move the text upward or downward

        # Instruction text setup
        self.font_instructions = defines.small_font
        self.instruction_text = self.font_instructions.render("Press Enter to start", True, "WHITE")
        self.instruction_text_rect = self.instruction_text.get_rect(
            center=(defines.SCREEN_WIDTH / 2, defines.SCREEN_HEIGHT / 2))
        self.instruction_text_rect.y += 300  # Adjust this value to move the text upward or downward

        # Retrieve version information from defines.version_keys()
        program_state, program_version, menu_version, settings_version, gameplay_version, title_version = defines.version_keys()

        # List of version information
        version_lines = [
            f"Program Version: {program_state} {program_version}",
            f"Menu Version: {program_state} {menu_version}",
            f"Settings Version: {program_state} {settings_version}",
            f"Gameplay Version: {program_state} {gameplay_version}",
            f"Title Version: {program_state} {title_version}"
        ]

        # Create a list to hold the rendered text surfaces and their rects
        self.version_texts = []

        # Initial position for the first line (bottom-left corner with some margin)
        start_x = 10
        start_y = defines.SCREEN_HEIGHT - 10

        # Font for the version information
        self.font_version = defines.version_font

        # Create each text surface and position it correctly
        for line in version_lines:
            # Render the line as a text surface
            text_surface = self.font_version.render(line, True, "WHITE")
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (start_x, start_y)

            # Add to the list of version texts
            self.version_texts.append((text_surface, text_rect))

            # Adjust the `y` coordinate for the next line, leaving some space between them
            start_y -= text_rect.height + 5  # Adjust this offset for desired spacing

    def handle_events(self, events):
        # Handle events like quitting or switching scenes
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to go to the main menu
                    return "main_menu"
        return None

    def update(self):
        # No specific updates needed here, but you can add logic if required
        pass

    def render(self, screen):
        # Fill the screen with black to avoid artifacts
        screen.fill("BLACK")

        # Draw the background image
        screen.blit(self.image, self.image_rect)

        # Draw the title and instruction text with correct alignment
        screen.blit(self.title_text, self.title_text_rect)  # Title text (adjusted upward)
        screen.blit(self.instruction_text, self.instruction_text_rect)  # Instruction text (adjusted downward)
        for text_surface, text_rect in self.version_texts:
            screen.blit(text_surface, text_rect)
