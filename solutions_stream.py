from os import path
from typing import List

class SolutionsStream:

    def __init__(self, directory_path: str, index: int, solution: List[str]) -> None:
        self.index = index
        self.solution = solution
        self.file = open(SolutionsStream.file_name(directory_path, index), 'w+')

    @staticmethod
    def file_name(directory_path: str, index: int) -> str:
        return path.join(directory_path, f'solution.{index}.txt')

    def write(self, times: int):
        self.file.write(times * self.solution[self.index])

    def copy(self, start_index: int, times: int):
        self.file.seek(start_index)
        buffer = self.file.read(times)
        self.file.seek(0, 2)
        self.file.write(buffer)

    def close(self):
        self.file.close()