from solutions_stream import SolutionsStream
from insert_node_value import InsertNodeValue
from piece_key_counts_piece import PieceKeyCountsPiece
from piece_keys import PIECE_KEY_TO_BYTE
from typing import List
from os import path
from pathlib import Path

class SolutionsStreams:

    def __init__(self, directory_path: str, pieces: List[PieceKeyCountsPiece]):
        self.pieces = pieces
        self.number_pieces = len(pieces)
        self.solution = [bytes([0])]*self.number_pieces
        self.solution_streams = SolutionsStreams.init_solution_streams(directory_path, self.number_pieces, self.solution)
        self.number_streams = len(self.solution_streams)
        self.stack_index = open(SolutionsStreams.file_name(directory_path, 'stack_index'), 'w')
        self.solution_index = open(SolutionsStreams.file_name(directory_path, 'solution_index'), 'w')
        self.first_solution_index = open(SolutionsStreams.file_name(directory_path, 'first_solution_index'), 'w')
        self.count = open(SolutionsStreams.file_name(directory_path, 'count'), 'w')
       
    @staticmethod
    def file_name(directory_path: str, prefix: str) -> str:
        return path.join(directory_path, f'{prefix}.txt')
    
    @staticmethod

    def init_solution_streams(path: str, length: int, solution: List[bytes]) -> List[List[SolutionsStream]]:
        directory_paths: List[str] = [SolutionsStreams.directory_path(path, i) for i in range(length)]
        return [[SolutionsStream(path, j, solution) for j in range(i + 1) ] for i, path in enumerate(directory_paths)]

    @staticmethod
    def directory_path(directory_path: str, index: int) -> str:

        directory_path = path.join(directory_path, f'{index}')

        SolutionsStreams.mkdir(directory_path)

        return directory_path

    @staticmethod
    def mkdir(directory_path: str) -> None:
        path: Path = Path(directory_path)
        if not path.exists():
            path.mkdir()

    def append_solution(self, solution_count : int, stack_index: int) -> int:
        self.extract_solution(self.number_pieces)

        for stream in self.solution_streams[-1]:
            stream.write()

        self.stack_index.write(f'{stack_index}\n')
        self.solution_index.write(f'{solution_count}\n')
        self.first_solution_index.write(f'{solution_count}\n')
        self.count.write(f'{0}\n')    

        return solution_count + 1

    def append_solution_with_prefix(self, solution_count: int, stack_index: int, insert_node_value: InsertNodeValue) -> int:

        number_pieces = stack_index + 1

        assert number_pieces < self.number_streams

        self.extract_solution(number_pieces)

        for stream in self.solution_streams[stack_index]:
            stream.write()

        self.stack_index.write(f'{stack_index}\n')
        self.solution_index.write(f'{solution_count}\n')
        self.first_solution_index.write(f'{insert_node_value.first}\n')
        self.count.write(f'{insert_node_value.count}\n')    

        return solution_count + insert_node_value.count

    def extract_solution(self, number_pieces: int) -> None:
        for i in range(number_pieces):
            self.solution[i] = PIECE_KEY_TO_BYTE[self.pieces[i].piece_key]
        
    def close(self) -> None:
        self.stack_index.close()
        self.solution_index.close()
        self.first_solution_index.close()
        self.count.close()
        for streams in self.solution_streams:
            for stream in streams:
                stream.close()