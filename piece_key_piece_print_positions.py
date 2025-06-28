from piece_key_piece import Coordinate, Directions

def escape_position(row: int, column: int):
    return f'\033[{row};{column}H'
  
def intit_position(coordinate: Coordinate, directions: Directions) -> str:
    x, y = coordinate.left(directions)
    return escape_position(y + 1, x + 1)
