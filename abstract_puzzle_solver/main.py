from random_piece_generator import RandomPieceGenerator
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPieceGenerator, PieceKeyCountsPiece
from iter_piece_key_counts_piece import IterPieceKeyCountsPiece
from typing import List, Set
from piece_keys import PIECE_KEYS

def main():
    width = 6
    height = 5

    random: RandomPieceGenerator = RandomPieceGenerator(width, height, firts_frame_piece_keys=[PIECE_KEYS[0]], piece_keys=[p for p in PIECE_KEYS if '0' not in p])

    counts: PieceKeyCounts  = PieceKeyCounts(piece_key_groups_counts_sum(random.pieces))
    first_frame: List[str]  = [p.inital_piece_key for p in random.spiral if p.frame_index == 0]

    generated_pieces: PieceKeyCountsPieceGenerator = PieceKeyCountsPieceGenerator(width, height, first_frame, counts.asterisk_piece_key_counts)

    pieces : List[PieceKeyCountsPiece] = generated_pieces.pieces

    solution_count = 0

    lasts: Set[str] = set()


    if len(pieces) > 0:    
        stack:List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(pieces[0])]

        while len(stack) > 0:
            piece:IterPieceKeyCountsPiece = stack[-1]
            if piece.next():
                forward: PieceKeyCountsPiece|None = piece.piece_key_counts_piece.forward
                if forward:
                    piece:IterPieceKeyCountsPiece = IterPieceKeyCountsPiece(forward)
                    stack.append(piece)
                else:
                    solution_count += 1
                    lasts.add(piece.piece_key_counts[0].piece_key_group_count.piece_groups_key)
                    print(len(lasts))
            else:
                stack.pop()

 
main()