import pygame
import moviepy.editor as mpy
import defines


class MainMenu:
    def __init__(self):
        self.font = defines.MENU_FONT
        self.options = ["Start Game", "Settings", "Quit"]
        self.selected_option = 0

        # Load and prepare video
        self.video = mpy.VideoFileClip("images/Jensgoblinidle.mp4")

        self.video_surface = pygame.Surface((self.video.size[0], self.video.size[1]))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_s:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.options[self.selected_option] == "Start Game":
                    return "start_game"
                elif self.options[self.selected_option] == "Settings":
                    return "open_settings"
                elif self.options[self.selected_option] == "Quit":
                    return "quit"
        return None

    def render(self, screen):
        # Fill the screen with black to avoid artifacts
        screen.fill("BLACK")
        # Play the video
        t = (pygame.time.get_ticks() / 1000.0) % self.video.duration
        frame = self.video.get_frame(t)
        pygame.surfarray.blit_array(self.video_surface, frame.swapaxes(0, 1)[:, :, :3])
        screen.blit(pygame.transform.scale(self.video_surface, screen.get_size()), (0, 0))

        # Render menu options
        for i, option in enumerate(self.options):
            color = (defines.white) if i == self.selected_option else (defines.green)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(1350, 400 + i * 75))
            screen.blit(text, text_rect)
