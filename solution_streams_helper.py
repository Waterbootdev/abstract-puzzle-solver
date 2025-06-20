
from os import path
from io import TextIOWrapper
from typing import BinaryIO



def open_solution_stack_stream(directory_path: str, mode: str) -> TextIOWrapper:
    if mode == 'r+' or mode == 'w':
        return open(file_name(directory_path, 'stack', 'txt'), mode)
    else:
        raise ValueError()

def open_position_stream(directory_path: str, name:str, mode: str) -> BinaryIO:
    if mode == 'br+' or mode == 'bw':
        return open(file_name(directory_path, name, 'bytes'), mode)
    else:
        raise ValueError()


def file_name(directory_path: str, prefix: str, extension: str) -> str:
    return path.join(directory_path, f'{prefix}.{extension}')
  