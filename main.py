import pygame
import sys

# define resolusion
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
monitor = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def resolusion():
    return SCREEN_WIDTH, SCREEN_HEIGHT


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
