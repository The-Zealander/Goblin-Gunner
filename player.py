import pygame
import defines

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image
        self.image = pygame.image.load("player_sprite.png").convert_alpha()  # Convert for performance
        self.rect = self.image.get_rect()

        # Set initial position
        self.rect.topleft = (0, 0)  # Top-left corner
        self.speed = 150  # Pixels per second (adjust as needed)

    def update(self, dt, keys):
        # Update the position based on key presses and delta time
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed * dt
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed * dt
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt

        # Ensure the player doesn't go out of bounds
        self.rect.clamp_ip((0, 0, defines.SCREEN_WIDTH, defines.SCREEN_HEIGHT))
