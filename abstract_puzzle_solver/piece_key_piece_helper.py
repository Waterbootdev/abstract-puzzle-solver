from piece_key_rotation_groups_generation import PIECE_KEYS_ROTATIONS
from piece_keys_helper import List, Dict, piece_keys_counts
from piece_key_piece import PieceKeyPiece
from typing import TypeVar

KeyPiece = TypeVar("KeyPiece", bound=PieceKeyPiece)

def piece_keys(pieces: List[KeyPiece]) -> List[str]:
    return list(map(str, pieces))

def piece_key_groups_counts(pieces: List[KeyPiece]) -> Dict[str, Dict[str, int]]:
    counts = piece_keys_counts(piece_keys(pieces))
    return {first_key: {key : counts[key] for key in keys[1]} for first_key, keys in PIECE_KEYS_ROTATIONS.items()}

def print_key_groups_counts(pieces: List[KeyPiece]) -> Dict[str, Dict[str, int]]:
    print()
    counts = piece_key_groups_counts(pieces)
    for group in counts.values():
        f = dict(filter(lambda t: t[1]> 0, group.items()))
        count = sum(f.values())
        if count:
            print('{}\t{}'.format(count ,f))
    return counts




