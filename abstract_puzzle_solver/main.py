from argv_helper import get_from_argvs
import sys
from random_piece_generator import RandomPieceGenerator
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPieceGenerator, PieceKeyCountsPiece
from iter_piece_key_counts_piece import IterPieceKeyCountsPiece
from typing import List
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

    last_forward = 0

    node_count_piece = 0
    node_count_counts = 0
    continue_count = 0

    if len(pieces) > 0: 
        last_solution_time: float = 0
        
        stack:List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(pieces[0], solution_count)]

        while len(stack) > 0:
            piece:IterPieceKeyCountsPiece = stack[-1]

            if piece.index > 0:
                if solution_count == piece.solutions_count:
                    new_node_count_piece, _  = piece.piece_key_counts_piece.insert(piece.insert_index)
                    node_count_piece += new_node_count_piece
                else:
                    piece.solutions_count = solution_count

            else:
                pass
            
            if piece.next():
                forward: PieceKeyCountsPiece|None = piece.piece_key_counts_piece.forward
                
                if forward:
                    new_node_count_counts, index =  counts.insert_counts()

                    node_count_counts += new_node_count_counts

                    piece.insert_index = index

                    if new_node_count_counts == 0:
    
                        ok , leaf = piece.piece_key_counts_piece.check()

                        if ok:
                            assert leaf is not None

                            if index in leaf.object:
                                print(TOP_LLEFT)
                                print(f'{node_count_piece}:{node_count_counts}:{continue_count}:{solution_count}:{int(time() - start)}:{last_solution_time}')
                                continue_count += 1
                                continue
                            else:
                                leaf.object.append(index)
                        else:
                            assert leaf is None
                    
                    piece:IterPieceKeyCountsPiece = IterPieceKeyCountsPiece(forward, solution_count)
                    stack.append(piece)

                    index = forward.coordinate.index
                    if index > last_forward:
                        last_forward = index
                else:
                    solution_count += 1
                    last_solution_time = time() - start
                    assert not piece.next()
                    stack.pop()
            else:
                stack.pop()
        
        print(TOP_LLEFT)
        print(f'{node_count_piece}:{node_count_counts}:{continue_count}:{solution_count}:{time() - start}:{last_solution_time}')
             
 
main()