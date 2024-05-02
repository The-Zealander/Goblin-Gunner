import defines
from enum import Enum


# Define different tile types
class TileType(Enum):
    GROUND = 0
    WATER = 1
    TREE = 2
    WALL = 3


# Define tile properties such as colors, speed modifiers, and walkable status
TILE_PROPERTIES = {
    TileType.GROUND: {
        "color": defines.brown,  # Brown
        "speed_modifier": 1.0,  # Normal speed
        "walkable": True,
    },
    TileType.WATER: {
        "color": defines.blue,  # Blue
        "speed_modifier": 0.5,  # Half speed
        "walkable": True,
    },
    TileType.TREE: {
        "color": defines.green,  # Green
        "speed_modifier": 0.0,  # Not walkable
        "walkable": False,
    },
    TileType.WALL: {
        "color": defines.gray,  # Gray
        "speed_modifier": 0.0,  # Not walkable
        "walkable": False,
    },
}
