from random_piece_generator import RandomPieceGenerator
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPieceGenerator, PieceKeyCountsPiece
from iter_piece_key_counts_piece import IterPieceKeyCountsPiece
from os import system
from typing import List

def main():
    width = 10
    height = 10

    random: RandomPieceGenerator = RandomPieceGenerator(width, height)

    counts: PieceKeyCounts  = PieceKeyCounts(piece_key_groups_counts_sum(random.pieces))
    first_frame: List[str]  = [p.inital_piece_key for p in random.spiral if p.frame_index == 0]

    generated_pieces: PieceKeyCountsPieceGenerator = PieceKeyCountsPieceGenerator(width, height, first_frame, counts.asterisk_piece_key_counts)

    pieces : List[PieceKeyCountsPiece] = generated_pieces.pieces

    solution_count = 0


    if len(pieces) > 0:    
        stack:List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(pieces[0])]

        while len(stack) > 0:
            piece:IterPieceKeyCountsPiece = stack[-1]
            if piece.next():
                forward: PieceKeyCountsPiece|None = piece.piece_key_counts_piece.forward
                if forward:
                    stack.append(IterPieceKeyCountsPiece(forward))
                else:
                    solution_count += 1
                    system('clear')
                    print(solution_count)
            else:
                stack.pop()

if __name__ == '__main__':
    main()

            








main()