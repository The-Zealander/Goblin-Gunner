import pygame
from itertools import cycle
from terrain import TILE_PROPERTIES, TileType

P_HP = 100


def load_frames(frame_names):
    frames = []
    for name in frame_names:
        try:
            image = pygame.image.load(f"Goblin_sprites_walking/player_walking/{name}").convert_alpha()
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
        self.animation_speed = 0.09
        self.last_frame_time = 0

    def move(self, direction, dt, game_map):
        if direction != self.current_animation:
            self.current_animation = direction
            self.current_cycle = self.animations[direction]
            self.current_frame = next(self.current_cycle)

        self.last_frame_time += dt
        if self.last_frame_time >= self.animation_speed:
            self.current_frame = next(self.current_cycle)
            self.last_frame_time = 0

        dx, dy = 0, 0
        if direction == Direction.LEFT:
            dx = -5
        elif direction == Direction.RIGHT:
            dx = 5
        elif direction == Direction.UP:
            dy = -5
        elif direction == Direction.DOWN:
            dy = 5

        next_rect = self.rect.move(dx, dy)
        tile_x, tile_y = next_rect.x // game_map.tile_size, next_rect.y // game_map.tile_size

        if game_map.is_walkable(tile_x, tile_y):
            speed_modifier = TILE_PROPERTIES[game_map.tiles[tile_y][tile_x]]["speed_modifier"]
            self.rect.x += dx * speed_modifier
            self.rect.y += dy * speed_modifier

    def draw(self, screen, camera):
        screen.blit(self.current_frame, (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y))

    def update(self):
        pass
