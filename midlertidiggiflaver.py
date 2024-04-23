from PIL import Image
import pygame
import defines

# Load the GIF
gif_path = "Goblinatcamp.gif"  # Path to your animated GIF file
gif = Image.open(gif_path)

# Extract frames from the GIF and store them in a list
frames = []
frame_count = gif.n_frames  # Number of frames in the GIF

for i in range(frame_count):
    gif.seek(i)  # Move to the ith frame
    frame = gif.copy()  # Copy the frame to avoid altering the original GIF
    frames.append(frame)  # Add the frame to the list

# Convert Pillow frames into Pygame surfaces
pygame_frames = [
    pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
    for frame in frames
]