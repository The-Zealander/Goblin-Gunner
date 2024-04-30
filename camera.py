import defines


class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def update(self, target_pos):
        # Center the camera on the target position (like a player)
        self.x = target_pos[0] - self.width // 2
        self.y = target_pos[1] - self.height // 2

        # Ensure the camera doesn't go beyond the map boundaries
        self.x = max(0, min(self.x, defines.map_width * defines.map_tile_size - self.width))
        self.y = max(0, min(self.y, defines.map_height * defines.map_tile_size - self.height))
