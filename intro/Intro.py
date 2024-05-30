import pygame
import time
import defines


class IntroSequence:
    def __init__(self, sequence, audio_path):
        self.sequence = sequence  # List of dictionaries with type: 'image' or 'video' and path
        self.audio_path = audio_path  # Path to the voice-over audio file
        self.current_index = 0
        self.start_time = time.time()
        self.display_time = 2  # Display each image for 2 seconds
        self.voiceover = None
        self.audio_started = False
        self.skip_pressed = False

    def start_audio(self):
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.play()

    def load_voiceover(self):
        self.voiceover = pygame.mixer.Sound(self.audio_path)
        self.voiceover.play()

    def update(self):
        if not self.audio_started:
            self.start_audio()
            self.load_voiceover()
            self.audio_started = True

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            self.skip_pressed = True

        if self.skip_pressed or self.current_index >= len(self.sequence):
            return

        current_time = time.time()
        if current_time - self.start_time >= self.display_time:
            self.current_index += 1
            self.start_time = current_time

    def draw(self, screen):
        screen.fill(defines.black)
        if self.current_index < len(self.sequence):
            item = self.sequence[self.current_index]
            if item['type'] == 'image':
                image = pygame.image.load(item['path']).convert()
                screen.blit(image, (0, 0))
            elif item['type'] == 'video':
                # You'll need to implement video playback here
                pass

    def is_finished(self):
        return self.current_index >= len(self.sequence)


# Example usage:
pygame.init()
screen = pygame.display.set_mode(defines.resolution)
clock = pygame.time.Clock()

# Define the intro sequence
sequence = [
    {'type': 'video', 'path': 'intro/The_amethyst_wizard_sword.mp4'},
    {'type': 'image', 'path': 'intro/Amethyst_mage_power.jpg'},
    {'type': 'video', 'path': 'intro/Amethyst_tower_normal.mp4'},
    {'type': 'video', 'path': 'intro/Amethyst_tower_corruption.mp4'},
    {'type': 'image', 'path': 'intro/citypeople.jpg'},
    {'type': 'image', 'path': 'intro/abominations.jpg'},
    {'type': 'image', 'path': 'intro/corpse.jpg'},
    {'type': 'image', 'path': 'intro/Serious_jens.jpg'},
    # Add more images or videos as needed
]

# Path to the voice-over audio file
audio_path = 'sounds/Jens the Goblin.mp3'

# Create the intro sequence object
intro = IntroSequence(sequence, audio_path)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    intro.update()
    intro.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    if intro.is_finished():
        break

pygame.quit()
