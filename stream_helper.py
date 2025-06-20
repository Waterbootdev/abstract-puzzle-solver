from os import path

def file_name(directory_path: str, index: int) -> str:
        return path.join(directory_path, f'solution.{index}.bytes')