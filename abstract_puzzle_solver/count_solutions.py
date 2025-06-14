from iter_piece_key_counts_piece import IterPieceKeyCountsPiece

from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPiece
from piece_key_piece_print_positions import escape_position

from time import time
from typing import List

TOP_LEFT = escape_position(1,1)

def count_solutions(counts: PieceKeyCounts, pieces: List[PieceKeyCountsPiece]):
    start: float  = time()

    solution_count = 0
    node_count_piece = 0
    node_count_counts = 0
    visited_before_count = 0
    pop_count = 0

    if len(pieces) > 1:
        last_solution_time: float = 0
        forward_stack: List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(pieces[0], solution_count)]
        assert pieces[0].forward
        while len(forward_stack) > 0:
            piece: IterPieceKeyCountsPiece = forward_stack[-1]

            if piece.next(solution_count):
                node_count_piece += piece.node_count_piece
                new_node_count_counts, index =  counts.insert_counts()
                node_count_counts += new_node_count_counts

                if piece.has_visited_befor(index, new_node_count_counts):
                    print(TOP_LEFT)
                    print(f'{node_count_piece + piece.node_count_piece}:{node_count_counts}:{visited_before_count}:{pop_count}:{solution_count}:{int(time() - start)}:{last_solution_time}')
                    visited_before_count += 1
                    continue

                assert piece.piece_key_counts_piece.forward is not None

                forward: PieceKeyCountsPiece = piece.piece_key_counts_piece.forward
                piece: IterPieceKeyCountsPiece = IterPieceKeyCountsPiece(forward, solution_count)

                if forward.forward:
                    forward_stack.append(piece)
                elif piece.next(solution_count):
                    solution_count += 1
                    last_solution_time = time() - start
            else:
                node_count_piece += piece.node_count_piece
                pop_count += 1
                forward_stack.pop()

        print(TOP_LEFT)
        print(f'{node_count_piece}:{node_count_counts}:{visited_before_count}:{pop_count}:{solution_count}:{time() - start}:{last_solution_time}')