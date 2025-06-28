from piece_key_group_count import PieceKeyGroupCount
from typing import List

class PieceKeyCount:
    def __init__(self, piece_key: str, piece_key_group_count: PieceKeyGroupCount) -> None:
        self.piece_key = piece_key
        self.piece_key_group_count = piece_key_group_count
    def __repr__(self) -> str:
        return f'{self.piece_key}/{self.piece_key_group_count}'

def copy_piece_key_counts_greater_zero(source: List[PieceKeyCount], distination: List[PieceKeyCount]) -> int:

    length = 0

    for count in source:
        if count.piece_key_group_count.current_count > 0:
            distination[length] = count
            length += 1

    return length
            