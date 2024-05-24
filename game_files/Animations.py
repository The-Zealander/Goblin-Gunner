import pygame
from itertools import cycle


class PlayerAnimation:
    def __init__(self, image_paths, frame_duration):
        self.frames = [pygame.image.load(path) for path in image_paths]
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.time_accumulator = 0

    def update(self, dt):
        self.time_accumulator += dt
        if self.time_accumulator >= self.frame_duration:
            self.time_accumulator -= self.frame_duration
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_current_frame(self):
        return self.frames[self.current_frame]


class EnemyAnimation:
    def __init__(self, frame_paths, speed):
        self.frames = self._load_frames(frame_paths)
        self.cycle = cycle(self.frames)  # Cycle through frames
        self.current_frame = next(self.cycle)
        self.animation_speed = speed
        self.last_frame_time = 0

    # Load images from the given paths
    def _load_frames(self, frame_paths):
        frames = []
        for path in frame_paths:
            try:
                image = pygame.image.load(path).convert_alpha()
                frames.append(image)
            except pygame.error as e:
                print(f"Error loading frame {path}: {e}")
                raise
        return frames

    # Get the next frame based on time elapsed
    def update(self, dt):
        self.last_frame_time += dt
        if self.last_frame_time >= self.animation_speed:
            self.current_frame = next(self.cycle)
            self.last_frame_time = 0

    # Get the current frame
    def get_current_frame(self):
        return self.current_frame
