import pygame
import sys
import defines

#Button colors
BUTTON_COLOR_INACTIVE = defines.navy
BUTTON_COLOR_ACTIVE = defines.blue
# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode(defines.resolution)

# Sounds
hit_sound = pygame.mixer.Sound(defines.BUTTON_CLICK_SOUND)

class Button:
    def __init__(self, x, y, color, text):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.selected = False

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 200, 50))
        text_surface = defines.GENERAL_FONT.render(self.text, True, defines.black)
        text_rect = text_surface.get_rect(center=(self.x + 200 // 2, self.y + 50 // 2))
        screen.blit(text_surface, text_rect)

    def play_hit_sound(self):
        hit_sound.play()

    def increase_size(self):
        self.color = defines.green
        pygame.draw.rect(screen, self.color, (self.x - 5, self.y - 5, 200 + 10, 50 + 10))

    def decrease_size(self):
        self.color = defines.red

class Button:
    def __init__(self, text, position, size, font_size=30, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        # Draw button with hover effect
        color = self.hover_color if self.hovered() else self.color
        pygame.draw.rect(screen, color, self.rect)

        # Render text
        text_surface = self.font.render(self.text, True, "WHITE")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def hovered(self):
        # Check if mouse is over the button
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                pygame.mixer.Sound.play(defines.BUTTON_CLICK_SOUND)  # Play sound on click
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True  # Button click action
            self.clicked = False
        return False

# Main loop
selected_button_index = 0
while True:
    screen.fill(defines.white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_button_index = (selected_button_index - 1) % len(buttons)
            elif event.key == pygame.K_DOWN:
                selected_button_index = (selected_button_index + 1) % len(buttons)
            elif event.key == pygame.K_SPACE:
                buttons[selected_button_index].play_hit_sound()

    for i, button in enumerate(buttons):
        if i == selected_button_index:
            button.increase_size()
        else:
            button.decrease_size()
        button.draw()

    pygame.display.flip()
