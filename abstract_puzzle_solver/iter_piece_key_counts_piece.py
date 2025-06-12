from abstract_puzzle_solver.piece_key_counts_piece import PieceKeyCountsPiece

class IterPieceKeyCountsPiece:
    def __init__(self, piece_key_counts_piece: PieceKeyCountsPiece) -> None:
        self.piece_key_counts_piece = piece_key_counts_piece
        self.piece_key_counts = [count for count in piece_key_counts_piece.current_piece_key_counts() if count.piece_key_group_count.current_count > 0]
        self.index = 0

    def next(self) -> bool:
        if self.index < len(self.piece_key_counts):
            piece_key_count = self.piece_key_counts[self.index]
            self.piece_key_counts_piece.set_piece_key(piece_key_count.piece_key)
            self.index += 1
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f'{self.piece_key_counts_piece}:{self.index}/{len(self.piece_key_counts)}'