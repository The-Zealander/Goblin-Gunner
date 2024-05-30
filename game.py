import pygame
from player import Player
from enemy import Enemy
from utilities import Bullet
from map import GameMap
from camera import Camera
from defines import *

SCREEN_WIDTH = resolution[0]
SCREEN_HEIGHT = resolution[1]


class Game:
    def __init__(self):
        # Initialize game objects
        self.game_map = GameMap()
        self.player = Player((map_width * map_tile_size) // 2, (map_height * map_tile_size) // 2)
        self.enemies = [Enemy(100, 100)]
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.bullets = []

    def update(self, dt, keys):
        # Update game logic
        self.player.update(keys, dt)
        for bullet in self.bullets:
            bullet.update(dt)
        for enemy in self.enemies:
            enemy.update(self.player.rect, dt)
        self.camera.update(self.player)
        for enemy in self.enemies:
            enemy.update(self.player.rect, dt)
            self.player.take_damage(20)


    def render(self, screen):
        # Fill the screen with black to avoid artifacts
        screen.fill(black)

        self.game_map.draw(screen, self.camera)
        for enemy in self.enemies:
            pygame.draw.rect(screen, red, self.camera.apply(enemy))
        for bullet in self.bullets:
            pygame.draw.rect(screen, white, self.camera.apply(bullet))
        self.player.draw(screen, self.camera)

    def handle_events(self, keys):
        # Handle shooting
        if keys[pygame.K_SPACE]:
            new_bullets = self.player.shoot()
            if new_bullets:
                self.bullets.extend(new_bullets)
