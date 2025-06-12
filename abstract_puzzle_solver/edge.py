from enum import IntEnum
from typing import Dict, List

class Edge(IntEnum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

NUMBER_EDGES = 4

OPPOSITE_EDGE: Dict[Edge, Edge] = {Edge.LEFT: Edge.RIGHT, Edge.UP: Edge.DOWN, Edge.RIGHT: Edge.LEFT, Edge.DOWN: Edge.UP}

LEFT_UP_RIGHT_DOWN: List[Edge] = [Edge.LEFT, Edge.UP, Edge.RIGHT, Edge.DOWN]
LEFT_UP_RIGHT: List[Edge] = [Edge.LEFT, Edge.UP, Edge.RIGHT]
LEFT_UP_DOWN: List[Edge] = [Edge.LEFT, Edge.UP, Edge.DOWN]
LEFT_UP: List[Edge] = [Edge.LEFT, Edge.UP]

EDGES = {str(e): e for e in [LEFT_UP, LEFT_UP_RIGHT, LEFT_UP_DOWN, LEFT_UP_RIGHT_DOWN]}