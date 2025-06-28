from edge import Edge, EDGES
from piece_keys import PIECE_KEYS
from typing import List, Dict, Set

def asterisk_from_edges(edges: List[Edge], key: str) -> str:

    key_list:List[str] = list(key)

    for i in range(len(key_list)):
        if i not in edges:
            key_list[i] = '*'
    
    return ''.join(key_list)

def asterisk_to_piece_keys(edges: List[Edge]) -> Dict[str, List[str]]:
    key_list: List[str] = [asterisk_from_edges(edges, key) for key in PIECE_KEYS]
    key_set: Set[str] = set(key_list)
    piece_keys_from_asterisk: Dict[str, List[str]] = {key: [] for key in key_set}

    for key, piece_key in zip(key_list, PIECE_KEYS):
        piece_keys_from_asterisk[key].append(piece_key)

    return piece_keys_from_asterisk

EDGES_TO_ASTERISK: Dict[str, Dict[str, List[str]]] = dict(zip(EDGES.keys(), map(asterisk_to_piece_keys, EDGES.values())))


