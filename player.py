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


# Define different movement directions
class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)  # 32x32 frame size

        # Load frames for each direction
        down_frames = load_frames(["goblin_walk_down_{}.png".format(i) for i in range(1, 7)])
        up_frames = load_frames(["goblin_walk_up_{}.png".format(i) for i in range(1, 7)])
        left_frames = load_frames(["goblin_walk_left_{}.png".format(i) for i in range(1, 7)])
        right_frames = load_frames(["goblin_walk_right_{}.png".format(i) for i in range(1, 7)])

        self.animations = {
            Direction.DOWN: cycle(down_frames),  # Cycle through frames
            Direction.UP: cycle(up_frames),
            Direction.LEFT: cycle(left_frames),
            Direction.RIGHT: cycle(right_frames),
        }

        self.current_animation = Direction.DOWN  # Default to walking down
        self.current_cycle = self.animations[self.current_animation]
        self.current_frame = next(self.current_cycle)  # Current frame to be drawn
        self.animation_speed = 0.09  # Speed for frame change
        self.last_frame_time = 0  # Time tracking for animation

    def move(self, direction, dt):
        # Change animation if direction changes
        if direction != self.current_animation:
            self.current_animation = direction
            self.current_cycle = self.animations[direction]
            self.current_frame = next(self.current_cycle)  # Reset to the first frame

        # Update the animation based on the speed
        self.last_frame_time += dt
        if self.last_frame_time >= self.animation_speed:
            self.current_frame = next(self.current_cycle)  # Move to the next frame
            self.last_frame_time = 0

    def draw(self, screen, camera):
        # Draw the current frame with respect to the camera's offset
        screen.blit(
            self.current_frame,
            (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y),
        )
