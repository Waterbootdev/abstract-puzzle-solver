from piece_key_group_count import PieceKeyGroupCount

class PieceKeyCount:
    def __init__(self, piece_key: str, piece_key_group_count: PieceKeyGroupCount) -> None:
        self.piece_key = piece_key
        self.piece_key_group_count = piece_key_group_count
    def __repr__(self) -> str:
        return f'{self.piece_key}/{self.piece_key_group_count}'
    
if __name__ == '__main__':
    pass