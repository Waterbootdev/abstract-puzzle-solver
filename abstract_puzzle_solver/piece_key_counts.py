from piece_key_group_count  import PieceKeyGroupCount
from piece_key_count import PieceKeyCount
from piece_key_rotation_groups_generation import PIECE_KEYS_ROTATIONS_SHORT
from trie import TrieNode, insert_key_list
from asterisk_piece_keys import EDGES_TO_ASTERISK
from typing import Dict, List, Tuple

class PieceKeyCounts:
    def __init__(self, initial_piece_key_groups_counts:Dict[str, int]) -> None:
        
        self.initial_piece_key_groups_counts: Dict[str, PieceKeyGroupCount] = {piece_groups_key: PieceKeyGroupCount(piece_groups_key, initial_count) for piece_groups_key, initial_count in initial_piece_key_groups_counts.items()}
        self.initial_piece_key_counts: Dict[str, PieceKeyCount] = {}

        for piece_key_groups_key, group in PIECE_KEYS_ROTATIONS_SHORT.items():
            initial_piece_key_groups_count: PieceKeyGroupCount = self.initial_piece_key_groups_counts[piece_key_groups_key]
            for piece_key in group:
                self.initial_piece_key_counts[piece_key] = PieceKeyCount(piece_key, initial_piece_key_groups_count)

        self.asterisk_piece_key_counts: Dict[str, Dict[str, List[PieceKeyCount]]] = {k1:{k2:[self.initial_piece_key_counts[v3] for v3 in v2] for k2,v2 in v1.items()} for k1, v1 in EDGES_TO_ASTERISK.items()}
        self.max : List[int] = list(map(lambda x: x+1, initial_piece_key_groups_counts.values()))
        self.max.append(0)
        self.root = TrieNode(self.max[0])
        self.current_index = 0

    def insert_counts(self) -> Tuple[int, int]:
        
        def current_count(piece_key_count: PieceKeyGroupCount) -> int:
        
            return piece_key_count.current_count
        
        count, index = insert_key_list(self.root, self.max, list(map(current_count, self.initial_piece_key_groups_counts.values())), self.current_index)
        
        if count > 0:
            assert(index == self.current_index)
            self.current_index += 1
        else:
            assert(index < self.current_index)
       
        return count, index 
        

if __name__ == '__main__':
    pass