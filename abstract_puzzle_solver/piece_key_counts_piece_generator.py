from opposite_piece_keys import DEFAULT_OPPOSITE_KEY
from piece_generator import PieceGenerator
from base_piece import Directions, Coordinate, List
from edge import Edge
from piece_key_counts_piece import PieceKeyCountsPiece
from piece_key_count import PieceKeyCount
from typing import Dict

class PieceKeyCountsPieceGenerator(PieceGenerator[PieceKeyCountsPiece]):
    def __init__(self, width: int, height: int, first_frame_piece_keys: List[str], piece_key_counts: Dict[str, Dict[str, List[PieceKeyCount]]], opposite_key: str = DEFAULT_OPPOSITE_KEY) -> None:
        super().__init__(width + 2, height + 2)
        
        def get_new_base_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> PieceKeyCountsPiece:
            return PieceKeyCountsPiece(piece_key_counts, opposite_key, frame_index, rotation_index, rotated, directions, coordinate, edges)
        
        self.spiral: List[PieceKeyCountsPiece] = self.generate(get_new_base_piece)

        for i, piece_key in enumerate(first_frame_piece_keys):
            self.spiral[i].set_piece_key(piece_key)

        self.pieces: List[PieceKeyCountsPiece] = [piece for piece  in self.spiral if piece.frame_index > 0]

        



        