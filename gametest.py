import pygame
import random
import defines


class The_Game:
    def __init__(self):
        # Get the resolution
        screen_width, screen_height = defines.get_current_resolution()

        # Game properties
        self.tile_size = 20  # Each tile is 20x20 pixels
        self.grid_width = int((screen_width - 280) / self.tile_size)  # Adjusted for info panel
        self.grid_height = int(screen_height / self.tile_size)  # Adjusted for full screen

        # Information panel
        self.info_panel_width = 280
        self.gameplay_width = screen_width - self.info_panel_width

        # Load the image for the grass tile
        self.grass_tile = pygame.image.load("images/grass_tile.png")  # Load the image file
        # Optionally scale the image to match the tile size
        self.grass_tile = pygame.transform.scale(self.grass_tile, (self.tile_size, self.tile_size))

        # Load the image for the grass tile
        self.water_tile = pygame.image.load("images/water_tile.png")  # Load the image file
        # Optionally scale the image to match the tile size
        self.water_tile = pygame.transform.scale(self.water_tile, (self.tile_size, self.tile_size))

        # Load the image for the stone tile
        self.stone_tile = pygame.image.load("images/stone_tile.png")  # Load the image file
        # Optionally scale the image to match the tile size
        self.stone_tile = pygame.transform.scale(self.stone_tile, (self.tile_size, self.tile_size))


        # Load the image for the longgrass tile
        self.longgrass_tile = pygame.image.load("images/long_grass_tile.png")  # Load the image file
        # Optionally scale the image to match the tile size
        self.longgrass_tile = pygame.transform.scale(self.longgrass_tile, (self.tile_size, self.tile_size))

        # Load the image for the tree tile
        #self.tree_tile = pygame.image.load("tree.png")  # Load the image file
        # Optionally scale the image to match the tile size
        #self.tree_tile = pygame.transform.scale(self.tree_tile, (self.tile_size, self.tile_size))

        # self.water_tile = pygame.Surface((self.tile_size, self.tile_size))
        # self.water_tile.fill("NAVY")

        # self.water_tile = pygame.Surface((self.tile_size, self.tile_size))
        # self.water_tile.fill("NAVY")

        # Load the image for the grass tile
        self.player_token = pygame.image.load("images/player_placeholder.png")  # Load the image file
        # Optionally scale the image to match the tile size
        self.player_token = pygame.transform.scale(self.player_token, (self.tile_size, self.tile_size))

        # Initialize grid with random elements
        self.grid = [[random.choice([0, 1, 2, 3]) for _ in range(self.grid_width)] for _ in range(self.grid_height)]

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
                tile_type = self.grid[row][col]  # Get the type of tile to render

                # Determine which tile to use based on the grid value
                if tile_type == 0:
                    tile = self.grass_tile
                elif tile_type == 1:
                    tile = self.water_tile
                elif tile_type == 2:
                    tile = self.stone_tile
                elif tile_type == 3:
                    tile = self.longgrass_tile
                else:
                    tile = self.grass_tile  # Default to grass_tile

                # Render the tile on the screen
                screen.blit(tile, (col * self.tile_size, row * self.tile_size))

                # Draw the player
                screen.blit(self.player_token,
                            (self.player_pos[0] * self.tile_size, self.player_pos[1] * self.tile_size))

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