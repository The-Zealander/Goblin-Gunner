import pygame
from itertools import cycle


# Function to load images from a directory
def load_frames(frame_names):
    frames = []
    for name in frame_names:
        try:
            image = pygame.image.load(f"Goblin_sprites_walking/{name}").convert_alpha()
            frames.append(image)
        except pygame.error as e:
            print(f"Error loading {name}: {e}")
            raise  # Optionally re-raise the error to halt execution
    return frames



class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)  # 32x32 frame size

        # Frame names for each direction
        down_frames = [f"goblin_walk_down_{i}.png" for i in range(1, 7)]  # down_1.png to down_6.png
        up_frames = [f"goblin_walk_up_{i}.png" for i in range(1, 7)]  # up_1.png to up_6.png
        left_frames = [f"goblin_walk_left_{i}.png" for i in range(1, 7)]  # left_1.png to left_6.png
        right_frames = [f"goblin_walk_right_{i}.png" for i in range(1, 7)]  # right_1.png to right_6.png

        # Load frames for each direction
        self.animations = {
            "down": cycle(load_frames(down_frames)),  # Load and cycle frames
            "up": cycle(load_frames(up_frames)),
            "left": cycle(load_frames(left_frames)),
            "right": cycle(load_frames(right_frames)),
        }

        # Default to walking down
        self.current_animation = "down"
        self.current_cycle = self.animations[self.current_animation]
        self.current_frame = next(self.current_cycle)

    def move(self, direction):
        # Change animation based on direction
        if direction != self.current_animation:
            self.current_animation = direction
            self.current_cycle = self.animations[direction]
            self.current_frame = next(self.current_cycle)

    def draw(self, screen, camera):
        # Draw the current frame with respect to the camera's offset
        screen.blit(
            self.current_frame,
            (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y),
        )
