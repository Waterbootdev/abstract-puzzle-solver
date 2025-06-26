from search_trie_pickle import SearchDict
from opposite_piece_keys import DEFAULT_OPPOSITE_KEY
from piece_generator import PieceGenerator
from generate_not_rotated import generate_not_rotated
from base_piece import Directions, Coordinate, List
from edge import Edge
from piece_key_counts_pickle_piece import PieceKeyCountsPiece
from piece_key_count import PieceKeyCount
from typing import Dict
from node_counter import NodeCounter
from array import array
from pathlib import Path
from os import path


class PieceKeyCountsPieceGenerator(PieceGenerator[PieceKeyCountsPiece]):
    def __init__(self, width: int, height: int, directory_path_name: str, node_counter: NodeCounter, first_frame_piece_keys: List[str], piece_key_counts: Dict[str, Dict[str, List[PieceKeyCount]]], opposite_key: str = DEFAULT_OPPOSITE_KEY) -> None:
        if width < 1 or height > width:
            raise ValueError()

        super().__init__(width + 2, height + 2)

        def get_new_base_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> PieceKeyCountsPiece:
            return PieceKeyCountsPiece(piece_key_counts, opposite_key, frame_index, rotation_index, rotated, directions, coordinate, edges)
        
        self.spiral: List[PieceKeyCountsPiece] = self.generate(get_new_base_piece)

        for i, piece_key in enumerate(first_frame_piece_keys):
            self.spiral[i].set_piece_key(piece_key)

        self.pieces: List[PieceKeyCountsPiece] = [piece for piece  in self.spiral if piece.frame_index > 0]

        links: List[List[int]] = generate_not_rotated(self.rotated, len(self.spiral), height + 2, self.frame_index)

        first_index = self.pieces[0].coordinate.index

        directory_path: Path = Path(directory_path_name)
        if not directory_path.exists():
            directory_path.mkdir()
   
        for piece, link in zip(self.spiral, links):
            piece.pieces =[self.spiral[li] for li in link if li >= first_index]
            length = len(piece.pieces)
            if length > 0:
                del piece.pieces[-1]
                length -= 1
            if piece.coordinate.index >= first_index:
                piece.down_keys = array('i', [0]*length)
                piece.root = SearchDict(node_counter, length + (1 if piece.rotated else 2), path.join(directory_path_name, str(piece.coordinate.index - first_index)))
            
     
            


    

        


