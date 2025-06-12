from base_piece import List, BasePiece, Directions, Coordinate
from edge import Edge, OPPOSITE_EDGE 
from rotation_matrix import INDEX_ROTATION_MATRIX
from piece_keys import PIECE_KEYS_IDENTITY
from collections.abc import Callable
from opposite_piece_keys import OPPOSITE_PIECE_KEYS

class PieceKeyPiece(BasePiece):
    def __init__(self, piece_key: str, opposite_key: str, print_positions: Callable[[Coordinate, List[Directions]], List[str]], frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> None:
        super().__init__(frame_index, rotation_index, rotated, directions, coordinate, edges)
        self.opposite_piece_keys = OPPOSITE_PIECE_KEYS[opposite_key]
        self.piece_key = piece_key
        self.opposite_piece_key = self.opposite_piece_keys[piece_key]
        rotation_matrix = INDEX_ROTATION_MATRIX[rotation_index]
        self.rotation_matrix = rotation_matrix
        self.rotation = rotation_matrix[0]
        self.inital_piece_key =  piece_key
        self.print_positions = print_positions(coordinate, directions)
    

    def __repr__(self) -> str:
        return self.rotated_piece_key()

    def rotated_piece_key(self) -> str:
        return PIECE_KEYS_IDENTITY[''.join([self.piece_key[i] for i in self.rotation])]
       
    def get_opposite_key_part(self, rotation_index: int, edge: Edge) -> str:
        return self.opposite_piece_key[self.rotation_matrix[rotation_index][OPPOSITE_EDGE[edge]]]
    
    def set_piece_key(self, piece_key: str) -> None:
        self.piece_key = PIECE_KEYS_IDENTITY[piece_key]
        self.opposite_piece_key = self.opposite_piece_keys[piece_key]

    def is_changed(self, edge: Edge) -> bool:
        return self.piece_key[edge] != self.inital_piece_key[edge]
    

    
