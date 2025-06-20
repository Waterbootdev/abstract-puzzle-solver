from coordinate import Coordinate
from directions import List, Directions
from edge import Edge
from typing import Self


class BasePiece:

    def __init__(self, frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> None:

      
        self.frame_index = frame_index
        self.rotation_index = rotation_index
        self.rotated = rotated
        self.directions = directions
        self.coordinate = coordinate
        self.edges = edges
        self.links: List[Self|None] = [None, None, None, None]
        self.forward: Self|None = None
        self.backward: Self|None = None

    def __repr__(self) -> str:
        return f'{self.frame_index}:{self.rotation_index}:{self.coordinate}:{self.rotated}:{self.directions}'

