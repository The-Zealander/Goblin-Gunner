import pygame
import defines
from titlescreen import TitleScreen
from start_menu import MainMenu
from gametest import The_Game


class Game:
    def __init__(self):
        pygame.init()

        # Setup the display with the current resolution
        self.screen = pygame.display.set_mode(defines.get_current_resolution())
        pygame.display.set_caption(defines.GAME_NAME)

        # Try to set an icon for the game window
        try:
            icon = pygame.image.load("images/8bitsword.png").convert_alpha()
            pygame.display.set_icon(icon)
        except FileNotFoundError:
            print("Icon file not found. Skipping.")

        self.current_scene = TitleScreen()  # Start with the title screen
        self.running = True

        # Frame rate control
        self.clock = pygame.time.Clock()  # Clock to track delta time

    def change_scene(self, scene_name):
        if scene_name == "quit":
            self.running = False
        elif scene_name == "main_menu":
            self.current_scene = MainMenu()  # Transition to the main menu
        elif scene_name == "start_game":
            self.current_scene = The_Game()  # Start the game

    def run(self):
        while self.running:
            events = pygame.event.get()  # Get all events
            next_scene = self.current_scene.handle_events(events)  # Handle scene events

            # Change scene based on the returned value
            self.change_scene(next_scene)

            # Update and render the current scene
            self.current_scene.update()  # Pass delta time to the scene
            self.current_scene.render(self.screen)  # Render the scene

            # Update the display
            pygame.display.flip()

        pygame.quit()  # Cleanup when exiting the loop


if __name__ == "__main__":
    game = Game()  # Create and initialize the game
    game.run()  # Start the game loop
