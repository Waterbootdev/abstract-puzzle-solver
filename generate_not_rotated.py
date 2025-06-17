from typing import List
from itertools import groupby
from spiral_helper import generate_rotated, generate_frame_index

def generate_not_rotated(rotated: List[bool], length: int, height: int, frame_indexes: List[int]) -> List[List[int]]:
    
    frames: List[List[int]] =  list(map(lambda t: list(t[1]), groupby(frame_indexes)))
    lengths = list(map(len, frames)) 

    if len (lengths) == 0:
        return []
        

    before: List[List[int]] = []
    not_rotated: List[int]
    
    if len(lengths) > 1:
        not_rotated = first_frame(rotated, before, lengths[0])

        if len(lengths) > 2:
            between_first_and_last_frame(rotated, length, before, lengths, not_rotated)
        
        last_frame(rotated, height, before, lengths, not_rotated)
    
    else:
        not_rotated = single_frame(before, lengths[0])

    if len(before[-1]) == 1:
        del before[-1][-1]

    assert(len(before) == length)
    assert(before[-1] == [])

    return before

def between_first_and_last_frame(rotated: List[bool], length: int, before: List[List[int]], lengths:List[int], not_rotated: List[int]):
    
    del not_rotated[0]
    index = lengths[0]

    for _ in range(length - lengths[-1] - lengths[0]):
        if not rotated[index]:
            del not_rotated[0]          
            not_rotated.append(index)
            before.append(not_rotated.copy())       
        else:
            del not_rotated[0]          
            del not_rotated[0]          
            before.append(not_rotated.copy())
            before[-1].append(index)  
        index += 1

def last_frame(rotated: List[bool], height: int, before: List[List[int]], lengths:List[int], not_rotated: List[int]):
    
    if height%2 == 0:

        lengthh = lengths[-1] // 2

        last_row(before, lengthh - 2, last_frame_first_row(rotated, before, lengthh))
    else:
        last_row(before, lengths[-1] - 1, not_rotated)

def last_frame_first_row(rotated: List[bool], before: List[List[int]], lengthh: int):
    
    not_rotated: List[int] = before[-1].copy()

    index: int = before[-1][-1] + 1

    del not_rotated[0]          
    del not_rotated[-1]          
    not_rotated.append(index)
    before.append(not_rotated.copy())
    index += 1

    for _ in range(lengthh):
        if not rotated[index]:
            del not_rotated[0]          
            not_rotated.append(index)
            before.append(not_rotated.copy())       
        else:
            del not_rotated[0]          
            del not_rotated[0]          
            before.append(not_rotated.copy())
            before[-1].append(index)
        index += 1
    
    return not_rotated

def last_row(before: List[List[int]], length: int, not_rotated: List[int]):
    index: int = before[-1][-1] + 1

    del not_rotated[0]          
    del not_rotated[-1]          
    not_rotated.append(index)
    before.append(not_rotated.copy())
    index += 1

    for _ in range(length):
        del not_rotated[0]          
        del not_rotated[-1]          
        del not_rotated[-1]          
        not_rotated.append(index)
        before.append(not_rotated.copy())
        index += 1

    del before[-1][-1]
    del before[-1][-1]

def first_frame(rotated: List[bool], before: List[List[int]], length:int):
    not_rotated: List[int] = []
      
    for index in range(length):
        if not rotated[index]:
            not_rotated.append(index)
            before.append(not_rotated.copy())
        else:
            before.append(not_rotated.copy())
            before[-1].append(index)
  
    del before[-1][0]

    return not_rotated

def single_frame(before: List[List[int]], length:int):
    not_rotated: List[int] = []
  
    assert(length % 2 == 0)

    lengthh = length // 2

    for index in range(lengthh):
        not_rotated.append(index)
        before.append(not_rotated.copy())       
          
    
    for index in range(lengthh):
        del not_rotated[-1]
        before.append(not_rotated.copy())
    
    return not_rotated



if __name__ == '__main__':
    
    width = 3
    height = 2

    length = width * height
      
    rotated = generate_rotated(width, height, length)

    frame_index, rotation_index = generate_frame_index(rotated)

    not_rotated =  generate_not_rotated(rotated, length, height, frame_index)

    
