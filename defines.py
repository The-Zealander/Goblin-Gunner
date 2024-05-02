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
    program_version = "0.35"
    menu_version = "0.2"
    settings_version = "0.0"
    gameplay_version = "0.1"
    title_version = "1"
    return {
        "program_state": program_state,
        "program_version": program_version,
        "menu_version": menu_version,
        "settings_version": settings_version,
        "gameplay_version": gameplay_version,
        "title_version": title_version,
    }


# Define common colors

black = (0, 0, 0)
silver = (192, 192, 192)
gray = (128, 128, 128)
white = (255, 255, 255)
maroon = (128, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)
lime = (0, 255, 0)
olive = (128, 128, 0)
yellow = (255, 255, 0)
navy = (0, 0, 128)
blue = (0, 0, 255)
purple = (128, 0, 128)
fuchsia = (255, 0, 255)
teal = (0, 128, 128)
aqua = (0, 255, 255)
brown =(101,67,33)


detec_rad = 10
e_speed = 1
p_speed = 5
b_speed = 10
map_width = 1920
map_height = 1080
map_tile_size = 32