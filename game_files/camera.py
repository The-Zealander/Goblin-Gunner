import pygame


# Define a Camera class that will be used to manage the game camera.
class Camera:
    # Initialize the camera with a specified width and height.
    def __init__(self, width, height):
        # Create a rectangle (self.rect) with the specified width and height,
        # positioned at the origin (0, 0) of the game world.
        self.rect = pygame.Rect(0, 0, width, height)

    # Apply the camera's position to an entity (e.g., a game object) to get its
    # position relative to the camera.
    def apply(self, entity):
        # Move the entity's rectangle by the negative of the camera's position,
        # effectively offsetting the entity's position by the camera's position.
        return entity.rect.move(-self.rect.x, -self.rect.y)

    # Update the camera's position to follow a target entity (e.g., the player).
    def update(self, target):
        # Set the camera's center position to the center position of the target entity.
        self.rect.center = target.rect.center
