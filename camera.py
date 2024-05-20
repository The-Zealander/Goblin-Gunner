import pygame

class Camera:
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)

    def apply(self, entity):
        return entity.rect.move(-self.rect.x, -self.rect.y)

    def update(self, target):
        self.rect.center = target.rect.center
