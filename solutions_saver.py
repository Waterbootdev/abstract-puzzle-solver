from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece import PieceKeyCountsPiece
from solution_searcher import SolutionSearcher
from solutions_streams import SolutionsStreams
from typing import List

def save_solutions(directory_path: str, counts: PieceKeyCounts, pieces: List[PieceKeyCountsPiece]) -> None:
    streams = SolutionsStreams(directory_path, pieces)
    solution_searcher = SolutionSearcher(counts, pieces, streams.append_solution, streams.append_solution_with_prefix)
    solution_searcher.search(True)
    streams.close()


        


    