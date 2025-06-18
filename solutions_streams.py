from solutions_stream import SolutionsStream
from insert_node_value import InsertNodeValue
from piece_key_counts_piece import PieceKeyCountsPiece
from piece_keys import PIECE_KEY_TO_INDEX_1, PIECE_KEY_TO_INDEX_0
from typing import List

class SolutionsStreams:

    def __init__(self, path: str, pieces: List[PieceKeyCountsPiece]):
        self.pieces = pieces
        self.number_pieces = len(pieces)
        self.number_streams = 2 * self.number_pieces
        self.solution = ['']*self.number_streams
        self.streams: List[SolutionsStream] = [SolutionsStream(path, i, self.solution)  for i in range(self.number_streams)]

    def append_solution(self, solution_count : int) -> int:
        self.extract_solution(self.number_pieces)
        for stream in self.streams:
            stream.write(1)
        return solution_count + 1

    def append_solution_with_prefix(self, solution_count: int, stack_index: int, insert_node_value: InsertNodeValue) -> int:

        number_pieces = stack_index + 1

        assert number_pieces < self.number_streams

        self.extract_solution(number_pieces)

        number_streams = 2 * number_pieces

        for i in range(number_streams):
            self.streams[i].write(insert_node_value.count)

        for i in range(number_streams, self.number_streams):
            self.streams[i].copy(insert_node_value.first, insert_node_value.count)

        return solution_count + insert_node_value.count

    def extract_solution(self, number_pieces: int) -> None:
        for i in range(number_pieces):
            stream_index = 2 * i
            piece_key = self.pieces[i].piece_key
            self.solution[stream_index] = PIECE_KEY_TO_INDEX_0[piece_key]
            self.solution[stream_index + 1] = PIECE_KEY_TO_INDEX_1[piece_key]

    def close(self) -> None:
        for stream in self.streams:
            stream.close()