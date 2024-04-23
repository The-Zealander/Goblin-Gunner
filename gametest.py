import pygame
import random
import defines

class The_Game:
    def __init__(self):
        # Get the resolution
        screen_width, screen_height = defines.get_resolution()

        # Game properties
        self.tile_size = 20  # Each tile is 20x20 pixels
        self.grid_width = int((screen_width - 280) / self.tile_size)  # Adjusted for info panel
        self.grid_height = int(screen_height / self.tile_size)  # Adjusted for full screen

        # Information panel
        self.info_panel_width = 280
        self.gameplay_width = screen_width - self.info_panel_width

        # Initialize tile surfaces and grid
        self.grass_tile = pygame.Surface((self.tile_size, self.tile_size))
        self.grass_tile.fill("GREEN")

        self.water_tile = pygame.Surface((self.tile_size, self.tile_size))
        self.water_tile.fill("NAVY")

        self.player_tile = pygame.Surface((self.tile_size, self.tile_size))
        self.player_tile.fill("RED")

        # Initialize grid with random elements
        self.grid = [[random.choice([0, 1]) for _ in range(self.grid_width)] for _ in range(self.grid_height)]

        # Initialize player position
        self.player_pos = [0, 0]
        while self.grid[self.player_pos[1]][self.player_pos[0]] != 0:
            self.player_pos[0] += 1
            if self.player_pos[0] >= self.grid_width:
                self.player_pos[0] = 0
                self.player_pos[1] += 1

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player_pos[1] = max(0, self.player_pos[1] - 1)  # Move up
                elif event.key == pygame.K_DOWN:
                    self.player_pos[1] = min(self.grid_height - 1, self.player_pos[1] + 1)  # Move down
                elif event.key == pygame.K_LEFT:
                    self.player_pos[0] = max(0, self.player_pos[0] - 1)  # Move left
                elif event.key == pygame.K_RIGHT:
                    self.player_pos[0] = min(self.grid_width - 1, self.player_pos[0] + 1)  # Move right
                elif event.key == pygame.K_p:
                    return "main_menu"  # Return to main menu
            elif event.type == pygame.QUIT:
                return "quit"
        return None

    def update(self):
        # Game logic updates
        pass

    def render(self, screen):
        # Clear the screen and draw gameplay elements
        screen.fill("WHITE")

        for row in range(self.grid_height):
            for col in range(self.grid_width):
                tile = self.grass_tile if self.grid[row][col] == 0 else self.water_tile
                screen.blit(tile, (col * self.tile_size, row * self.tile_size))

        # Draw the player
        screen.blit(self.player_tile, (self.player_pos[0] * self.tile_size, self.player_pos[1] * self.tile_size))

        # Draw the info section on the right
        info_section_rect = pygame.Rect(self.gameplay_width, 0, 280, screen_height)
        pygame.draw.rect(screen, "GRAY", info_section_rect)

        # Display controls and other information in the info panel
        controls_text = [
            "Controls:",
            " - Arrow keys to move",
            " - P to go to the main menu",
            " - Q to shoot (N/A)",
            " - W for melee (N/A)",
            " - E for shield (N/A)",
        ]

        y_offset = 20  # Initial vertical offset
        for line in controls_text:
            text_surface = pygame.font.Font(None, 30).render(line, True, "BLACK")
            screen.blit(text_surface, (self.gameplay_width + 10, y_offset))  # Padding from left
            y_offset += 30  # Adjust the vertical offset for each line
