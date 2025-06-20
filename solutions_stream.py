from os import path
from typing import List

class SolutionsStream:

    def __init__(self, directory_path: str, index: int, solution: List[bytes]) -> None:
        self.index = index
        self.solution = solution
        self.file = open(SolutionsStream.file_name(directory_path, index), 'bw')

    @staticmethod
    def file_name(directory_path: str, index: int) -> str:
        return path.join(directory_path, f'solution.{index}.bytes')

    def write(self):
        self.file.write(self.solution[self.index])

    
    def close(self):
        self.file.close()