from collections.abc import Callable
from os import path
from pathlib import Path
from typing import List, TypeVar

from solutions_stream import ReadSolutionBytesStream, WriteSolutionBytesStream

T = TypeVar("T", WriteSolutionBytesStream, ReadSolutionBytesStream)


def mkdir(directory_name: str) -> None:
    directory_path: Path = Path(directory_name)
    if not directory_path.exists():
        directory_path.mkdir()


def init_solution_streams(
    directory_path: str,
    length: int,
    solution: List[str],
    new_stream: Callable[[str, int, List[str]], T],
    create_directory: bool,
) -> List[List[T]]:
    directory_paths: List[str] = [
        solution_directory_path(directory_path, i, create_directory)
        for i in range(length)
    ]
    return [
        [new_stream(path, j, solution) for j in range(i + 1)]
        for i, path in enumerate(directory_paths)
    ]


def solution_directory_path(
    directory_path: str, index: int, create_directory: bool
) -> str:
    directory_path = path.join(directory_path, f"{index}")

    if create_directory:
        mkdir(directory_path)

    return directory_path
