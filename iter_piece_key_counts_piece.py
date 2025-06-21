from piece_key_constants import MAX_NUMBER_PIECE_KEYS
from piece_key_count import PieceKeyCount, copy_piece_key_counts_greater_zero
from piece_key_counts_piece import PieceKeyCountsPiece
from piece_key_group_count import PieceKeyGroupCount
from insert_node_value import InsertNodeValue
from typing import List

from extra_piece import ExtraPieceKeyCountsPiece
from typing import TypeVar, Generic

T = TypeVar('T', PieceKeyCountsPiece, ExtraPieceKeyCountsPiece)


class IterPieceKeyCountsPiece(Generic[T]):
    DUMMY_PIECE_KEY_COUNT: PieceKeyCount = PieceKeyCount('', PieceKeyGroupCount('', 0)) 

    def __init__(self, piece_key_counts_piece: T) -> None:
        self.index = 0
        self.insert_index = 0
        self.solutions_count = 0
        self.piece_key_counts_piece = piece_key_counts_piece
        self.node_count_piece = 0
        self.contaned = False
        self.piece_key_counts: List[PieceKeyCount] = [IterPieceKeyCountsPiece.DUMMY_PIECE_KEY_COUNT]*MAX_NUMBER_PIECE_KEYS
        self.length = 0
        self.insert_node = None


    def init(self, solutions_count: int) -> None:
        self.index = 0
        self.insert_index = 0
        self.solutions_count = solutions_count
        self.node_count_piece = 0
        self.contaned = False
        self.insert_node = None
        self.length = copy_piece_key_counts_greater_zero(self.piece_key_counts_piece.current_piece_key_counts(), self.piece_key_counts)
        if self.length > 0:
            self.piece_key_counts_piece.init_down_keys()
        
    def next(self, solution_count: int) -> bool:

        if self.index < self.length:
            if self.index > 0:
                self.update(solution_count)
            piece_key_count = self.piece_key_counts[self.index]
            piece_key_count.piece_key_group_count.current_count -= 1
            self.piece_key_counts_piece.set_piece_key(piece_key_count.piece_key)
            self.index += 1
            return True
        else:
            if self.index > 0:
                self.update(solution_count)
            return False
    
    def last_next(self) -> None:
        self.piece_key_counts[0].piece_key_group_count.current_count += 1
              
    def update(self, solution_count: int):

        assert self.insert_node is not None

        if not self.contaned:    
            if solution_count == self.solutions_count:
                self.insert_node.append_index(self.insert_index, None)
            else:
                self.insert_node.append_index(self.insert_index, InsertNodeValue(self.solutions_count, solution_count))
        
        self.solutions_count = solution_count
            
        self.piece_key_counts[self.index - 1].piece_key_group_count.current_count += 1
        
    def has_visited_before(self, index: int, new_node_count_counts: int) -> bool:

        self.insert_index = index
   
        self.insert_node = self.piece_key_counts_piece.insert_node()
      
        self.contaned = self.insert_node.contains_index(index)
         
        return self.contaned and new_node_count_counts == 0
     
    def __repr__(self) -> str:
        return f'{self.piece_key_counts_piece}:{self.index}/{self.length}'