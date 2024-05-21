from defines import *


class ControlScreen:
    def __init__(self):
        self.font = SMALL_FONT
        self.controls = [
            ("Move Up", "W"),
            ("Move Down", "S"),
            ("Move Left", "A"),
            ("Move Right", "D"),
            ("Sprint", "Left Shift"),
            ("Shoot", "Space"),
            ("Reload", "R"),
            ("Pause", "Esc")
        ]

    def render(self, screen):
        screen.fill(black)
        title_text = self.font.render("Controls", True, white)
        screen.blit(title_text, (resolution[0] // 2 - title_text.get_width() // 2, 50))

        for i, (action, key) in enumerate(self.controls):
            action_text = self.font.render(f"{action}: {key}", True, white)
            screen.blit(action_text, (100, 150 + i * 40))

        # Render "Back" option
        back_text = self.font.render("Press Esc to go back", True, white)
        screen.blit(back_text, (resolution[0] // 2 - back_text.get_width() // 2, resolution[1] - 100))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return "back"
        return None
