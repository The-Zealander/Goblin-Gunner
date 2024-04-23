import pygame
import random

import defines


class The_Game:
    def __init__(self):
        # Game properties
        self.tile_size = 20  # Each tile is 20x20 pixels
        self.grid_width = 60  # 64 tiles wide
        self.grid_height = 36  # 36 tiles tall

        # Information panel (280 pixels wide, full height)
        self.info_panel_width = self.tile_size * 4
        self.gameplay_width = defines.SCREEN_WIDTH - self.info_panel_width

        self.font = defines.version_font

        # Load tile images (these could be images or simple surfaces with colors)
        self.grass_tile = pygame.Surface((self.tile_size, self.tile_size))
        self.grass_tile.fill("GREEN")  # Green for grass

        self.water_tile = pygame.Surface((self.tile_size, self.tile_size))
        self.water_tile.fill("NAVY")  # Blue for water

        self.player_tile = pygame.Surface((self.tile_size, self.tile_size))
        self.player_tile.fill("RED")  # Red for player

        # Example grid layout: 0 for grass, 1 for water
        self.grid = [[random.choice([0, 1]) for _ in range(self.grid_width)] for _ in range(self.grid_height)]

        self.player_pos = [0, 0]  # Initial player position

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
                    return "main_menu"  # Return to the main menu when "P" is pressed
        return None

    def update(self):
        # Update logic (if needed)
        pass

    def render(self, screen):
        # Clear the screen
        screen.fill("WHITE")

        # Draw the gameplay area
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.grid[row][col] == 0:
                    screen.blit(self.grass_tile, (col * self.tile_size, row * self.tile_size))
                else:
                    screen.blit(self.water_tile, (col * self.tile_size, row * self.tile_size))

        # Draw the player
        screen.blit(self.player_tile, (self.player_pos[0] * self.tile_size, self.player_pos[1] * self.tile_size))

        # Draw the info section on the right
        info_section_rect = pygame.Rect(self.gameplay_width, 0, self.info_panel_width, defines.SCREEN_HEIGHT)
        pygame.draw.rect(screen, "GRAY", info_section_rect)  # Background color for the info section

        # Display controls and other information
        controls_text = [
            "Controls:",
            " - Arrow keys to move",
            " - P to go to menu",
            " - Q to shoot(N/A)",
            " - W to mellee(N/A)",
            " - E to shield(N/A)",
        ]

        y_offset = 20  # Initial vertical offset for text in the info section
        for line in controls_text:
            text_surface = self.font.render(line, True, "BLACK")
            screen.blit(text_surface, (self.gameplay_width + 10, y_offset))  # Padding from left side
            y_offset += 30  # Increment the y_offset for each new line
