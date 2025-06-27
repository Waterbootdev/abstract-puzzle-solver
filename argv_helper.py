from typing import TypeVar, List
from collections.abc import Callable

T = TypeVar("T", int, float)

def cast_number(type: Callable[[str], T], number_str: str, default: T, minimum: T):
    try:
        value = max(minimum, type(number_str))
    except Exception:
        return default
    else:
        return value
        
def get_from_argvs(current_args: List[str], 
                   width_def: int = 5, 
                   height_def: int = 5,
                   subdirctory_def: str = 'solutions') -> tuple[int, int, str]:
    width = width_def
    height = height_def
    subdirctory = subdirctory_def    
    match len(current_args):
        case 2:             
            width = cast_number(int, current_args[1], width_def, 0)
        case 3: 
            width = cast_number(int, current_args[1], width_def, 0)
            height = cast_number(int, current_args[2], height_def, 0)
        case 4:
            width = cast_number(int, current_args[1], width_def, 0)
            height = cast_number(int, current_args[2], height_def, 0)
            subdirctory = current_args[3]
        case _:
            pass
    return width, min(width, height), subdirctory
