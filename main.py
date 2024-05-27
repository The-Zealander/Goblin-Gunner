import pygame
import sys
from game_files.player import Player
from game_files.enemy import Enemy
from game_files.game import Game
from titlescreen import TitleScreen
from start_menu import MainMenu
from controls import ControlScreen
import defines

# Define game states
TITLE_SCREEN = 0
INTRO_VIDEO = 1
MENU_SCREEN = 2
GAME_SCREEN = 3
CONTROLS_SCREEN = 4

# Initialize pygame and set up the display
pygame.init()
screen = pygame.display.set_mode(defines.resolution)
pygame.display.set_caption(defines.GAME_NAME)
clock = pygame.time.Clock()

# Initialize the mixer for audio
pygame.mixer.init()

# Game state and main loop flag
game_state = TITLE_SCREEN
running = True

# Create instances of different screens and game components
title_screen = TitleScreen()

menu = MainMenu()
game = Game()
controls_screen = ControlScreen()

# Load music
intro_music = "sounds/Jens the Goblin.mp3"
game_music = "sounds/Pixelated Adventure.mp3"
pygame.mixer.music.set_volume(0.5)


# Function to play music based on game state
def play_music(track):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)


# Play the intro music at the start
play_music(intro_music)

# Main game loop
while running:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()

        if game_state == TITLE_SCREEN:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = MENU_SCREEN


        elif game_state == MENU_SCREEN:
            action = menu.handle_event(event)
            if action == "quit":
                running = False
            elif action == "start_game":
                game_state = GAME_SCREEN
                play_music(game_music)
            elif action == "open_controls":
                game_state = CONTROLS_SCREEN

        elif game_state == CONTROLS_SCREEN:
            action = controls_screen.handle_event(event)
            if action == "back":
                game_state = MENU_SCREEN

        elif game_state == GAME_SCREEN:
            game.handle_events(keys)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = MENU_SCREEN
                play_music(intro_music)

    if game_state == TITLE_SCREEN:
        title_screen.render(screen)
    elif game_state == MENU_SCREEN:
        menu.render(screen)
    elif game_state == CONTROLS_SCREEN:
        controls_screen.render(screen)
    elif game_state == GAME_SCREEN:
        game.update(dt, keys)
        game.render(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
