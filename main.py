import pygame
import sys
import subprocess

# define resolusion
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
monitor = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def version_keys():
    program_state = "Aplha"
    program_version = "0.1"
    Menu_Version = "0.2"
    Settings_Version = "0.0"
    Gameplay_Version = "0.0"
    Title_Version = "0.1"
    return program_state, program_version, Menu_Version, Settings_Version, Gameplay_Version, Title_Version


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


def main():
    #Launch titlescreen:)
    try:
        subprocess.run(["python", "titlescreen.py"])
    except subprocess.CalledProcessError as e:
        print(f"Error launching titlescreen.py: {e}")


if __name__ == "__main__":
    main()
