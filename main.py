import pygame
import defines
from titlescreen import TitleScreen
from start_menu import MainMenu
from gametest import The_Game

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((defines.SCREEN_WIDTH,defines.SCREEN_HEIGHT))
        pygame.display.set_caption(defines.game_name)
        try:
            icon = pygame.image.load("8bitsword.png")
            pygame.display.set_icon(icon)
        except FileNotFoundError:
            print("Icon file not found. Skipping.")
        self.current_scene = TitleScreen()  # Start with the title screen
        self.running = True

    def run(self):
        while self.running:
            events = pygame.event.get()

            # Handle events
            next_scene = self.current_scene.handle_events(events)
            if next_scene == "quit":
                self.running = False
            elif next_scene == "main_menu":
                self.current_scene = MainMenu()  # Transition to the main menu
            elif next_scene == "start_game":
                self.current_scene = The_Game()

            # Update and render the current scene
            self.current_scene.update()
            self.current_scene.render(self.screen)
            pygame.display.flip()  # Update the display

            pygame.time.delay(30)  # Control the game's frame rate

        pygame.quit()


if __name__ == "__main__":
    game = Game()  # Create and run the game
    game.run()  # Start the game loop
