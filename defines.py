import pygame

# Initialize Pygame
pygame.init()

# Define resolutions
RESOLUTIONS = {
    "HD": {"width": 1280, "height": 720},  # 720p
    "FHD": {"width": 1920, "height": 1080},  # 1080p
    "UHD": {"width": 2560, "height": 1440},  # 2K Resolution
}

# Default resolution (can be changed based on user preference)
DEFAULT_RESOLUTION = RESOLUTIONS["HD"]  # Set to 1280x720 by default

# Define fonts
TITLE_FONT = pygame.font.SysFont("Arial", 90)  # Font for titles
GENERAL_FONT = pygame.font.SysFont("Arial", 50)  # General font
SMALL_FONT = pygame.font.SysFont("Arial", 25)  # Smaller font
VERSION_FONT = pygame.font.SysFont("Arial", 12)  # Font for version info

# Game name
GAME_NAME = "Goblin Gunner"

# Sounds
BUTTON_CLICK_SOUND = "Button_sound.mp3"  # Path to button click sound file


# tile shit
TILE_SIZE = 32  # The size of each tile in pixels

# Define the grid layout
GRID_WIDTH = 36  # Number of tiles horizontally
GRID_HEIGHT = 20  # Number of tiles vertically

# Define screen resolution based on grid size and tile size
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE  # 36 tiles across
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE  # 20 tiles up and down

# Define information panel size
INFO_PANEL_TILES = 3  # Info panel width in tiles
INFO_PANEL_WIDTH = INFO_PANEL_TILES * TILE_SIZE

# Final screen size with the info panel included
TOTAL_SCREEN_WIDTH = SCREEN_WIDTH + INFO_PANEL_WIDTH  # Include the info panel in screen width


# Function to get the current resolution
def get_current_resolution():
    return DEFAULT_RESOLUTION["width"], DEFAULT_RESOLUTION["height"]


# Define program version and state
def get_version_info():
    program_state = "Alpha"
    program_version = "0.3"
    menu_version = "0.2"
    settings_version = "0.0"
    gameplay_version = "0.0"
    title_version = "0.5"
    return {
        "program_state": program_state,
        "program_version": program_version,
        "menu_version": menu_version,
        "settings_version": settings_version,
        "gameplay_version": gameplay_version,
        "title_version": title_version,
    }


# Define common colors
def get_colors():
    return {
        "BLACK": (0, 0, 0),
        "SILVER": (192, 192, 192),
        "GRAY": (128, 128, 128),
        "WHITE": (255, 255, 255),
        "MAROON": (128, 0, 0),
        "RED": (255, 0, 0),
        "GREEN": (0, 128, 0),
        "LIME": (0, 255, 0),
        "OLIVE": (128, 128, 0),
        "YELLOW": (255, 255, 0),
        "NAVY": (0, 0, 128),
        "BLUE": (0, 0, 255),
        "PURPLE": (128, 0, 128),
        "FUCHSIA": (255, 0, 255),
        "TEAL": (0, 128, 128),
        "AQUA": (0, 255, 255),
    }
