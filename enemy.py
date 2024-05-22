import pygame

# Define constants for enemy speed and health
ENEMY_SPEED = 1
ENEMY_HEALTH = 100


# Define a class to represent an enemy in the game
class Enemy:
    def __init__(self, x, y):
        # Initialize the enemy's rectangle with the given x and y coordinates, and a size of 32x32
        self.rect = pygame.Rect(x, y, 32, 32)
        # Set the enemy's speed to the defined constant
        self.speed = ENEMY_SPEED
        # Set the enemy's health to the defined constant
        self.health = ENEMY_HEALTH

    # Method to update the enemy's position based on the player's position
    def update(self, player_rect):
        # Calculate the difference in x and y coordinates between the enemy and the player
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        # Calculate the distance between the enemy and the player, ensuring a minimum distance of 1
        distance = max(1, abs(dx) + abs(dy))
        # Normalize the dx and dy values by dividing by the distance
        dx /= distance
        dy /= distance
        # Update the enemy's x and y coordinates based on the normalized dx and dy values and the enemy's speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    # Method to apply damage to the enemy
    def take_damage(self, damage):
        # Subtract the damage from the enemy's health
        self.health -= damage
        # If the enemy's health is less than or equal to 0, set it to 0
        if self.health <= 0:
            self.health = 0
