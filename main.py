import pygame  # Import the pygame library for game development
import sys  # Import the sys module for system-specific functions
import defines  # Import the defines module for game constants

# Import game components
from game_files.game import Game  # Import the Game class that contains the game logic
from titlescreen import TitleScreen  # Import the TitleScreen class
from start_menu import MainMenu  # Import the MainMenu class
from controls import ControlScreen  # Import the ControlScreen class

# Define game states
TITLE_SCREEN = 0  # Constant for the title screen state
MENU_SCREEN = 1  # Constant for the menu screen state
GAME_SCREEN = 2  # Constant for the game screen state
CONTROLS_SCREEN = 3  # Constant for the controls screen state

# Initialize pygame and set up the display
pygame.init()  # Initialize the pygame library
screen = pygame.display.set_mode(defines.resolution)  # Set the screen resolution
pygame.display.set_caption(defines.GAME_NAME)  # Set the game window title
clock = pygame.time.Clock()  # Create a clock object for managing frame rate

# Load music
intro_music = "sounds/Jens the Goblin.mp3"
game_music = "sounds/Pixelated Adventure.mp3"

pygame.mixer.music.set_volume(0.5)  # Set the volume (optional)


# Function to play music based on game state
def play_music(track):
    if pygame.mixer.music.get_busy():  # If music is already playing, stop it first
        pygame.mixer.music.stop()
    pygame.mixer.music.load(track)  # Load the appropriate music track
    pygame.mixer.music.play(-1)  # Play the music in a loop (use -1 for infinite loop)


# Game state and main loop flag
game_state = TITLE_SCREEN  # Initialize the game state to the title screen
running = True  # Flag to indicate whether the game is running

# Create instances of different screens and game components
title_screen = TitleScreen()  # Create an instance of the TitleScreen class
menu = MainMenu()  # Create an instance of the MainMenu class
game = Game()  # Create an instance of the Game class
controls_screen = ControlScreen()  # Create an instance of the ControlScreen class

# Play the intro music at the start
play_music(intro_music)

# Main game loop
while running:
    dt = clock.tick(60) / 1000.0  # Calculate the time delta (dt) in seconds
    for event in pygame.event.get():  # Handle events (e.g., keyboard input, mouse clicks)
        if event.type == pygame.QUIT:  # Check for the quit event
            running = False  # Exit the game when the quit event is triggered
        keys = pygame.key.get_pressed()  # Get the current state of the keyboard

        # Handle events based on the current game state
        if game_state == TITLE_SCREEN:
            # Transition to menu if a specific key is pressed, like SPACE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = MENU_SCREEN

        elif game_state == MENU_SCREEN:
            # Handle menu events
            action = menu.handle_event(event)  # Let the menu handle the event
            if action == "quit":
                running = False  # Exit the game if the quit action is triggered
            elif action == "start_game":
                game_state = GAME_SCREEN  # Transition to the game screen
                play_music(game_music)  # Play game music when transitioning to the game screen
            elif action == "open_controls":
                game_state = CONTROLS_SCREEN  # Transition to the controls screen

        elif game_state == CONTROLS_SCREEN:
            # Handle controls screen events
            action = controls_screen.handle_event(event)  # Let the controls screen handle the event
            if action == "back":
                game_state = MENU_SCREEN  # Transition back to the menu screen

        elif game_state == GAME_SCREEN:
            game.handle_events(keys)  # Pass events to the game
            # Return to menu with ESC
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = MENU_SCREEN
                play_music(intro_music)  # Play intro music when transitioning back to the menu screen

    # Rendering and updating based on the game state
    if game_state == TITLE_SCREEN:
        title_screen.render(screen)  # Render the title screen

    elif game_state == MENU_SCREEN:
        menu.render(screen)  # Render the menu

    elif game_state == CONTROLS_SCREEN:
        controls_screen.render(screen)  # Render the controls screen

    elif game_state == GAME_SCREEN:
        game.handle_events(keys)  # Pass events to the game
        game.update(dt, keys)  # Update game logic
        game.render(screen)  # Render the game elements with the camera

    # Update the display
    pygame.display.flip()  # Update the entire display window

# Clean up when exiting the game loop
pygame.quit()  # Quit the pygame library
sys.exit()  # Exit the program
