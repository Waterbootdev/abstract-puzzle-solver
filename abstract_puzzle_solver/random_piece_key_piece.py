
from piece_key_piece import PieceKeyPiece, Directions, Coordinate, Callable, Edge
from piece_keys import PIECE_KEYS
from typing import List
from random import choice

class RandomPieceKeyPiece(PieceKeyPiece):
    
    def __init__(self, opposite_key: str, print_positions: Callable[[Coordinate, List[Directions]], List[str]], frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> None:
        super().__init__(choice(PIECE_KEYS), opposite_key, print_positions, frame_index, rotation_index, rotated, directions, coordinate, edges)
    
    def fit_part(self, opposite_pice: PieceKeyPiece|None, edge: Edge) -> str:
        if opposite_pice:
            return opposite_pice.get_opposite_key_part(self.rotation_index, edge)
        else:
            raise Exception()
        
    def fit_piece_key(self) -> str:
        piece_key = list(self.piece_key)
    
        for edge in self.edges:
            piece_key[edge] = self.fit_part(self.links[edge], edge)
        
        return ''.join(piece_key)
            
    def fit_piece(self) -> None:
        self.set_piece_key(self.fit_piece_key())

    
    