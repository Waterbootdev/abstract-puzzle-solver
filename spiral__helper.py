from coordinate import Coordinate
from directions import Directions
from itertools import starmap
from copy import copy
from typing import List    

def decrement_coordinates(coordinates: List[Coordinate]) -> List[Coordinate]:
    for coordinate in coordinates:
        coordinate.decrement()
    return coordinates

def generate_coordinates(coordinate: Coordinate, rotated: List[bool], directions: List[List[Directions]]) -> List[Coordinate]:
    
    def step(rotate: bool, directions: List[Directions]):
        save = copy(coordinate)
        direction = directions[0]
        if rotate:
            coordinate.step_down(direction)
        else:
            coordinate.step_right(direction)
        return save
    
    return list(starmap(step, zip(rotated, directions)))

def incremented_coordinate() -> Coordinate:
    coordinate = Coordinate()
    coordinate.increment()
    return coordinate


def to_matrix(width: int , height: int, coordinates: List[Coordinate]) -> List[List[int|None]]  :
    matrix: List[List[int|None]] = [[None for _ in range(height + 2)] for _ in range(width + 2)]

    for coordinate in coordinates:
        assert isinstance(coordinate, Coordinate)
        coordinate.set_to_matrix(matrix)
    
    return matrix 


def generate_links(width: int, height: int, directions: List[List[Directions]], coordinates: List[Coordinate]) -> List[List[int|None]]:
    matrix = to_matrix(width, height, coordinates)
    
    def links(coordinate: Coordinate, directions: List[Directions]) -> List[int|None]:
        return list(map(lambda direction: coordinate.matrix_left(matrix, direction) ,directions))
        
    return list(starmap(links, zip(coordinates, directions)))


