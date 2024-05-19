import pygame
import defines
from map import GameMap
from player import Player
from enemy import Enemy
import random


class Camera:
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.offset_x = 0
        self.offset_y = 0

    def apply(self, entity):
        return entity.rect.move(self.offset_x, self.offset_y)

    def update(self, target):
        self.rect = target.rect
        self.offset_x = -self.rect.centerx + int(self.rect.width / 2)
        self.offset_y = -self.rect.centery + int(self.rect.height / 2)


class Game:
    def __init__(self):
        self.map = GameMap(30, 20, 32)
        self.player = Player(100, 100)
        self.enemies = [Enemy(random.randint(0, defines.map_width), random.randint(0, defines.map_height), 32) for _ in range(5)]  # Create 5 enemies
        self.camera = Camera(800, 600)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left", pygame.time.get_ticks(), self.map)
        if keys[pygame.K_RIGHT]:
            self.player.move("right", pygame.time.get_ticks(), self.map)
        if keys[pygame.K_UP]:
            self.player.move("up", pygame.time.get_ticks(), self.map)
        if keys[pygame.K_DOWN]:
            self.player.move("down", pygame.time.get_ticks(), self.map)

    def update(self, fps):
        self.player.update()
        for enemy in self.enemies:
            enemy.update(fps, (self.player.rect.x, self.player.rect.y))  # Pass delta time and player position
        self.camera.update(self.player)

    def render(self, screen):
        self.map.draw(screen, self.camera)
        self.player.draw(screen, self.camera)
        for enemy in self.enemies:
            enemy.draw(screen, self.camera)