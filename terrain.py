from defines import *


class TileType:
    GROUND = 0
    GRASS = 1
    WATER = 2
    TREE = 3
    WALL = 4

# Define terrain properties as a dictionary
TILE_PROPERTIES = {
    TileType.GROUND: {
        "color": brown,
        "walkable": True,
        "speed_modifier": 1.0,  # No movement penalty
        #"image": pygame.image.load("assets/dirt.png").convert_alpha(),  # Load image
    },
    TileType.GRASS: {
        "color": green,
        "walkable": True,
        "speed_modifier": 1.0,  # No movement penalty
        #"image": pygame.image.load("grass_tile.png").convert_alpha(),  # Load image
    },
    TileType.WATER: {
        "color": blue,
        "walkable": True,
        "speed_modifier": 0.5,  # Movement penalty in water
        #"image": pygame.image.load("assets/water.png").convert_alpha(),  # Load image
    },
    TileType.TREE: {
        "color": lime,
        "walkable": True,  # Trees are walkable but block vision
        "speed_modifier": 0.75,  # Movement penalty in forest
        "blocks_vision": True,  # Add a property for vision blocking
        #"image": pygame.image.load("assets/tree.png").convert_alpha(),  # Load image
    },
    TileType.WALL: {
        "color": gray,
        "walkable": False,
        "speed_modifier": 1.0,  # No movement penalty
        #"image": pygame.image.load("wall_tile.png").convert_alpha(),  # Load image
    },
}