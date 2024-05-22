import pygame
import math
import random
import player

# Define constants for enemy speed, health, and detection range
ENEMY_SPEED = 1
ENEMY_HEALTH = 100
ENEMY_DETECTION_RANGE = 300  # Pixels
ENEMY_SLAM_COOLDOWN = 3000  # milliseconds
ENEMY_SLAM_DAMAGE = 10
ENEMY_SLAM_PUSHBACK = 96  # 3 tiles assuming each tile is 32x32
ENEMY_SLAM_SLOW_DURATION = 1000  # milliseconds (1 second)
ENEMY_SLAM_RANGE = 100  # The range of the slam attack


class Enemy:
    def __init__(self, x, y):
        # Initialize the enemy's rectangle with the given x and y coordinates, and a size of 32x32
        self.rect = pygame.Rect(x, y, 32, 32)
        self.image = pygame.image.load("assets/enemy images/top-car-view-png-34878.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))  # Scale image to the size of the rect
        self.speed = ENEMY_SPEED
        self.health = ENEMY_HEALTH
        self.angle = 0  # The current angle the enemy is facing
        self.last_slam_time = 0

    def update(self, player_rect, dt):
        # Calculate the difference in x and y coordinates between the enemy and the player
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        # Calculate the distance between the enemy and the player
        distance = math.hypot(dx, dy)

        if distance < ENEMY_DETECTION_RANGE:
            # Normalize the dx and dy values
            if distance > 0:
                dx /= distance
                dy /= distance

            # Rotate the enemy to face the player
            self.angle = math.degrees(math.atan2(-dy, dx))

            # Update the enemy's position to move forward
            self.rect.x += dx * self.speed * dt
            self.rect.y += dy * self.speed * dt

            # Attempt to perform a slam attack
            self.slam_attack(player_rect, distance)

    def take_damage(self, damage):
        # Subtract the damage from the enemy's health
        self.health -= damage
        # If the enemy's health is less than or equal to 0, set it to 0
        if self.health <= 0:
            self.health = 0

    def slam_attack(self, player_rect, distance):
        now = pygame.time.get_ticks()
        if now - self.last_slam_time > ENEMY_SLAM_COOLDOWN and distance <= ENEMY_SLAM_RANGE:
            self.last_slam_time = now
            if self.rect.colliderect(player_rect):
                self.handle_slam_hit(player_rect)

    def handle_slam_hit(self, player_rect):
        # Apply damage to the player (you need to implement player.take_damage() method)
        player.take_damage(ENEMY_SLAM_DAMAGE)

        # Apply pushback (assuming the player has a push_back(dx, dy) method)
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)
        if distance > 0:
            dx /= distance
            dy /= distance
        player.push_back(dx * ENEMY_SLAM_PUSHBACK, dy * ENEMY_SLAM_PUSHBACK)

        # Apply slow effect to the player (assuming the player has a slow(duration) method)
        player.slow(ENEMY_SLAM_SLOW_DURATION)

    def draw(self, screen):
        # Rotate the image to face the player
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, new_rect.topleft)
