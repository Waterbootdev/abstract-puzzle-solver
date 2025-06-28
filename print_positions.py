from piece_key_piece import Coordinate, Directions, List
from piece_key_piece_print_positions import intit_position

class PrintPositions:

    EMPTY = ['','','','']

    def __init__(self, scale_x: int = 3, scale_y: int = 3, x: int = 1, y: int = 1) -> None:
       self.scale_x: int = scale_x
       self.scale_y: int = scale_y
       self.x: int = x
       self.y: int = y

    def print_positions(self, coordinate: Coordinate, directions: List[Directions]) -> List[str]:
        coordinate = coordinate.scale_add(self.scale_x, self.scale_y, self.x, self.y)
        return [intit_position(coordinate, directions)  for directions in directions]
    
    @staticmethod
    def empty_print_positions(coordinate: Coordinate, directions: List[Directions]) -> List[str]:
        return PrintPositions.EMPTY
    
DEFAULT_PRINT_POSITIONS: PrintPositions = PrintPositions()