import pygame
from player import Player
from enemy import Enemy
from map import GameMap
from camera import Camera
from defines import *

class Game:
    def __init__(self):
        self.camera = None
        self.player = None
        self.enemies = []
        self.game_map = None
        self.initialize()

    def initialize(self):
        self.camera = Camera(resolution[0], resolution[1])
        self.player = Player(0, 0)
        self.enemies = [Enemy(100 + i * 50, 100 + i * 50) for i in range(5)]
        self.game_map = GameMap('map.txt', 32)

    def update(self, dt):
        player_position = self.player.position()
        self.player.update(dt, player_position)

        for enemy in self.enemies:
            enemy.update(dt, player_position)

        self.camera.update(self.player.rect.center)

    def render(self, screen):
        screen.fill(black)
        self.game_map.draw(screen, self.camera)
        self.player.draw(screen, self.camera)
        #for enemy in self.enemies:
            #senemy.draw(screen, self.camera)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move_up()
        if keys[pygame.K_s]:
            self.player.move_down()
        if keys[pygame.K_a]:
            self.player.move_left()
        if keys[pygame.K_d]:
            self.player.move_right()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

