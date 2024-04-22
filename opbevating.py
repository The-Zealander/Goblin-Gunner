class Play_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE, font_size=30):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.hovered() else self.color, self.rect)
        text_surface = self.font.render(self.text, True, "WHITE")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                self.clicked = True
                print("you clicked start")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


class Settings_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE,
                 font_size=30):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.hovered() else self.color, self.rect)
        text_surface = self.font.render(self.text, True, "WHITE")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                self.clicked = True
                print("you clicked Settings")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


class Unknown_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE,
                 font_size=30):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.hovered() else self.color, self.rect)
        text_surface = self.font.render(self.text, True, "WHITE")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                self.clicked = True
                print("you clicked unknown")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False


class Quit_Button:
    def __init__(self, text, position, size, color=BUTTON_COLOR_INACTIVE, hover_color=BUTTON_COLOR_ACTIVE,
                 font_size=30):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(position, size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.hovered() else self.color, self.rect)
        text_surface = self.font.render(self.text, True, "WHITE")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered():
                self.clicked = True
                print("you clicked quit")
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.hovered():
                self.clicked = False
                return True
            self.clicked = False
        return False