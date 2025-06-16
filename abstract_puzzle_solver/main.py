from argv_helper import get_from_argvs
import sys
from piece_key_constants import PIECE_KEY_BASE
from random_piece_generator import RandomPieceGenerator
from typing import List, Any
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPieceGenerator, PieceKeyCountsPiece
from piece_keys import PIECE_KEYS
from os import system
from solution_searcher import SolutionSearcher
from piece_key_piece_print_positions import escape_position




TOP_LEFT = escape_position(2,1)
    
def main():

    system('clear')

    current_argv = sys.argv
   
    width, height, = get_from_argvs(current_argv)

    random: RandomPieceGenerator = RandomPieceGenerator(width, height, firts_frame_piece_keys=[PIECE_KEYS[0]], piece_keys=[p for p in PIECE_KEYS if '0' not in p])

    counts: PieceKeyCounts  = PieceKeyCounts(piece_key_groups_counts_sum(random.pieces))
    first_frame: List[str]  = [p.inital_piece_key for p in random.spiral if p.frame_index == 0]

    generated_pieces: PieceKeyCountsPieceGenerator = PieceKeyCountsPieceGenerator(width, height, first_frame, counts.asterisk_piece_key_counts)

    pieces : List[PieceKeyCountsPiece] = generated_pieces.pieces
   
    solutions_count: int = 0

    piece_key_ints: List[int] = []

    piece_key_trie: List[Any|None] = [None]*PIECE_KEY_BASE 

    def append(piece_keys:List[str]):
        nonlocal piece_key_ints
        nonlocal solutions_count
        nonlocal piece_key_trie
        solutions_count += 1
        piece_key_str: str = ''.join(piece_keys)
        piece_key_int: int = int(piece_key_str, base=3)

        current: Any  = piece_key_trie
        for piece_key in piece_keys:
            for piece_key_digit in piece_key:
                id = int(piece_key_digit)
                if current[id] is None:
                    current[id] = [None]*PIECE_KEY_BASE
                current = current[id]
    
        piece_key_ints.append(piece_key_int)
        print(TOP_LEFT)
        print(f'{solutions_count}:{hex(piece_key_int)}')
            
    searcher = SolutionSearcher(counts, pieces, append)
    
    searcher.search(True)

    print(escape_position(3,1))
    print(solutions_count)


    

    
main()