from edge import Edge, NUMBER_EDGES, LEFT_UP_RIGHT_DOWN
from typing import List

def generation_rotation_matrix() -> List[List[List[Edge]]]:
        
    identity = LEFT_UP_RIGHT_DOWN
    rotations =[identity[rotation_index:] + identity[:rotation_index]  for rotation_index in range(NUMBER_EDGES)]
    rotation_matrix: List[List[List[Edge]]] = [[[] for _ in range(NUMBER_EDGES)] for _ in range(NUMBER_EDGES)]
    for first in range(NUMBER_EDGES):
        for second in range(NUMBER_EDGES):
            rotation_index = second - first
            if rotation_index < 0:
                rotation_index += NUMBER_EDGES
            rotation_matrix[first][second]= rotations[rotation_index]
    return rotation_matrix 

INDEX_ROTATION_MATRIX: List[List[List[Edge]]] = generation_rotation_matrix()
    

       