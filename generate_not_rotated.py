from typing import List
from itertools import groupby

def generate_not_rotated(rotated: List[bool], rotated_length: int, height: int, frame_indexes: List[int]) -> List[List[int]]:
    
    frames: List[List[int]] =  list(map(lambda t: list(t[1]), groupby(frame_indexes)))
    lengths = list(map(len, frames)) 

    if len (lengths) == 0:
        return []
        

    before: List[List[int]] = []
    not_rotated: List[int]
    
    if len(lengths) > 1:
        not_rotated = first_frame(rotated, before, lengths[0])

        if len(lengths) > 2:
            between_first_and_last_frame(rotated, rotated_length, before, lengths, not_rotated)
        
        last_frame(rotated, height, before, lengths, not_rotated)
    
    else:
        not_rotated = single_frame(before, lengths[0])

    if len(before[-1]) == 1:
        del before[-1][-1]

    assert(len(before) == rotated_length)
    assert(before[-1] == [])

    return before

def between_first_and_last_frame(rotated: List[bool], length: int, before: List[List[int]], lengths:List[int], current_not_rotated: List[int]):
    
    del current_not_rotated[0]
    index = lengths[0]

    for _ in range(length - lengths[-1] - lengths[0]):
        if not rotated[index]:
            del current_not_rotated[0]          
            current_not_rotated.append(index)
            before.append(current_not_rotated.copy())       
        else:
            del current_not_rotated[0]          
            del current_not_rotated[0]          
            before.append(current_not_rotated.copy())
            before[-1].append(index)  
        index += 1

def last_frame(rotated: List[bool], height: int, before: List[List[int]], lengths:List[int], current_not_rotated: List[int]):
    
    if height%2 == 0:

        half_length = lengths[-1] // 2

        last_row(before, half_length - 2, last_frame_first_row(rotated, before, half_length))
    else:
        last_row(before, lengths[-1] - 1, current_not_rotated)

def last_frame_first_row(rotated: List[bool], before: List[List[int]], row_length: int):
    
    current_not_rotated: List[int] = before[-1].copy()

    index: int = before[-1][-1] + 1

    del current_not_rotated[0]          
    del current_not_rotated[-1]          
    current_not_rotated.append(index)
    before.append(current_not_rotated.copy())
    index += 1

    for _ in range(row_length):
        if not rotated[index]:
            del current_not_rotated[0]          
            current_not_rotated.append(index)
            before.append(current_not_rotated.copy())       
        else:
            del current_not_rotated[0]          
            del current_not_rotated[0]          
            before.append(current_not_rotated.copy())
            before[-1].append(index)
        index += 1
    
    return current_not_rotated

def last_row(before: List[List[int]], row_length: int, current_not_rotated: List[int]):
    index: int = before[-1][-1] + 1

    del current_not_rotated[0]          
    del current_not_rotated[-1]          
    current_not_rotated.append(index)
    before.append(current_not_rotated.copy())
    index += 1

    for _ in range(row_length):
        del current_not_rotated[0]          
        del current_not_rotated[-1]          
        del current_not_rotated[-1]          
        current_not_rotated.append(index)
        before.append(current_not_rotated.copy())
        index += 1

    del before[-1][-1]
    del before[-1][-1]

def first_frame(current_rotated: List[bool], before: List[List[int]], frame_length:int):
    current_not_rotated: List[int] = []
      
    for index in range(frame_length):
        if not current_rotated[index]:
            current_not_rotated.append(index)
            before.append(current_not_rotated.copy())
        else:
            before.append(current_not_rotated.copy())
            before[-1].append(index)
  
    del before[-1][0]

    return current_not_rotated

def single_frame(before: List[List[int]], frame_length:int):
    current_not_rotated: List[int] = []
  
    assert(frame_length % 2 == 0)

    half_frame_length = frame_length // 2

    for index in range(half_frame_length):
        current_not_rotated.append(index)
        before.append(current_not_rotated.copy())       
          
    
    for index in range(half_frame_length):
        del current_not_rotated[-1]
        before.append(current_not_rotated.copy())
    
    return current_not_rotated
