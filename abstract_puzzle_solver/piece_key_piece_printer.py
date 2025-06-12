from escape_color import EscapeColor
from edge import Edge, List,LEFT_UP_RIGHT_DOWN
from printer_helper import print_piece_key_edge, print_initial_piece_key_edge
from piece_key_piece_helper import KeyPiece, PieceKeyPiece
from time import sleep

class PieceKeyPiecePrinter:

    def __init__(self, seconds: float,  red: EscapeColor = EscapeColor.RED, yellow: EscapeColor = EscapeColor.YELLOW, green: EscapeColor = EscapeColor.GREEN, blue: EscapeColor = EscapeColor.BLUE) -> None:        
        self.seconds = seconds
        self.red = red
        self.yellow = yellow
        self.green = green
        self.blue = blue
        self.red_count = 0
        self.green_count = 0

    def print_pieces(self, pieces: List[KeyPiece],  edge : Edge, color: EscapeColor):
        print(color.value)
        for piece in pieces:
            print_piece_key_edge(piece, edge)

    def print_blue(self, piece: PieceKeyPiece):
        print(self.blue.value)
        for edge in LEFT_UP_RIGHT_DOWN:
            print_initial_piece_key_edge(piece, edge)

    def print_yellow(self, piece: PieceKeyPiece):
        print(self.yellow.value)
        for edge in piece.edges:
            print_initial_piece_key_edge(piece, edge)
                
    def print_red_or_green(self, piece: PieceKeyPiece):
        for edge in piece.edges:
            if piece.is_changed(edge):
                print(self.red.value)
                self.red_count += 1

            else:
                print(self.green.value)
                self.green_count += 2
            print_piece_key_edge(piece, edge)
            
    def print_changes(self, pieces: List[KeyPiece]):
        for piece in pieces:
            self.print_blue(piece)
            sleep(self.seconds/2.0)
            self.print_yellow(piece)
            sleep(self.seconds)
            self.print_red_or_green(piece)

    def print_counts(self) -> None:
        PieceKeyPiecePrinter.print_count(self.red, self.red_count)
        PieceKeyPiecePrinter.print_count(self.green, self.green_count)
    
    @staticmethod
    def print_count(color: EscapeColor, count: int) -> None:
        print(color.value)
        print(f'color_count = {count}')
        

if __name__ == '__main__':
   pass

    


        
