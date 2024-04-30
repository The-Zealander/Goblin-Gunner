import math

def calculate_distance(pos1, pos2):
    # Euclidean distance between two points (x1, y1) and (x2, y2)
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
