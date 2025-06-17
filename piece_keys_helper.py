from piece_keys import List, Dict, PIECE_KEYS
from piece_key_rotation_groups_generation import PIECE_KEYS_ROTATIONS_SHORT
from typing import TypeVar

T = TypeVar("T")

def to_piece_keys(pieces: List[T]) -> List[str]:
    return list(map(str, pieces))

def piece_keys_counts(piece_keys: List[str]) -> Dict[str, int]:
    counts = {key: 0 for key in PIECE_KEYS}
    for piece_key in piece_keys:
        counts[piece_key]+=1
    return counts

def piece_key_groups_counts(pieces: List[T]) -> Dict[str, Dict[str, int]]:
    counts = piece_keys_counts(to_piece_keys(pieces))
    return {first_key: {key : counts[key] for key in keys} for first_key, keys in PIECE_KEYS_ROTATIONS_SHORT.items()}

if __name__ == '__main__':
    assert len(piece_keys_counts(PIECE_KEYS)) == len(PIECE_KEYS)
    assert set(piece_keys_counts(PIECE_KEYS).keys())==set(PIECE_KEYS)
    assert set(piece_keys_counts(PIECE_KEYS).values())=={1} 
    assert set(piece_keys_counts(PIECE_KEYS+PIECE_KEYS).values())=={2}
    