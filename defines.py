import pygame

# Initialize the Pygame library, which is used for creating video games
pygame.init()

# Define the resolution of the game window
resolution = (1920, 1080)
FPS = 60  # Frames Per Second, which controls the game's speed

# Font settings
# Define the path to the pixel font file
pixelfont = 'fonts/PixeloidSans-mLxMm.ttf'

# Define different font sizes for various game elements
TITLE_FONT = pygame.font.Font(pixelfont, 100)  # Font for titles, such as the game title
MENU_FONT = pygame.font.Font(pixelfont, 75)  # Font for menu items
GENERAL_FONT = pygame.font.Font(pixelfont, 50)  # General font for in-game text
SMALL_FONT = pygame.font.Font(pixelfont, 25)  # Smaller font for minor details
VERSION_FONT = pygame.font.Font(pixelfont, 12)  # Font for version information

# Game metadata
GAME_NAME = "Goblin Gunner"  # The title of the game
icon = pygame.image.load('images/goblin_logo.png')  # The game's icon

# Sound effects and music
BUTTON_CLICK_SOUND = "sounds/Button_sound.mp3"  # Sound effect for button clicks
Shotguncoking_sound = "sounds/shotgun-cocking.mp3"  # Sound effect for shotgun cocking
Swing_sound = "sounds/swing_sound.mp3"  # Sound effect for swinging
background_song = "sounds/Pixelated Adventure.mp3"  # Background music for the game
Jens_Song = "sounds/Jens the Goblin.mp3"  # Music for a specific character or level


# Function to retrieve version information
def get_version_info():
    program_state = "Alpha"  # The current state of the game (e.g., Alpha, Beta, Release)
    program_version = "1"  # The version number of the game
    menu_version = "1.1"  # The version number of the menu system
    settings_version = "0.0"  # The version number of the settings system
    gameplay_version = "0.5"  # The version number of the gameplay mechanics
    title_version = "1.5"  # The version number of the title screen
    return {
        "program_state": program_state,
        "program_version": program_version,
        "menu_version": menu_version,
        "settings_version": settings_version,
        "gameplay_version": gameplay_version,
        "title_version": title_version,
    }


# Define common colors used throughout the game
black = (0, 0, 0)  # RGB value for black
silver = (192, 192, 192)  # RGB value for silver
gray = (128, 128, 128)  # RGB value for gray
white = (255, 255, 255)  # RGB value for white
maroon = (128, 0, 0)  # RGB value for maroon
red = (255, 0, 0)  # RGB value for red
green = (0, 128, 0)  # RGB value for green
lime = (0, 255, 0)  # RGB value for lime
olive = (128, 128, 0)  # RGB value for olive
yellow = (255, 255, 0)  # RGB value for yellow
navy = (0, 0, 128)  # RGB value for navy
blue = (0, 0, 255)  # RGB value for blue
purple = (128, 0, 128)  # RGB value for purple
fuchsia = (255, 0, 255)  # RGB value for fuchsia
teal = (0, 128, 128)  # RGB value for teal
aqua = (0, 255, 255)  # RGB value for aqua
brown = (101, 67, 33)  # RGB value for brown

# Define various game constants
detec_rad = 10  # Detection radius for enemies or other game objects
enemy_speed = 1  # Speed of regular enemies
big_enemy_speed = 1  # Speed of larger or more powerful enemies
player_speed = 5  # Speed of the player character
b_speed = 100  # Speed of bullets or projectiles
map_width = 100  # Width of the game map
map_height = 100  # Height of the game map
test_map_width = 50  # Width of the test map
test_map_height = 50  # Height of the test map
map_tile_size = 32  # Size of individual map tiles
player_size = 32  # Size of the player character
small_enemey_size = 32  # Size of regular enemies
big_enemy_size = 128  # Size of larger or more powerful enemies
enemy_melee_range = 5  # Range of melee attacks for enemies
enemy_long_range = 100  # Range of long-range attacks for enemies
INVINCIBILITY_DURATION = 1  # Duration of invincibili
