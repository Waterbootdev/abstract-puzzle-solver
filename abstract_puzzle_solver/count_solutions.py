from iter_piece_key_counts_piece import IterPieceKeyCountsPiece
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPiece
from piece_key_piece_print_positions import escape_position
from time import time
from typing import List, Tuple

TOP_LEFT = escape_position(1,1)

def count_solutions(counts: PieceKeyCounts, pieces: List[PieceKeyCountsPiece]) -> int:
    start: float  = time()
    solutions_count: int = 0
    node_count_piece: int = 0
    node_count_counts: int = 0
    visited_before_count: int = 0

    if len(pieces) > 1:
        last_solution_time: float = 0

        forward_stack: List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(piece) for piece in pieces]
        stack_index: int = 0
        stack_length: int = len(forward_stack)
        last_stack_index: int = stack_length - 1
        piece: IterPieceKeyCountsPiece = forward_stack[0]
        piece.init(solutions_count)

        while stack_index >= 0:
    
            if piece.next(solutions_count):

                if stack_index < last_stack_index:

                    node_count_piece += piece.node_count_piece
                    new_node_count_counts, index =  counts.insert_counts()
                    node_count_counts += new_node_count_counts

                    if piece.has_visited_before(index, new_node_count_counts):
                        print(TOP_LEFT)
                        print(f'{node_count_piece}:{node_count_counts}:{visited_before_count}:{solutions_count}:{int(time() - start)}:{last_solution_time}')
                        visited_before_count += 1
                        pass
                    else:
                        stack_index, piece = increment(stack_index, solutions_count, forward_stack)
                else:
                    solutions_count += 1
                    last_solution_time = time() - start
                    node_count_piece += piece.node_count_piece
                
                    piece.last_next()
                    
                    stack_index, piece = decrement(stack_index, forward_stack)                
            else:
                node_count_piece += piece.node_count_piece
                stack_index, piece = decrement(stack_index, forward_stack)                
               


        print(TOP_LEFT)
        print(f'{node_count_piece}:{node_count_counts}:{visited_before_count}:{solutions_count}:{time() - start}:{last_solution_time}')
    
    return solutions_count

def decrement(stack_index: int, forward_stack: List[IterPieceKeyCountsPiece]) -> Tuple[int, IterPieceKeyCountsPiece]:
    stack_index -= 1
    piece: IterPieceKeyCountsPiece = forward_stack[stack_index]
    return stack_index, piece

def increment(stack_index: int, solution_count: int, forward_stack: List[IterPieceKeyCountsPiece]) -> Tuple[int, IterPieceKeyCountsPiece]:
    stack_index += 1
    piece: IterPieceKeyCountsPiece = forward_stack[stack_index]
    piece.init(solution_count)
    return stack_index ,piece