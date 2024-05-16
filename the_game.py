import pygame
from player import Player  # Assuming the Player class is defined in a separate file
from enemy import Enemy
from map import GameMap
from camera import Camera
import defines


class Game:
    def __init__(self):
        self.camera = None
        self.player = None
        self.enemies = []
        self.game_map = None
        self.initialize()

    def initialize(self):
        self.camera = Camera(defines.resolution[0], defines.resolution[1])
        self.player = Player(0, 0)  # Assuming the Player class has a position attribute
        self.enemies = [Enemy(100, 100) for _ in range(5)]  # A list of enemies
        self.game_map = GameMap(1920, 1080, 32)  # Assuming the GameMap class handles map rendering

    def update(self, dt):
        """Update game logic."""
        player_position = self.player.position()  # Get the current position of the player
        self.player.update(dt, player_position)  # Update player state, like movement

        for enemy in self.enemies:
            enemy.update(dt, player_position)  # Update enemy logic

        self.camera.update(self.player.rect.center)  # Update camera position based on the player's location

    def render(self, screen):
        """Render the game with the camera's offset."""
        # Clear the screen with a background color
        screen.fill(defines.black)

        # Render the map, shifted by the camera's position
        self.game_map.draw(screen, self.camera)

        # Render the player with the camera's offset
        self.player.draw(screen, self.camera)


    def handle_events(self):
        """Handle keyboard events to move the player."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move_up()
                elif event.key == pygame.K_s:
                    self.player.move_down()
                elif event.key == pygame.K_a:
                    self.player.move_left()
                elif event.key == pygame.K_d:
                    self.player.move_right()
