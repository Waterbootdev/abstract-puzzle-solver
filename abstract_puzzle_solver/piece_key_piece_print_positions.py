from piece_key_piece import Coordinate, Directions

def escape_position(row: int, column: int):
    return"\033[%d;%dH" %(row, column)

def intit_position(coordinate: Coordinate, directions: Directions) -> str:
    x, y = coordinate.left(directions)
    return escape_position(y + 1, x + 1)
