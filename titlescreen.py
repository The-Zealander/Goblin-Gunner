import pygame
import sys
import time
import glob
import subprocess
from defines import resolusion, version_keys

# Initialize Pygame
pygame.init()

# Call functions to get screen resolution and version info
screen_resolusion = resolusion()
program_state, program_version, Menu_Version, Settings_Version, Gameplay_Version, Title_Version = version_keys()

# Define fonts
version_font = pygame.font.SysFont(None, 20)
title_font = pygame.font.SysFont(None, 100)  # Changed font size for title

# Function to draw text on screen
def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Main function
def main():
    # Set up the screen
    screen = pygame.display.set_mode((screen_resolusion[0], screen_resolusion[1]))
    pygame.display.set_caption("TITLESCREEN")
    icon = pygame.image.load("8bitsword.png")
    pygame.display.set_icon(icon)

    # Frame rate control
    clock = pygame.time.Clock()

    # Load GIF frames
    frame_paths = sorted(glob.glob("C:\Users\Zakarias\PycharmProjects\pphehe\Titlescreen image folder"))  # Adjust the path to your frames folder
    frames = [pygame.image.load(frame_path) for frame_path in frame_paths]

    # Animation settings
    frame_index = 0
    frame_duration = 0.1  # Time in seconds for each frame
    last_frame_time = time.time()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Handle Enter key press
                try:
                    result = subprocess.run(["python", "menu_main.py"], check=True, capture_output=True, text=True)
                    print(result.stdout)
                    pygame.quit()
                    sys.exit()
                except subprocess.CalledProcessError as e:
                    print(f"Error launching menu_main.py: {e}")

        # Clear the screen
        screen.fill("BLACK")

        # Draw the title and version info
        draw_text(screen, "G O B L I N   G U N N E R", title_font, "WHITE", screen_resolusion[0] - 710, screen_resolusion[1] - 550)
        draw_text(screen, f"Game Version: {program_state} {Title_Version}", version_font, "WHITE", 15, screen_resolusion[1] - 50)

        # Get the current time
        current_time = time.time()

        # Update frame if enough time has passed
        if current_time - last_frame_time > frame_duration:
            frame_index = (frame_index + 1) % len(frames)
            last_frame_time = current_time

        # Draw the current frame
        screen.blit(frames[frame_index], (0, 0))

        # Update the display
        pygame.display.flip()

        # Control frame rate
        clock.tick(30)  # Limit to 30 FPS

    # Quit pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
