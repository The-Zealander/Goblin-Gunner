import pygame

ENEMY_SPEED = 2
ENEMY_HEALTH = 100

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.speed = ENEMY_SPEED
        self.health = ENEMY_HEALTH

    def update(self, player_rect):
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        distance = max(1, abs(dx) + abs(dy))
        dx /= distance
        dy /= distance
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
