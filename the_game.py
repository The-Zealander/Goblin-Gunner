import pygame
import defines
from player import Player
from enemy import Enemy
from map import GameMap
from camera import Camera


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
        self.player.update(dt)  # Update player state, like movement
        for enemy in self.enemies:
            enemy.update(dt,player_pos)  # Update enemy logic

        self.camera.update(self.player.rect.center)  # Update camera position based on the player's location

    def render(self, screen):
        """Render the game with the camera's offset."""
        # Clear the screen with a background color
        screen.fill(defines.black)

        # Render the map, shifted by the camera's position
        self.game_map.render(screen, self.camera)

        # Render the player with the camera's offset
        self.player.render(screen, self.camera)

        # Render the enemies with the camera's offset
        for enemy in self.enemies:
            enemy.render(screen, self.camera)
