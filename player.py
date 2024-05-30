import pygame
from itertools import cycle
import math
import random
from defines import *
from utilities import Bullet

shotguncock = pygame.mixer.Sound(Shotguncoking_sound)
swingsound = pygame.mixer.Sound(Swing_sound)


def load_frames(frame_names):
    frames = []
    for name in frame_names:
        try:
            image = pygame.image.load(f"sprites/player_walking/{name}").convert_alpha()
            scaled_image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
            frames.append(scaled_image)
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
        self.base_speed = 200  # Speed in pixels per second
        self.sprint_multiplier = 2
        self.speed = self.base_speed
        # stamina
        self.max_stamina = 100
        self.stamina = self.max_stamina
        self.stamina_regen_moving = 5
        self.stamina_regen_standing = 25
        self.stamina_sprint_cost = 10
        self.is_sprinting = False
        self.shoot_sound = pygame.mixer.Sound("sounds/gunshot.mp3")
        self.slowed_until = 0

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
        self.animation_speed = 0.1  # Adjust animation speed if necessary
        self.last_frame_time = 0
        self.direction = pygame.Vector2(0, 0)

        # gun stuff
        self.last_shot_time = 0
        self.shot_cooldown = 500  # milliseconds
        self.max_shots = 2
        self.shots_left = self.max_shots
        self.pouch_ammo = 10
        self.reload_time_per_bullet = 1000  # milliseconds (1 second)
        self.reloading = False
        self.reload_start_time = 0

        # melee stuff
        self.melee_cooldown = 250  # milliseconds
        self.last_melee_time = 0
        self.melee_range = 50  # pixels
        self.melee_damage = 15

        # health stuff
        self.health = 100
        self.max_health = 100

        self.font = SMALL_FONT

        # Load UI images
        self.ammo_image = pygame.image.load("assets/Shotgunshell.png").convert_alpha()


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

        if keys[pygame.K_LSHIFT] and self.stamina > 0:
            self.is_sprinting = True
            self.speed = self.base_speed * self.sprint_multiplier
        else:
            self.is_sprinting = False
            self.speed = self.base_speed

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()  # Normalize the vector to ensure consistent speed
            self.rect.x += self.direction.x * self.speed * dt
            self.rect.y += self.direction.y * self.speed * dt

            now = pygame.time.get_ticks()
            if now - self.last_frame_time > self.animation_speed * 1000:
                self.current_cycle = self.animations[self.current_animation]
                self.current_frame = next(self.current_cycle)
                self.last_frame_time = now

            # Regenerate stamina while moving
            if self.is_sprinting:
                self.stamina -= self.stamina_sprint_cost * dt
                if self.stamina < 0:
                    self.stamina = 0
            else:
                self.stamina += self.stamina_regen_moving * dt
                if self.stamina > self.max_stamina:
                    self.stamina = self.max_stamina
        else:
            # Reset to the first frame if not moving
            self.current_cycle = self.animations[self.current_animation]
            self.current_frame = self.current_cycle.__next__()

            # Regenerate stamina faster when standing still
            self.stamina += self.stamina_regen_standing * dt
            if self.stamina > self.max_stamina:
                self.stamina = self.max_stamina

        if keys[pygame.K_r] and not self.reloading and self.shots_left < self.max_shots:
            self.start_reloading()

        if self.reloading:
            self.reload()

        if keys[pygame.K_SPACE]:
            self.melee_attack()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > self.shot_cooldown and self.shots_left > 0:
            self.last_shot_time = now
            self.shots_left -= 1
            bullets = []
            base_angle = math.atan2(self.direction.y, self.direction.x)
            for _ in range(5):
                angle_offset = random.uniform(-5, 5)  # Random offset between -5 and 5 degrees
                angle = base_angle + math.radians(angle_offset)
                bullet = Bullet(self.rect.centerx, self.rect.centery, angle)
                bullets.append(bullet)
            self.shoot_sound.play()
            return bullets
        return None

    def start_reloading(self):
        self.reloading = True
        self.reload_start_time = pygame.time.get_ticks()

    def reload(self):
        now = pygame.time.get_ticks()
        if now - self.reload_start_time >= self.reload_time_per_bullet:
            if self.shots_left < self.max_shots and self.pouch_ammo > 0:
                self.shots_left += 1
                self.pouch_ammo -= 1
                self.reload_start_time = now
                shotguncock.play()
            if self.shots_left == self.max_shots or self.pouch_ammo == 0:
                self.reloading = False

    def melee_attack(self):
        now = pygame.time.get_ticks()
        if now - self.last_melee_time > self.melee_cooldown:
            self.last_melee_time = now
            swingsound.play()
            # Define the melee attack range
            melee_rect = self.rect.inflate(self.melee_range, self.melee_range)
            return melee_rect, self.melee_damage
        return None, 0

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.health)
        if self.health < 0:
            self.health = 0

    def push_back(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def slow(self, duration):
        self.slowed_until = pygame.time.get_ticks() + duration

    def draw(self, screen, camera):
        screen.blit(self.current_frame, camera.apply(self))
        self.draw_health_bar(screen)
        self.draw_ammo(screen)
        self.draw_stamina_bar(screen)

    def draw_health_bar(self, screen):
        # Calculate health bar dimensions
        health_bar_length = 100
        health_bar_height = 20
        health_ratio = self.health / self.max_health
        current_health_length = health_bar_length * health_ratio

        # Position for the health icon and bar
        health_icon_pos = (10, 10)
        health_bar_pos = (50, 10)

        # Draw health icon
        # screen.blit(self.health_image, health_icon_pos)

        # Draw health bar background
        pygame.draw.rect(screen, (255, 0, 0), (*health_bar_pos, health_bar_length, health_bar_height))

        # Draw current health
        pygame.draw.rect(screen, (0, 255, 0), (*health_bar_pos, current_health_length, health_bar_height))

    def draw_ammo(self, screen):
        # Position for the ammo icon and text
        ammo_icon_pos = (10, 40)
        gun_ammo_text_pos = (50, 40)
        pouch_ammo_text_pos = (50, 70)

        # Draw ammo icon
        screen.blit(self.ammo_image, ammo_icon_pos)

        # Draw ammo in gun
        ammo_text = self.font.render(f"Gun: {self.shots_left}/{self.max_shots}", True, (255, 255, 255))
        screen.blit(ammo_text, gun_ammo_text_pos)

        # Draw ammo in pouch
        pouch_text = self.font.render(f"Pouch: {self.pouch_ammo}", True, (255, 255, 255))
        screen.blit(pouch_text, pouch_ammo_text_pos)

    def draw_stamina_bar(self, screen):
        # Calculate stamina bar dimensions
        stamina_bar_length = 100
        stamina_bar_height = 20
        stamina_ratio = self.stamina / self.max_stamina
        current_stamina_length = stamina_bar_length * stamina_ratio

        # Position for the stamina icon and bar
        stamina_icon_pos = (10, 100)
        stamina_bar_pos = (50, 100)

        # Draw stamina icon
        # screen.blit(self.stamina_image, stamina_icon_pos)

        # Draw stamina bar background
        pygame.draw.rect(screen, (0, 0, 0), (*stamina_bar_pos, stamina_bar_length, stamina_bar_height))

        # Draw current stamina
        pygame.draw.rect(screen, (0, 0, 255), (*stamina_bar_pos, current_stamina_length, stamina_bar_height))
