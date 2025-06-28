from generate_spiral import generate_spiral, Edge
from base_piece_helper import generate_linked_base_pieces, Directions, Coordinate, Callable, Piece
from base_piece import List
from typing import Generic

class PieceGenerator(Generic[Piece]):

    def __init__(self, width: int , height: int) -> None:
        self.width = width
        self.height = height

        self.rotated, self.frame_index, self.rotation_index, self.directions, self.coordinates, self.links, self.forward, self.backward, self.turns, self.edges = generate_spiral(width, height)

    def generate(self, get_new_base_piece: Callable[[int, int, bool, List[Directions], Coordinate, List[Edge]], Piece]) -> List[Piece]:
        return generate_linked_base_pieces(get_new_base_piece, self.frame_index, self.rotation_index, self.rotated, self.directions, self.coordinates, self.edges, self.links, self.forward, self.backward)
       
    