from argv_helper import get_from_argvs
import sys
from random_piece_generator import RandomPieceGenerator
from typing import List
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPieceGenerator, PieceKeyCountsPiece
from piece_keys import PIECE_KEYS
from os import system
from solution_searcher import SolutionSearcher
from piece_key_piece_print_positions import escape_position
from insert_node_value import InsertNodeValue





FIRST_LINE = escape_position(3,1)
SECOND_LINE = escape_position(5,1)
    
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

    insert_node_values: List[InsertNodeValue] = []

    first_hex_length: int = 0
    second_hex_length: int = 0

    insert_count = 0

    max_count = 0
    max_hex: str = ''

    def append(piece_keys:List[str], insert_node_value: InsertNodeValue):
        nonlocal piece_key_ints
        nonlocal solutions_count
        nonlocal insert_node_values
        nonlocal first_hex_length
        nonlocal second_hex_length
        nonlocal insert_count
        nonlocal max_count
        nonlocal max_hex
        insert_count += 1
        piece_key_str: str = ''.join(piece_keys)
        piece_key_int: int = int(piece_key_str, base=3)
        piece_key_ints.append(piece_key_int)
        insert_node_values.append(insert_node_value)
        piece_key_hex: str = hex(piece_key_int)
        
        
        if insert_node_value.count > 0:
            if insert_node_value.count > max_count:
                max_count = insert_node_value.count
                max_hex = str(piece_keys)
                hex_length = len(max_hex)
                if hex_length < second_hex_length:
                    max_hex += ' ' * (second_hex_length - hex_length)
                
                second_hex_length = hex_length
           
            solutions_count += insert_node_value.count
         
            print(SECOND_LINE)
            print(f'{max_count}:{insert_count}/{solutions_count}:{max_hex}')
        
        else:
            hex_length = len(piece_key_hex)
       
            solutions_count += 1
            
            if hex_length < first_hex_length:
                piece_key_hex += ' ' * (first_hex_length - hex_length)
            
            first_hex_length = hex_length
            
            print(FIRST_LINE)
            print(f'{insert_count}/{solutions_count}:{piece_key_hex}')
              
    searcher = SolutionSearcher(counts, pieces, append)
    
    searcher.search(True)

    print(escape_position(7,1))
    print((solutions_count * width * height * 4)/1024/1024/1024)

main()