from iter_piece_key_counts_piece import IterPieceKeyCountsPiece
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPiece
from typing import List
from collections.abc import Callable
from piece_key_piece_print_positions import escape_position
from insert_node_value import InsertNodeValue

TOP_LEFT = escape_position(1,1)
ZERO_INSERT_NODE_VALUE = InsertNodeValue(0,0)

class SolutionSearcher:

    def __init__(self, counts: PieceKeyCounts, pieces: List[PieceKeyCountsPiece], append: Callable[[List[str], InsertNodeValue], None]) -> None:
        if len(pieces) < 1:
            raise ValueError()
        
        self.counts: PieceKeyCounts = counts
        self.pieces: List[PieceKeyCountsPiece] = pieces
        self.stack_index: int = -1
        self.search_stack: List[IterPieceKeyCountsPiece] = [IterPieceKeyCountsPiece(piece) for piece in pieces]
        self.stack_length: int = len(self.search_stack)
        self.last_stack_index: int = self.stack_length - 1
        self.solutions:List[List[str]] = []
        self.searched = False
        self.append = append
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

    def append_solution(self, solutions_count: int) -> int:
        self.append([piece.piece_key for piece in  self.pieces], InsertNodeValue(solutions_count, solutions_count))
        solutions_count += 1
        return solutions_count
    
    def search(self, print_visited_before_count: bool = False) -> None:
        if self.searched:
            raise Exception("can't serach twice")
        solutions_count: int = 0
        piece: IterPieceKeyCountsPiece = self.increment(solutions_count)
        while self.stack_index >= 0:
            assert piece.piece_key_counts_piece.coordinate.index == self.stack_index + self.first_index
                     
            if piece.next(solutions_count):
                if self.stack_index < self.last_stack_index:
                    if self.has_not_visited_before(piece):
                        piece = self.increment(solutions_count)
                    else:

                        assert piece.insert_node is not None

                        insert_node_value = piece.insert_node.get_value(piece.insert_index)

                        if insert_node_value is not None:
                            assert insert_node_value.count > 0
                            self.append([piece.piece_key for piece in  self.pieces[:self.stack_index + 1]], insert_node_value)
                            solutions_count += insert_node_value.count
                        
                        self.visited_before_count += 1
                        if print_visited_before_count:
                            print(TOP_LEFT)
                            print(f'{self.counts.current_index}:{self.visited_before_count}')
                else:
                    solutions_count = self.append_solution(solutions_count)
                    piece.last_next()
                    piece = self.decrement()
            else:
                piece = self.decrement()
        self.searched

    