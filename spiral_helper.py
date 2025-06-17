from itertools import chain
from copy import copy
from directions import Ring, DIRECTIONSLISTLIST, Directions
from coordinate import Coordinate
from spiral__helper import List, generate_coordinates, incremented_coordinate, generate_links, decrement_coordinates
from typing import Tuple
from edge import Edge, LEFT_UP, LEFT_UP_RIGHT, LEFT_UP_DOWN, LEFT_UP_RIGHT_DOWN

def generate_rotated(width: int, height: int, length: int) -> List[bool]:

    if height > width or width < 2 or height < 2:
        raise Exception()
    
    right = width
    down = height - 1
    left = width - 1
    up = height - 2

    step_counts = []

    if height == 2:
        step_counts = [right, down, left] 
    else:
        frame = [right, down, left, up]
    
        step_counts = copy(frame)

        while frame[-1] > 2:
            frame = [steps - 2 for steps in frame]
            step_counts.extend(frame)

        (last_right, last_down, last_left, last_up) = tuple(frame)

        match last_up:
            case 1:
                step_counts.append(last_right - 2)
            case 2:
                step_counts.extend([last_right - 2, last_down - 2, last_left -2])
            case _:
                pass
    
    rotated = list(chain.from_iterable(map(lambda steps_without_rotation : [False for _ in range(steps_without_rotation - 1)] + [True], step_counts)))

    rotated[-1] = False

    assert length == width * height
    return rotated    

def generate_frame_index(rotated: List[bool]) -> Tuple[List[int], List[int]]:
    frame_index = 0
    rotation_index = 0
    frame_indexes: List[int] = []
    rotation_indexes: List[int] = []

    for rotate in rotated:
        current_frame_index = frame_index
        current_rotation_index = rotation_index
        
        if rotate:
            if rotation_index < 3:
                rotation_index += 1
            else:
                rotation_index = 0
                frame_index += 1
        
        frame_indexes.append(current_frame_index)
        rotation_indexes.append(current_rotation_index)

    return frame_indexes, rotation_indexes 

def generate_directions(rotated: List[bool]) -> List[List[Directions]]:
    ring = Ring[List[Directions]](DIRECTIONSLISTLIST)
   
    def generate(step_rotate: bool):
        current = ring.current()
        if step_rotate:
            ring.forward()
        return current

    return list(map(generate, rotated))
 
def generate_coordinates_and_links(width: int, height: int, rotated: List[bool],  directions: List[List[Directions]]) -> Tuple[List[Coordinate], List[List[int|None]]]:

    coordinates = generate_coordinates(incremented_coordinate(), rotated, directions)

    generated_links = generate_links(width, height, directions, coordinates)

    return decrement_coordinates(coordinates), generated_links

def generate_forward(length: int) -> List[int|None]:
    last = length - 1
    return[None if i == last else i + 1 for i in range(length)]

def generate_backward(length: int) -> List[int|None]:
    return[None if i == 0 else i - 1 for i in range(length)]

def generate_turns(rotated: List[bool]) -> List[int]:
    turns: List[int] = []
    for index, rotate in enumerate(rotated):
        if rotate:
            turns.append(index)
    return turns

def generate_edges(length: int, turns: List[int]) -> List[List[Edge]]:

    edges: List[List[Edge]] = [LEFT_UP for _ in range(length)]

    for index in turns:
        edges[index] = LEFT_UP_RIGHT

    for index in range(turns[-1] + 1, length - 1):
        edges[index] = LEFT_UP_DOWN

    edges[-1] = LEFT_UP_RIGHT_DOWN 

    return edges