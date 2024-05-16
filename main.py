import pygame
import sys
import defines
from player import Player
from the_game import Game  # The class that contains the game logic
from titlescreen import TitleScreen  # The title screen
from start_menu import MainMenu  # The menu screen

# Game States
TITLE_SCREEN = 0
MENU_SCREEN = 1
GAME_SCREEN = 2

# Initialize pygame and set up the display
pygame.init()
screen = pygame.display.set_mode(defines.resolution)
pygame.display.set_caption(defines.GAME_NAME)
clock = pygame.time.Clock()

# Game state and main loop flag
game_state = TITLE_SCREEN
running = True

# Create instances of different screens and game components
title_screen = TitleScreen()  # Assuming TitleScreen has a render method
menu = MainMenu()  # Assuming Menu has a render method
game = Game()  # This is your game class with the camera system

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game when the quit event is triggered

        if game_state == TITLE_SCREEN:
            # Transition to menu if a specific key is pressed, like SPACE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = MENU_SCREEN

        elif game_state == MENU_SCREEN:
            # Transition to game if a key is pressed
            action = menu.handle_event(event)
            if action == "quit":
                running = False
            elif action == "start_game":
                game_state = GAME_SCREEN
            elif action == "open_settings":
                print("ingenting")


        elif game_state == GAME_SCREEN:
            game.handle_events()  # Pass events to the game
            # Return to menu with ESC
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = MENU_SCREEN

    # Rendering and updating based on the game state
    if game_state == TITLE_SCREEN:
        title_screen.render(screen)  # Render the title screen

    elif game_state == MENU_SCREEN:
        menu.render(screen)  # Render the menu

    elif game_state == GAME_SCREEN:
        game.update(defines.FPS)  # Update game logic
        game.render(screen)  # Render the game elements with the camera

    # Update the display
    pygame.display.flip()

# Clean up when exiting the game loop
pygame.quit()
sys.exit()
