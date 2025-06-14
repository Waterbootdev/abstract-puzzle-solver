from piece_key_counts_piece import PieceKeyCountsPiece
class IterPieceKeyCountsPiece:
    def __init__(self, piece_key_counts_piece: PieceKeyCountsPiece, solutions_count: int) -> None:
        self.index = 0
        self.insert_index = 0
        self.solutions_count = solutions_count
        self.piece_key_counts_piece = piece_key_counts_piece
        self.node_count_piece = 0
        
        self.piece_key_counts = [count for count in piece_key_counts_piece.current_piece_key_counts() if count.piece_key_group_count.current_count > 0]
        
        if len(self.piece_key_counts) > 0:
            self.piece_key_counts_piece.init_down_keys()
      
    def next(self, solution_count: int) -> bool:

        if self.index < len(self.piece_key_counts):
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
        
    def update(self, solution_count: int): 
        
        if solution_count == self.solutions_count and not self.contaned:
            self.node_count_piece, _ = self.piece_key_counts_piece.insert(self.insert_index)
        else:
            self.solutions_count = solution_count
            
        piece_key_count = self.piece_key_counts[self.index -1]
        piece_key_count.piece_key_group_count.current_count += 1
        
    def has_visited_befor(self, index: int, new_node_count_counts: int) -> bool:

        self.insert_index = index
   
        if new_node_count_counts == 0:
      
            contaned, appended = self.piece_key_counts_piece.contains(index)

            self.contaned = contaned
        
            return contaned and not appended # if False else False
    
        else:
            self.contaned = False
            return False



    def __repr__(self) -> str:
        return f'{self.piece_key_counts_piece}:{self.index}/{len(self.piece_key_counts)}'