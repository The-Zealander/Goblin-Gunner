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
    },
    TileType.GRASS: {
        "color": green,
        "walkable": True,
        "speed_modifier": 1.0,  # No movement penalty
    },
    TileType.WATER: {
        "color": blue,
        "walkable": True,
        "speed_modifier": 0.5,  # Movement penalty in water
    },
    TileType.TREE: {
        "color": lime,
        "walkable": True,  # Trees are walkable but block vision
        "speed_modifier": 0.75,  # Movement penalty in forest
        "blocks_vision": True,  # Add a property for vision blocking
    },
    TileType.WALL: {
        "color": gray,
        "walkable": False,
        "speed_modifier": 1.0,  # No movement penalty
    },
}
