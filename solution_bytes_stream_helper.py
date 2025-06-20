from typing import List, TypeVar
from collections.abc import Callable
from solutions_stream import WriteSolutionBytesStream, ReadSolutionBytesStream
from os import path
from pathlib import Path

T = TypeVar('T', WriteSolutionBytesStream, ReadSolutionBytesStream)

def mkdir(directory_path: str) -> None:
    path: Path = Path(directory_path)
    if not path.exists():
        path.mkdir()

def init_solution_streams(path: str, length: int, solution: List[str], new_stream: Callable[[str, int, List[str]], T], create_directory: bool) -> List[List[T]]:
    directory_paths: List[str] = [directory_path(path, i, create_directory) for i in range(length)]
    return [[new_stream(path, j, solution) for j in range(i + 1) ] for i, path in enumerate(directory_paths)]

def directory_path(directory_path: str, index: int, create_directory: bool) -> str:

    directory_path = path.join(directory_path, f'{index}')

    if create_directory:
        mkdir(directory_path)

    return directory_path

