from piece_key_constants import ASTERISK_PIECE_KEY, PIECE_KEY_BASE
from base_piece import BasePiece, Directions, Coordinate
from edge import Edge, OPPOSITE_EDGE 
from rotation_matrix import INDEX_ROTATION_MATRIX
from opposite_piece_keys import OPPOSITE_PIECE_KEYS
from piece_key_count import PieceKeyCount
from typing import List, Dict, Self, Tuple
from trie import TrieNode, insert_key, contains_key


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
        self.down_keys: List[int] = []
        self.pieces: List[PieceKeyCountsPiece] = []
        self.root = TrieNode(PIECE_KEY_BASE)
        
    
    def __repr__(self) -> str:
        return self.rotated_piece_key()
    
    def init_down_keys(self) -> None:
        for i, piece in enumerate(self.pieces):        
            self.down_keys[i] = piece.part(Edge.DOWN)
        
    def insert(self, index: int) -> Tuple[int, List[int]]:

        return insert_key(self.root, PIECE_KEY_BASE, self.down_keys, index)

    def contains(self, index: int) -> Tuple[bool, bool]:

        if self.rotated:
            self.down_keys[-1] = self.part(Edge.DOWN)
        else:
            self.down_keys[-1] = self.part(Edge.RIGHT)
            self.down_keys[-2] = self.part(Edge.DOWN)

        return contains_key(self.root, self.down_keys, index)

    def part(self,edge: Edge) -> int:
        return int(self.piece_key[edge])

    def rotated_piece_key(self) -> str:
        return ''.join([self.piece_key[i] for i in self.rotation])
       
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
    

def down_keys(down_keys:List[int], pieces:List[PieceKeyCountsPiece]) -> None:
        for i, piece in enumerate(pieces):
           down_keys[i] = int(piece.piece_key[Edge.DOWN])

 

        


         
    
    

    
