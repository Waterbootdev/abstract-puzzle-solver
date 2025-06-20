from stream_helper import file_name
from typing import List
from piece_keys import PIECE_KEY_TO_BYTE, BYTE_TO_PIECE_KEY


class SolutionBytes:
    def __init__(self, index: int, solution: List[str]) -> None:
        self.index = index
        self.solution = solution
    def get(self)-> bytes:
       return PIECE_KEY_TO_BYTE[self.solution[self.index]]
    def set(self, piece_key: bytes) -> None:
        self.solution[self.index] = BYTE_TO_PIECE_KEY[piece_key]
    
class WriteSolutionBytesStream(SolutionBytes):

    def __init__(self, directory_path: str, index: int, solution: List[str]) -> None:
        super().__init__(index, solution)
        self.file = open(file_name(directory_path, index), 'bw')

    def write(self)-> None:
        self.file.write(self.get())
    
    def close(self)-> None:
        self.file.close()

class ReadSolutionBytesStream(SolutionBytes):

    def __init__(self, directory_path: str, index: int, solution: List[str]) -> None:
        super().__init__(index, solution)
        self.file = open(file_name(directory_path, index), 'br+')

    def read(self) -> None:
        self.set(self.file.read(1))
    
    def close(self)-> None:
        self.file.close()