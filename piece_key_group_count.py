
class PieceKeyGroupCount:
    def __init__(self,piece_groups_key: str, initial_count: int) -> None:
        self.piece_groups_key = piece_groups_key
        self.initial_count = initial_count
        self.current_count = initial_count
    
    def __repr__(self) -> str:
        return f'{self.piece_groups_key}:{self.current_count}/{self.initial_count}'
    

