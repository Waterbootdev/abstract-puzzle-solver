from solutions_stream import WriteSolutionBytesStream, ReadSolutionBytesStream
from solution_bytes_stream_helper import init_solution_streams
from insert_node_value import InsertNodeValue
from piece_key_counts_piece import PieceKeyCountsPiece
from solution_streams_helper import open_solution_stack_stream, open_position_stream
from typing import List

from extra_piece import ExtraPieceKeyCountsPiece
from typing import TypeVar, Generic

T = TypeVar('T', PieceKeyCountsPiece, ExtraPieceKeyCountsPiece)


class SolutionWriteStreams(Generic[T]):

    def __init__(self, directory_path: str, pieces: List[T]):
        self.pieces = pieces
        self.number_pieces = len(pieces)
        self.stack_stream = open_solution_stack_stream(directory_path, 'w')
        self.position_stream = open_position_stream(directory_path, 'position','bw')
        self.stack_position_stream = open_position_stream(directory_path, 'stack_position','bw')
        self.stack_stream.write(f'{self.number_pieces}\n')
        self.solution = ['']*self.number_pieces
        self.solution_streams = init_solution_streams(directory_path, self.number_pieces, self.solution, WriteSolutionBytesStream, True)
        self.number_streams = len(self.solution_streams)

    def append_solution(self, solution_count : int, stack_index: int) -> int:
        
        self.write_to_streams(stack_index)

        self.stack_position_stream.write(self.stack_stream.tell().to_bytes(length=8))
        
        self.stack_stream.write(f'{stack_index}:{solution_count}:{solution_count}:{0}\n')
     
        return solution_count + 1

    def append_solution_with_prefix(self, solution_count: int, stack_index: int, insert_node_value: InsertNodeValue) -> int:

        self.write_to_streams(stack_index)

        self.stack_position_stream.write(self.stack_stream.tell().to_bytes(length=8))
        
        self.stack_stream.write(f'{stack_index}:{solution_count}:{insert_node_value.first}:{insert_node_value.count}\n')
     
        return solution_count + insert_node_value.count

    def write_to_streams(self, stack_index: int):
        
        self.extract_solution(stack_index)

        streams: List[WriteSolutionBytesStream] = self.solution_streams[stack_index]

        self.position_stream.write(streams[0].file.tell().to_bytes(length=8))

        for stream in streams:
            stream.write()

    def extract_solution(self, stack_index: int) -> None:
        for i in range(stack_index + 1):
            self.solution[i] = self.pieces[i].piece_key
        
    def close(self) -> None:
        self.position_stream.close()
        self.stack_position_stream.close()
        self.stack_stream.close()
        for streams in self.solution_streams:
            for stream in streams:
                stream.close()


class SolutionReadStreams:

    def __init__(self, directory_path: str):
        self.stack_stream = open_solution_stack_stream(directory_path, 'r+')
        self.position_stream = open_position_stream(directory_path, 'position','br+')
        self.stack_position_stream = open_position_stream(directory_path, 'stack_position','br+')
        self.number_pieces = int(self.stack_stream.readline())
        self.solution = ['']*self.number_pieces
        self.solution_streams = init_solution_streams(directory_path, self.number_pieces, self.solution, ReadSolutionBytesStream, False)
        self.number_streams = len(self.solution_streams)
    
        
    def close(self) -> None:
        self.stack_stream.close()
        self.position_stream.close()
        self.stack_position_stream.close()
        for streams in self.solution_streams:
            for stream in streams:
                stream.close()