import pygame

# Initialize Pygame
pygame.init()

# Define resolution
resolution = (1920, 1080)
FPS = 60

# Define fonts
TITLE_FONT = pygame.font.SysFont("Arial", 90)  # Font for titles
GENERAL_FONT = pygame.font.SysFont("Arial", 50)  # General font
SMALL_FONT = pygame.font.SysFont("Arial", 25)  # Smaller font
VERSION_FONT = pygame.font.SysFont("Arial", 12)  # Font for version info

# Game name
GAME_NAME = "Goblin Gunner"

# Sounds
BUTTON_CLICK_SOUND = "sounds/Button_sound.mp3"  # Path to button click sound file


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


detec_rad = 10
e_speed = 5
p_speed = 6
b_speed = 1