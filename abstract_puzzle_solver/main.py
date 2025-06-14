from argv_helper import get_from_argvs
import sys
from random_piece_generator import RandomPieceGenerator
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPieceGenerator, PieceKeyCountsPiece
from iter_piece_key_counts_piece import IterPieceKeyCountsPiece
from typing import List, Tuple
from piece_keys import PIECE_KEYS
from piece_key_piece_print_positions import escape_position
from os import system
from time import time
    
TOP_LLEFT = escape_position(1,1)

def main():

    system('clear')
    print(TOP_LLEFT)

    start: float  = time()

    current_argv = sys.argv
   
    width, height, = get_from_argvs(current_argv)

    random: RandomPieceGenerator = RandomPieceGenerator(width, height, firts_frame_piece_keys=[PIECE_KEYS[0]], piece_keys=[p for p in PIECE_KEYS if '0' not in p])

    counts: PieceKeyCounts  = PieceKeyCounts(piece_key_groups_counts_sum(random.pieces))
    first_frame: List[str]  = [p.inital_piece_key for p in random.spiral if p.frame_index == 0]

    generated_pieces: PieceKeyCountsPieceGenerator = PieceKeyCountsPieceGenerator(width, height, first_frame, counts.asterisk_piece_key_counts)

    pieces : List[PieceKeyCountsPiece] = generated_pieces.pieces

    solution_count = 0
    node_count_piece = 0
    node_count_counts = 0
    visited_before_count = 0

    if len(pieces) > 1: 
        
        last_solution_time: float = 0
        forward_stack:List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(pieces[0], solution_count)]
        assert pieces[0].forward
        while len(forward_stack) > 0:
            
            piece:IterPieceKeyCountsPiece = forward_stack[-1]  
            
            if piece.next(solution_count):

                node_count_piece += piece.node_count_piece
                new_node_count_counts, index =  counts.insert_counts()
                node_count_counts += new_node_count_counts
                
                if piece.has_visited_befor(index, new_node_count_counts):
                    print(TOP_LLEFT)
                    print(f'{node_count_piece + piece.node_count_piece}:{node_count_counts}:{visited_before_count}:{solution_count}:{int(time() - start)}:{last_solution_time}')
                    visited_before_count += 1
                    continue
                
                assert piece.piece_key_counts_piece.forward is not None
                
                forward: PieceKeyCountsPiece = piece.piece_key_counts_piece.forward
                piece:IterPieceKeyCountsPiece = IterPieceKeyCountsPiece(forward, solution_count)

                if forward.forward:
                    forward_stack.append(piece)
                elif piece.next(solution_count):
                    solution_count += 1
                    last_solution_time = time() - start
                    assert not piece.next(solution_count)
            else:
                node_count_piece += piece.node_count_piece
                forward_stack.pop()
        
        print(TOP_LLEFT)
        print(f'{node_count_piece}:{node_count_counts}:{visited_before_count}:{solution_count}:{time() - start}:{last_solution_time}')
             
def has_visited_before(counts: PieceKeyCounts, piece: IterPieceKeyCountsPiece) -> Tuple[bool, int]:

    new_node_count_counts, index =  counts.insert_counts()

    return piece.has_visited_befor(index, new_node_count_counts), new_node_count_counts

main()