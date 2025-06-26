from index_pool import IndexPool
from piece_key_counts import PieceKeyCounts
from solution_searcher import SolutionSearcher
from solutions_streams import SolutionWriteStreams
from node_counter import NodeCounter
from typing import List
from piece_key_counts_pieces import T
 
def save_solutions(directory_path: str, index_pool: IndexPool, node_counter: NodeCounter,  counts: PieceKeyCounts, pieces: List[T]) -> None:
    streams = SolutionWriteStreams[T](directory_path, pieces)
    solution_searcher = SolutionSearcher[T](index_pool, node_counter, counts, pieces, streams.append_solution, streams.append_solution_with_prefix, sum(map(lambda x: x.root.length ,pieces)))
    solution_searcher.search(True)
    streams.close()


        


    