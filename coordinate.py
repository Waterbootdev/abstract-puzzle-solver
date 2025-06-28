from directions import Directions
from typing import List, TypeVar

T = TypeVar("T")

class Coordinate:

    def __init__(self) -> None:
        self.index: int = 0
        self.x: int = 0
        self.y: int = 0

    def __repr__(self) -> str:
        return f"[{self.index}, [{self.x}, {self.y}]]"
    
    def increment(self):
        self.x += 1
        self.y += 1

    def decrement(self):
        self.x -= 1
        self.y -= 1

    def right(self, directions: Directions):
        return directions.x.add_to(self.x, self.y)
    
    def left(self, directions: Directions):
        return directions.x.subtract_from(self.x, self.y)
    
    def up(self, directions: Directions):
        return directions.y.subtract_from(self.x, self.y)
    
    def down(self, directions: Directions):
        return directions.y.add_to(self.x, self.y)

    def matrix_left[T](self, matrix: List[List[T]], directions: Directions):
        x, y = self.left(directions)
        return matrix[x][y]
    
    def matrix_up[T](self, matrix: List[List[T]], directions: Directions):
        x, y = self.up(directions)
        return matrix[x][y]

    def matrix_right[T](self, matrix: List[List[T]], directions: Directions):
        x, y = self.right(directions)
        return matrix[x][y]
    
    def matrix_down[T](self, matrix: List[List[T]] , directions: Directions):
        x, y = self.down(directions)
        return matrix[x][y]
    
    def set_to_matrix(self, matrix: List[List[int|None]]) -> None:
        matrix[self.x][self.y]= self.index
    
    def get_from_matrix[T](self, matrix: List[List[T]]):
        return matrix[self.x][self.y]
        
    def step_right(self, directions: Directions):
        self.index += 1
        self.x, self.y = self.right(directions)
    
    def step_down(self, directions: Directions):
        self.index += 1
        self.x, self.y = self.down(directions)
    
    def step_left(self, directions: Directions):
        self.index -= 1
        self.x, self.y = self.left(directions)
    
    def step_right_down(self, directions: Directions):
        self.x, self.y = self.right(directions)
        self.x, self.y = self.down(directions)

    def scale_add(self, scale_factor_x: int, scale_factor_y: int, x: int, y: int):
        coordinate = Coordinate()
        coordinate.index = self.index
        coordinate.x = scale_factor_x * self.x + x
        coordinate.y = scale_factor_y * self.y + y        
        return coordinate


    
      


        
    
