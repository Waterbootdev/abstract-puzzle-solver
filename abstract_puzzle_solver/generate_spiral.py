

from spiral_helper import Directions, Coordinate, List, Tuple, Edge, generate_rotated, generate_frame_index, generate_directions, generate_coordinates_and_links, generate_forward, generate_backward, generate_turns, generate_edges
from itertools import groupby
def generate_spiral(width: int, height: int) -> Tuple[List[bool], List[int], List[int], List[List[Directions]], List[Coordinate], List[List[int|None]], List[int|None], List[int|None], List[int], List[List[Edge]]]:
    if height > width or width < 2 or height < 2:
        raise Exception()

    length = width * height
      
    rotated = generate_rotated(width, height, length)

    frame_index, rotation_index = generate_frame_index(rotated)

    directions = generate_directions(rotated)

    coordinates, links = generate_coordinates_and_links(width, height, rotated, directions)

    forward = generate_forward(length)
    backward = generate_backward(length)

    turns =  generate_turns(rotated)

    edges = generate_edges(length, turns)

    return rotated, frame_index, rotation_index, directions, coordinates, links, forward, backward, turns, edges
    


def generate_not_rotated(rotated: List[bool], length: int, height: int, frame_indexes: List[int]) -> List[List[int]]:
    not_rotated: List[int] = []
    before: List[List[int]] = []

    frames: List[List[int]] =  list(map(lambda t: list(t[1]), groupby(frame_indexes)))
    lengths = list(map(len, frames)) 

    if len(lengths) > 1:

        for i in range(lengths[0]):
            if not rotated[i]:
                not_rotated.append(i)
                before.append(not_rotated.copy())
            else:
                before.append(not_rotated.copy())
                before[-1].append(i)
  
        del before[-1][0]
    
    
    if len(lengths) > 2:
        
        del not_rotated[0]
        i = lengths[0]

        for _ in range(length - lengths[-1] - lengths[0]):
            if not rotated[i]:
                del not_rotated[0]          
                not_rotated.append(i)
                before.append(not_rotated.copy())       
            else:
                del not_rotated[0]          
                del not_rotated[0]          
                before.append(not_rotated.copy())
                before[-1].append(i)  
            i += 1
    
    if len(lengths) == 1:

        assert(lengths[-1] % 2 == 0)

        lengthh = lengths[-1] // 2

        for i in range(lengthh):
            not_rotated.append(i)
            before.append(not_rotated.copy())       
          
    
        for i in range(lengthh):
            del not_rotated[-1]
            before.append(not_rotated.copy())

    elif height%2 == 0:

        lengthh = lengths[-1] // 2

        not_rotated = before[-1].copy()

        i = before[-1][-1] + 1

        del not_rotated[0]          
        del not_rotated[-1]          
        not_rotated.append(i)
        before.append(not_rotated.copy())
        i += 1

        for _ in range(lengthh):
            if not rotated[i]:
                del not_rotated[0]          
                not_rotated.append(i)
                before.append(not_rotated.copy())       
            else:
                del not_rotated[0]          
                del not_rotated[0]          
                before.append(not_rotated.copy())
                before[-1].append(i)
            i += 1
    


        j = before[-1][-1] + 1

        del not_rotated[0]          
        del not_rotated[-1]          
        not_rotated.append(j)
        before.append(not_rotated.copy())
        j += 1

        for _ in range(lengthh - 2):
            del not_rotated[0]          
            del not_rotated[-1]          
            del not_rotated[-1]          
            not_rotated.append(j)
            before.append(not_rotated.copy())
            j += 1

        del before[-1][-1]
        del before[-1][-1]
    
    else:
    
    
        j = before[-1][-1] + 1

        del not_rotated[0]          
        del not_rotated[-1]          
        not_rotated.append(j)
        before.append(not_rotated.copy())
        j += 1

        for _ in range(lengths[-1] - 1):
            del not_rotated[0]          
            del not_rotated[-1]          
            del not_rotated[-1]          
            not_rotated.append(j)
            before.append(not_rotated.copy())
            j += 1

        del before[-1][-1]
        del before[-1][-1]
      
    assert(len(before) == length)
    assert(before[-1] == [])

    return before

if __name__ == '__main__':
    
    width = 7
    height = 7


    length = width * height
      
    rotated = generate_rotated(width, height, length)

    frame_index, rotation_index = generate_frame_index(rotated)

    not_rotated = generate_not_rotated(rotated, length, height, frame_index)

    
