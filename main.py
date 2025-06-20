from argv_helper import get_from_argvs
import sys
from random_piece_generator import RandomPieceGenerator
from typing import List
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_counts import PieceKeyCounts
from piece_key_counts_piece_generator import PieceKeyCountsPieceGenerator, PieceKeyCountsPiece
from piece_keys import PIECE_KEYS
from os import system,path
from piece_key_piece_print_positions import escape_position
from solutions_saver import save_solutions
from pathlib import Path

DRIVE = "/mnt/g"

FIRST_LINE = escape_position(3,1)
SECOND_LINE = escape_position(5,1)
    
def main():

    system('clear')

    current_argv = sys.argv
   
    width, height, subdirctory = get_from_argvs(current_argv)

    directory_path_name = path.join(DRIVE, subdirctory)

    directory_path: Path = Path(directory_path_name)

    if not directory_path.exists():
        directory_path.mkdir()

    random: RandomPieceGenerator = RandomPieceGenerator(width, height, firts_frame_piece_keys=[PIECE_KEYS[0]], piece_keys=[p for p in PIECE_KEYS if '0' not in p])

    counts: PieceKeyCounts  = PieceKeyCounts(piece_key_groups_counts_sum(random.pieces))
    first_frame: List[str]  = [p.inital_piece_key for p in random.spiral if p.frame_index == 0]

    generated_pieces: PieceKeyCountsPieceGenerator = PieceKeyCountsPieceGenerator(width, height, first_frame, counts.asterisk_piece_key_counts)

    pieces : List[PieceKeyCountsPiece] = generated_pieces.pieces

    save_solutions(directory_path_name, counts, pieces)

main()