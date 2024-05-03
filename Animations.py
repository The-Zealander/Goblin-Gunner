import pygame
from itertools import cycle


class PlayerAnimation:
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
