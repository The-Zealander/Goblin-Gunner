import sys
import pygame

# Initialize Pygame
pygame.init()

# define resolution
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Define the fonts to be used
title_font = pygame.font.SysFont("Arial", 90)  # Font for title
general_font = pygame.font.SysFont("Arial", 50)  # General font
small_font = pygame.font.SysFont("Arial", 25)  # Small font
version_font = pygame.font.SysFont("Arial", 12)  # Font for version info

# other shit
game_name = "Goblin Gunner"

# SOunds
BUTTON_CLICK_SOUND = "Button_sound.mp3"  # Make sure this file exists in your project directory


def resolution():
    return SCREEN_WIDTH, SCREEN_HEIGHT


def version_keys():
    program_state = "Aplha"
    program_version = "0.3"
    Menu_Version = "0.2"
    Settings_Version = "0.0"
    Gameplay_Version = "0.0"
    Title_Version = "0.5"
    return program_state, program_version, Menu_Version, Settings_Version, Gameplay_Version, Title_Version


# Set colors
def define_colors():
    colors = {
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
        "AQUA": (0, 255, 255)
    }
    return colors
