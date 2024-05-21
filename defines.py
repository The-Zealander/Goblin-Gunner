import pygame

# Initialize Pygame
pygame.init()

# Define resolution
resolution = (1920, 1080)
FPS = 60

# Font shit
# Font types
pixelfont = 'fonts/PixeloidSans-mLxMm.ttf'
#pixelfont = 'fonts/Pixelfy.ttf'
# Define fonts
TITLE_FONT = pygame.font.Font(pixelfont, 100)  # Font for titles
MENU_FONT = pygame.font.Font(pixelfont, 75)  # Font for titles
GENERAL_FONT = pygame.font.Font(pixelfont, 50)  # General font
SMALL_FONT = pygame.font.Font(pixelfont, 25)  # Smaller font
VERSION_FONT = pygame.font.Font(pixelfont, 12)  # Font for version info

# Game name
GAME_NAME = "Goblin Gunner"
icon = pygame.image.load('images/goblin_logo.png')

# Sounds
BUTTON_CLICK_SOUND = "sounds/Button_sound.mp3"
Shotguncoking_sound = "sounds/shotgun-cocking.mp3"
background_song = "sounds/Pixelated Adventure.mp3"
Jens_Song = "sounds/Jens the Goblin.mp3"


# Define program version and state
def get_version_info():
    program_state = "Alpha"
    program_version = "1"
    menu_version = "1.1"
    settings_version = "0.0"
    gameplay_version = "0.5"
    title_version = "1.5"
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
brown = (101, 67, 33)

# define various shit
detec_rad = 10
enemy_speed = 1
big_enemy_speed = 1
player_speed = 5
b_speed = 100
map_width = 100
map_height = 100
test_map_width = 50
test_map_height = 50
map_tile_size = 32
player_size = 32
small_enemey_size = 32
big_enemy_size = 128
enemy_melee_range = 5
enemy_long_range = 100
INVINCIBILITY_DURATION = 1  # 1 second invincibility after taking damage
