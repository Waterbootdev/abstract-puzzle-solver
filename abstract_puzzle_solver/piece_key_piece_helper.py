from piece_keys_helper import List, Dict, T, piece_key_groups_counts
#from piece_key_piece import PieceKeyPiece
#from typing import TypeVar

#KeyPiece = TypeVar("KeyPiece", bound=PieceKeyPiece)

def piece_key_groups_counts_sum(pieces: List[T]) -> Dict[str, int]:
    return {first_key: sum(keys.values()) for first_key, keys in piece_key_groups_counts(pieces).items()}

def print_key_groups_counts(pieces: List[T]) -> Dict[str, Dict[str, int]]:
    print()
    counts = piece_key_groups_counts(pieces)
    for group in counts.values():
        f = dict(filter(lambda t: t[1]> 0, group.items()))
        count = sum(f.values())
        if count:
            print('{}\t{}'.format(count ,f))
    return counts


