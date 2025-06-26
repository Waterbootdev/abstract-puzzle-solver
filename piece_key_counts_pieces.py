import piece_key_counts_piece
import piece_key_counts_pickle_piece
from extra_piece import ExtraPieceKeyCountsPiece
from typing import TypeVar

T = TypeVar('T', piece_key_counts_piece.PieceKeyCountsPiece, piece_key_counts_pickle_piece.PieceKeyCountsPiece, ExtraPieceKeyCountsPiece)

