class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, player):
        self.offset_x = player.rect.centerx - self.width // 2
        self.offset_y = player.rect.centery - self.height // 2
