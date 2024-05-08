import pygame
import defines
import player
import enemy
import map
import test_map


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.camera = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.player = player.Player(0,0)  # Assuming the Player class has a position attribute
        self.enemies = [enemy.Enemy(1, 1) for _ in range(5)]  # A list of enemies
        self.map = test_map.TestGameMap(1920, 1080, 32)  # Assuming the Map class handles map rendering

    def update_camera(self):
        """Update the camera's position to center on the player."""
        half_width = self.screen_width // 2
        half_height = self.screen_height // 2
        self.camera.center = self.player.position()  # Center the camera on the player's position

        # Ensure the camera doesn't go out of map bounds
        self.camera.clamp_ip(self.map.get_bounds())  # The map should have a method to get bounds

    def update(self):
        """Update game logic."""
        self.player.update()  # Update player state, like movement
        for enemy in self.enemies:
            enemy.update()  # Update enemy logic

        self.update_camera()  # Update camera position based on the player's location

    def render(self):
        """Render the game with the camera's offset."""
        # Clear the screen with a background color
        self.screen.fill(defines.black)

        # Calculate the camera offset
        camera_offset = (-self.camera.x, -self.camera.y)

        # Render the map, shifted by the camera's position
        self.map.render(self.screen, camera_offset)

        # Render the player with the camera's offset
        self.player.render(self.screen, camera_offset)

        # Render the enemies with the camera's offset
        for enemy in self.enemies:
            enemy.render(self.screen, camera_offset)

    def handle_event(self, event):
        """Handle events like key presses, mouse clicks, etc."""
        self.player.handle_event(event)  # Pass events to the player for interaction
