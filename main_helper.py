import sys
import time
from collections.abc import Callable
from os import path, system
from pathlib import Path
from resource import RLIMIT_NOFILE, setrlimit
from typing import List, Tuple

import pickle_piece_key_counts_piece_generator
import piece_key_counts_piece_generator
from argv_helper import get_from_argvs
from node_counter import NodeCounter
from piece_key_counts import PieceKeyCounts
from piece_key_counts_pieces import T
from piece_key_piece_helper import piece_key_groups_counts_sum
from piece_key_piece_print_positions import escape_position
from piece_keys import PIECE_KEYS
from random_piece_generator import RandomPieceGenerator
from solutions_saver import save_solutions

DRIVE = "/mnt/g"

FIRST_LINE = escape_position(3, 1)
SECOND_LINE = escape_position(6, 1)


def init_piece_key_counts_piece_generator(width: int, height: int, _: str):
    counts, first_frame, node_counter = init_random(width, height)
    generated_pieces: piece_key_counts_piece_generator.PieceKeyCountsPieceGenerator = (
        piece_key_counts_piece_generator.PieceKeyCountsPieceGenerator(
            width, height, node_counter, first_frame, counts.asterisk_piece_key_counts
        )
    )
    return counts, node_counter, generated_pieces.pieces


def init_pickle_piece_key_counts_piece_generator(
    width: int, height: int, pickle_directory_path_name: str
):
    counts, first_frame, node_counter = init_random(width, height)
    generated_pieces: pickle_piece_key_counts_piece_generator.PieceKeyCountsPieceGenerator = pickle_piece_key_counts_piece_generator.PieceKeyCountsPieceGenerator(
        width,
        height,
        pickle_directory_path_name,
        node_counter,
        first_frame,
        counts.asterisk_piece_key_counts,
    )
    return counts, node_counter, generated_pieces.pieces


def init_random(width: int, height: int):
    random: RandomPieceGenerator = RandomPieceGenerator(
        width,
        height,
        firts_frame_piece_keys=[PIECE_KEYS[0]],
        piece_keys=[p for p in PIECE_KEYS if "0" not in p],
    )
    counts: PieceKeyCounts = PieceKeyCounts(piece_key_groups_counts_sum(random.pieces))
    first_frame: List[str] = [
        p.inital_piece_key for p in random.spiral if p.frame_index == 0
    ]
    node_counter: NodeCounter = NodeCounter()
    return counts, first_frame, node_counter


def init(
    generate: Callable[[int, int, str], Tuple[PieceKeyCounts, NodeCounter, List[T]]],
):
    setrlimit(RLIMIT_NOFILE, (1000000, 1000000))
    system("clear")
    current_argv = sys.argv
    width, height, subdirctory = get_from_argvs(current_argv)
    solutions_directory_path_name = path.join(DRIVE, subdirctory)
    make_directory(solutions_directory_path_name)
    pickle_directory_path_name = path.join(DRIVE, f"{subdirctory}.pickle")
    counts, node_counter, pieces = generate(width, height, pickle_directory_path_name)
    print(FIRST_LINE)
    start1 = time.time()
    save_solutions(solutions_directory_path_name, node_counter, counts, pieces)
    end1 = time.time()
    print(SECOND_LINE)
    print(f"{end1 - start1}")


def make_directory(directory_path_name: str):
    directory_path: Path = Path(directory_path_name)
    if not directory_path.exists():
        directory_path.mkdir()
