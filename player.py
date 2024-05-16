import pygame
import time  # This imports the 'time' module
import defines
from Animations import PlayerAnimation
from player_mods import HealthModule
from defines import player_size, player_speed


# Define different movement directions
class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, player_size, player_size)

        # Animation setup for different directions
        self.animations = {
            "down": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_down_{}.png".format(i) for i in range(1, 7)],
                                    0.09),
            "up": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_up_{}.png".format(i) for i in range(1, 7)],
                                  0.09),
            "left": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_left_{}.png".format(i) for i in range(1, 7)],
                                    0.09),
            "right": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_right_{}.png".format(i) for i in range(1, 7)],
                                     0.09),
        }
        self.current_animation = "down"
        self.current_cycle = self.animations[self.current_animation]

        # Health module
        self.health = HealthModule(100)  # Start with 100 health
        self.invincible = False  # Flag for invincibility
        self.invincibility_start = 0  # Start time for invincibility

    # Handle player movement and animation
    def move(self, direction, dt):
        # Change animation if direction changes
        if direction != self.current_animation:
            self.current_animation = direction
            self.current_cycle = self.animations[direction]

        # Update animation
        self.current_cycle.update(dt)

    def take_damage(self, damage):
        if not self.invincible:
            self.health.take_damage(damage)  # Only take damage if not invincible
            self.invincible = True  # Enable invincibility
            self.invincibility_start = time.time()  # Record start time

    def update(self, dt, player_position):
        # Manage invincibility duration
        if self.invincible and (time.time() - self.invincibility_start) > defines.INVINCIBILITY_DURATION:
            self.invincible = False

        # Update animation cycle with the time delta
        self.current_cycle.update(dt)

        # Update player's position based on the provided position
        self.rect.x, self.rect.y = player_position

    def draw(self, screen, camera):

        # If invincible, flash white
        if self.invincible:
            if int(time.time() * 10) % 2 == 0:  # Toggle every 0.1 second for flashing effect
                screen.blit(
                    self.current_cycle.get_current_frame(),
                    (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y),
                )
        else:
            # Drawing a transparent surface to simulate 'invisibility'
            transparent_surface = pygame.Surface((player_size, player_size), pygame.SRCALPHA).convert_alpha()
            transparent_surface.fill((255, 255, 255, 0))  # Making sure it’s completely transparent
            screen.blit(transparent_surface, (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y))

        # Blit the current animation frame
        screen.blit(self.current_cycle.get_current_frame(),
                    (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y))

    def update_position(self, dx, dy):
        self.rect.x += dx * player_speed
        self.rect.y += dy * player_speed

    def position(self):
        """Return the current position of the player."""
        return self.rect.x, self.rect.y
