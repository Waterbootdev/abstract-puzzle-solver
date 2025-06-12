from abstract_puzzle_generator.piece_key_constants import ASTERISK_PIECE_KEY
from abstract_puzzle_generator.base_piece import BasePiece, Directions, Coordinate
from abstract_puzzle_generator.edge import Edge, OPPOSITE_EDGE 
from abstract_puzzle_generator.rotation_matrix import INDEX_ROTATION_MATRIX
from abstract_puzzle_generator.piece_keys import PIECE_KEYS_IDENTITY
from abstract_puzzle_generator.opposite_piece_keys import OPPOSITE_PIECE_KEYS
from piece_key_count import PieceKeyCount
from typing import List, Dict, Self

class PieceKeyCountsPiece(BasePiece):
    def __init__(self, piece_key_counts: Dict[str, Dict[str, List[PieceKeyCount]]], opposite_key: str, frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> None:
        super().__init__(frame_index, rotation_index, rotated, directions, coordinate, edges)
        self.opposite_piece_keys = OPPOSITE_PIECE_KEYS[opposite_key]
        self.piece_key = ASTERISK_PIECE_KEY
        self.opposite_piece_key = ASTERISK_PIECE_KEY
        rotation_matrix = INDEX_ROTATION_MATRIX[rotation_index]
        self.rotation_matrix = rotation_matrix
        self.rotation = rotation_matrix[0]
        self.piece_key_counts = piece_key_counts[str(self.edges)]
       
    def __repr__(self) -> str:
        return self.rotated_piece_key()

    def rotated_piece_key(self) -> str:
        return PIECE_KEYS_IDENTITY[''.join([self.piece_key[i] for i in self.rotation])]
       
    def get_opposite_key_part(self, rotation_index: int, edge: Edge) -> str:
        return self.opposite_piece_key[self.rotation_matrix[rotation_index][OPPOSITE_EDGE[edge]]]
    
    def set_piece_key(self, piece_key: str) -> None:
        self.piece_key = piece_key
        self.opposite_piece_key = self.opposite_piece_keys[piece_key]

    def oppsites_opposite_key_part(self, opposite_pice: Self|None, edge: Edge) -> str:
        if opposite_pice:
            return opposite_pice.get_opposite_key_part(self.rotation_index, edge)
        else:
            raise Exception()
        
    def asterisk_piece_key(self) -> str:
        asterisk_piece_key = list(ASTERISK_PIECE_KEY)
    
        for edge in self.edges:
            asterisk_piece_key[edge] = self.oppsites_opposite_key_part(self.links[edge], edge)
        
        return ''.join(asterisk_piece_key)
    
    def current_piece_key_counts(self) -> List[PieceKeyCount]:
        return self.piece_key_counts[self.asterisk_piece_key()]

    
        
    


    
