import pygame
from itertools import cycle
import math
import defines
from utilities import Bullet
import random


def load_frames(frame_names):
    frames = []
    for name in frame_names:
        try:
            image = pygame.image.load(f"sprites/player_walking/{name}").convert_alpha()
            frames.append(image)
        except pygame.error as e:
            print(f"Error loading {name}: {e}")
            raise
    return frames


class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.speed = 200  # Speed in pixels per second

        down_frames = load_frames(["goblin_walk_down_{}.png".format(i) for i in range(1, 7)])
        up_frames = load_frames(["goblin_walk_up_{}.png".format(i) for i in range(1, 7)])
        left_frames = load_frames(["goblin_walk_left_{}.png".format(i) for i in range(1, 7)])
        right_frames = load_frames(["goblin_walk_right_{}.png".format(i) for i in range(1, 7)])

        self.animations = {
            Direction.DOWN: cycle(down_frames),
            Direction.UP: cycle(up_frames),
            Direction.LEFT: cycle(left_frames),
            Direction.RIGHT: cycle(right_frames),
        }

        self.current_animation = Direction.DOWN
        self.current_cycle = self.animations[self.current_animation]
        self.current_frame = next(self.current_cycle)
        self.animation_speed = 0.5
        self.last_frame_time = 0
        self.direction = pygame.Vector2(0, 0)
        self.last_shot_time = 0
        self.shot_cooldown = 500  # milliseconds
        self.ammo = 10
        self.max_ammo = 10
        self.health = 100
        self.max_health = 100

    def update(self, keys, dt):
        self.direction = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.current_animation = Direction.UP
        if keys[pygame.K_s]:
            self.direction.y = 1
            self.current_animation = Direction.DOWN
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.current_animation = Direction.LEFT
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.current_animation = Direction.RIGHT

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()  # Normalize the vector to ensure consistent speed
            self.rect.x += self.direction.x * self.speed * dt
            self.rect.y += self.direction.y * self.speed * dt

        now = pygame.time.get_ticks()
        if now - self.last_frame_time > self.animation_speed * 1000:
            self.current_frame = next(self.current_cycle)
            self.last_frame_time = now

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > self.shot_cooldown and self.ammo > 0:
            self.last_shot_time = now
            self.ammo -= 1
            bullets = []
            defines.Shotguncoking_sound()
            for _ in range(5):
                angle_offset = random.uniform(-10, 10)  # Random offset between -5 and 5 degrees
                angle = math.atan2(self.direction.y, self.direction.x) + math.radians(angle_offset)
                bullet = Bullet(self.rect.centerx, self.rect.centery, angle)
                bullets.append(bullet)
            return bullets
        return None

    def draw(self, screen, camera):
        screen.blit(self.current_frame, camera.apply(self))
