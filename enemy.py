from random import randint
from defines import *


class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, small_enemey_size, small_enemey_size)
        self.speed = enemy_speed
        self.attack_range = 100
        self.health = 100
        self.attack_damage = 10
        self.state = "wander"  # Initial state
        self.target = None  # Target player object
        self.last_attack_time = 0  # Time tracking for attack cooldown

    def update(self, dt, player_position):
        if self.state == "wander":
            # Wander behavior
            self.wander()
            # Check if player is within attack range
            if self.can_attack_player(player_position):
                self.state = "attack"  # Switch to attack state

        elif self.state == "attack":
            # Attack behavior
            self.attack(player_position)
            # Check if player is no longer within attack range
            if not self.can_attack_player(player_position):
                self.state = "wander"  # Switch back to wander state

    def wander(self):
        # Randomly move the enemy
        direction = randint(0, 3)  # 0: up, 1: down, 2: left, 3: right
        if direction == 0:
            self.rect.y -= self.speed
        elif direction == 1:
            self.rect.y += self.speed
        elif direction == 2:
            self.rect.x -= self.speed
        elif direction == 3:
            self.rect.x += self.speed

    def attack(self, player_position):
        # Perform attack action
        # Implement either ranged or melee attack based on enemy type
        # For example:
        # if self.attack_type == "ranged":
        #     self.ranged_attack(player_position)
        # elif self.attack_type == "melee":
        #     self.melee_attack(player_position)
        pass

    def can_attack_player(self, player_position):
        # Check if the player is within attack range
        distance_squared = (player_position[0] - self.rect.x) ** 2 + (player_position[1] - self.rect.y) ** 2
        return distance_squared <= self.attack_range ** 2

    def draw(self, screen):
        # Draw the enemy on the screen
        pygame.draw.rect(screen, red, self.rect)
