from piece_key_group_count  import PieceKeyGroupCount
from piece_key_count import PieceKeyCount
from piece_key_rotation_groups_generation import PIECE_KEYS_ROTATIONS_SHORT
from trie import TrieDict
from asterisk_piece_keys import EDGES_TO_ASTERISK
from typing import Dict, List, Tuple
from collections.abc import Callable
from array import array

class PieceKeyCounts:
    def __init__(self, initial_piece_key_groups_counts:Dict[str, int]) -> None:
        
        self.initial_piece_key_groups_counts: Dict[str, PieceKeyGroupCount] = {piece_groups_key: PieceKeyGroupCount(piece_groups_key, initial_count) for piece_groups_key, initial_count in initial_piece_key_groups_counts.items()}
        self.initial_piece_key_counts: Dict[str, PieceKeyCount] = {}

        for piece_key_groups_key, group in PIECE_KEYS_ROTATIONS_SHORT.items():
            initial_piece_key_groups_count: PieceKeyGroupCount = self.initial_piece_key_groups_counts[piece_key_groups_key]
            for piece_key in group:
                self.initial_piece_key_counts[piece_key] = PieceKeyCount(piece_key, initial_piece_key_groups_count)

        self.asterisk_piece_key_counts: Dict[str, Dict[str, List[PieceKeyCount]]] = {k1:{k2:[self.initial_piece_key_counts[v3] for v3 in v2] for k2,v2 in v1.items()} for k1, v1 in EDGES_TO_ASTERISK.items()}
        
        self.max : array[int] =  array('i', map(lambda x: x+1, filter(lambda x: x > 0 ,initial_piece_key_groups_counts.values())))
        self.length = len(self.max) - 1
        self.root = TrieDict(self.max)
        self.keys: array[int] = array('i', [0]*(self.length))
        self.last_current_count = 0

        
    def insert_counts(self, next : Callable[[], int]) -> Tuple[bool, int]:
        
        for i, piece_key_count in enumerate(filter(lambda x: x.initial_count > 0, self.initial_piece_key_groups_counts.values())):
            if i < len(self.keys):
                self.keys[i] = piece_key_count.current_count
            else:
                self.last_current_count = piece_key_count.current_count

        return self.root.insert(self.keys, self.last_current_count, next)        

if __name__ == '__main__':
    pass