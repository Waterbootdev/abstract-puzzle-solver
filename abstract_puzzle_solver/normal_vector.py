from typing import Tuple

class NormalVector:
    def __init__(self, x: int = 0, y: int = 0) -> None:

        if (x == 0 and y == 0) or (x != 0 and y != 0):
            raise ValueError()

        self.x = NormalVector.normalize(x)
        self.y = NormalVector.normalize(y)

    def __repr__(self) -> str:
        return f'[{self.x}, {self.y}]'
    
    @staticmethod
    def normalize(v: int):
        return 0 if v == 0 else 1 if v > 0 else -1
          
    def rotate_cw(self):
        if self.x == 0:
            self.x = self.y
            self.y = 0
        else:
            self.y = -self.x
            self.x = 0 

    def rotate_ccw(self):
        if self.x == 0:
            self.x = -self.y
            self.y = 0
        else:
            self.y = self.x
            self.x = 0

    def add_to(self, x: int , y: int)-> Tuple[int, int]:
        return x + self.x, y + self.y

    def subtract_from(self, x: int , y: int)-> Tuple[int, int]:
        return x - self.x, y - self.y
        