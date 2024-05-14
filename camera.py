class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, player_position):
        player_center_x, player_center_y = player_position
        self.offset_x = player_center_x - self.width // 2
        self.offset_y = player_center_y - self.height // 2
