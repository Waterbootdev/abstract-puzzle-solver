from random_piece_key_piece import List, RandomPieceKeyPiece, Directions, Coordinate, PieceKeyPiece, Edge
from piece_generator import PieceGenerator
from print_positions import PrintPositions, DEFAULT_PRINT_POSITIONS
from opposite_piece_keys import DEFAULT_OPPOSITE_KEY

class RandomPieceGenerator(PieceGenerator[RandomPieceKeyPiece]):
    
    def __init__(self, number_columns: int, number_rows: int, print_positions: PrintPositions=DEFAULT_PRINT_POSITIONS, opposite_key: str=DEFAULT_OPPOSITE_KEY) -> None:
       
        if number_rows > number_columns or number_columns < 0:
            raise ValueError() 
       
        super().__init__(number_columns + 2, number_rows + 2)
        
        def new_piece(frame_index: int, rotation_index: int, rotated: bool, directions: List[Directions], coordinate: Coordinate, edges: List[Edge]) -> RandomPieceKeyPiece:
            return RandomPieceKeyPiece(opposite_key, print_positions.print_positions, frame_index, rotation_index, rotated, directions, coordinate, edges)

        spiral: List[RandomPieceKeyPiece] = self.generate(new_piece)
       
        self.pieces: List[RandomPieceKeyPiece] = [piece for piece  in spiral if piece.frame_index > 0]

        for piece in self.pieces:
            piece.fit_piece()

        self.spiral: List[RandomPieceKeyPiece] = spiral
    
        self.border:  List[RandomPieceKeyPiece] = [piece for piece  in spiral if piece.coordinate.index > 0 and piece.frame_index == 0 and not piece.rotated]
        
        if len(self.pieces) == 0:
            del self.border[-1]      
        else:
            self.border.append(spiral[self.turns[3]])

                             
    def bottom_right(self) -> PieceKeyPiece:
        return self.spiral[self.turns[1]]
        
if __name__ == '__main__':
    pass