from iter_piece_key_counts_piece import IterPieceKeyCountsPiece
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPiece
from typing import List
from collections.abc import Callable
from piece_key_piece_print_positions import escape_position
from insert_node_value import InsertNodeValue

TOP_LEFT = escape_position(1,1)

class SolutionSearcher:

    def __init__(self, counts: PieceKeyCounts, pieces: List[PieceKeyCountsPiece], append_solution: Callable[[int, int], int], append_solution_with_prefix: Callable[[int, int, InsertNodeValue], int]) -> None:
        if len(pieces) < 1:
            raise ValueError()
        
        self.counts: PieceKeyCounts = counts
        self.stack_index: int = -1
        self.search_stack: List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(piece) for piece in pieces]
        self.stack_length: int = len(self.search_stack)
        self.last_stack_index: int = self.stack_length - 1
        self.solutions:List[List[str]] = []
        self.searched = False
        self.append_solution = append_solution
        self.append_solution_with_prefix = append_solution_with_prefix  
        self.visited_before_count: int = 0
        self.first_index = self.search_stack[0].piece_key_counts_piece.coordinate.index

    def decrement(self) -> IterPieceKeyCountsPiece:
        self.stack_index -= 1
        piece = self.search_stack[self.stack_index]
        return piece

    def increment(self, solutions_count: int) -> IterPieceKeyCountsPiece:
        self.stack_index += 1
        piece = self.search_stack[self.stack_index]
        piece.init(solutions_count)
        return piece

    def has_not_visited_before(self, piece: IterPieceKeyCountsPiece) -> bool:
        new_node_count_counts, index =  self.counts.insert_counts()
        return not piece.has_visited_before(index, new_node_count_counts)

     
    def search(self, print_visited_before_count: bool = False) -> None:
        if self.searched:
            raise Exception("can't serach twice")
        solutions_count: int = 0
        piece: IterPieceKeyCountsPiece = self.increment(solutions_count)
        while self.stack_index >= 0:                 
            if piece.next(solutions_count):
                if self.stack_index < self.last_stack_index:
                    if self.has_not_visited_before(piece):
                        piece = self.increment(solutions_count)
                    else:

                        assert piece.insert_node is not None

                        insert_node_value = piece.insert_node.get_value(piece.insert_index)

                        if insert_node_value is not None:
                            assert insert_node_value.count > 0
                            solutions_count = self.append_solution_with_prefix(solutions_count, self.stack_index, insert_node_value)
           
                        self.visited_before_count += 1
                        
                        if print_visited_before_count:
                            print(TOP_LEFT)
                            print(f'{solutions_count}:{self.counts.current_index}:{self.visited_before_count}')
                else:
                    solutions_count = self.append_solution(solutions_count, self.stack_index)
                    piece.last_next()
                    piece = self.decrement()
            else:
                piece = self.decrement()
        self.searched

    