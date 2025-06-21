from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece import PieceKeyCountsPiece
from extra_piece import ExtraPieceKeyCountsPiece
from solution_searcher import SolutionSearcher
from solutions_streams import SolutionWriteStreams
from typing import List, TypeVar

T = TypeVar('T', PieceKeyCountsPiece, ExtraPieceKeyCountsPiece)



def save_solutions(directory_path: str, counts: PieceKeyCounts, pieces: List[T]) -> None:
    streams = SolutionWriteStreams[T](directory_path, pieces)
    solution_searcher = SolutionSearcher(counts, pieces, streams.append_solution, streams.append_solution_with_prefix)
    solution_searcher.search(True)
    streams.close()


        


    