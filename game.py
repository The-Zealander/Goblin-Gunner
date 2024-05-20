import pygame
from player import Player
from enemy import Enemy
from utilities import Bullet
from map import GameMap
from camera import Camera
from defines import *
from terrain import TileType

# music
pygame.mixer.music.load(background_song)  # Start the song jackass.
pygame.mixer.music.set_volume(0.5)  # Adjust volume
pygame.mixer.music.play(-1)  # Play in a loop

# sound effects
shotguncock = pygame.mixer.Sound(Shotguncoking_sound)
# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BULLET_DAMAGE = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Create game objects
game_map = GameMap()
player = Player((map_width * map_tile_size) // 2, (map_height * map_tile_size) // 2)
enemies = [Enemy(100, 100), Enemy(200, 200)]
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
bullets = []



# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    dt = clock.tick(60) / 1000.0  # Amount of seconds between each loop

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_tile_type = TileType.GRASS
            elif event.key == pygame.K_2:
                selected_tile_type = TileType.WATER
            elif event.key == pygame.K_3:
                selected_tile_type = TileType.TREE
            elif event.key == pygame.K_4:
                selected_tile_type = TileType.WALL

    # Update game objects
    player.update(keys, dt)
    for bullet in bullets:
        bullet.update(dt)
    for enemy in enemies:
        enemy.update(player.rect)
    camera.update(player)

    # Handle shooting
    if keys[pygame.K_SPACE]:
        shotguncock.play()
        new_bullets = player.shoot()
        if new_bullets:
            bullets.extend(new_bullets)

    # Check collisions
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                enemy.take_damage(BULLET_DAMAGE)
                bullets.remove(bullet)
                break

    # Draw everything
    game_map.draw(screen, camera)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), camera.apply(enemy))
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), camera.apply(bullet))
    player.draw(screen, camera)

    pygame.display.flip()

pygame.quit()
