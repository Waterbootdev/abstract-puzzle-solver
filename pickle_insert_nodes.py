from node_counter import NodeCounter
from piece_key_constants import PIECE_KEY_BASE
from array import array
from typing import Set, Tuple
from pickle_insert_node import InsertNode
from pathlib import Path

class InsertNodes:
    def __init__(self, node_counter: NodeCounter, depth: int, directory_path_name: str) -> None:
        self.node_counter = node_counter
        self.length = PIECE_KEY_BASE ** depth
        self.leafs: Set[int] = set()
        self.insert_node: InsertNode = InsertNode(directory_path_name)

        directory_path: Path = Path(directory_path_name)
        if not directory_path.exists():
            directory_path.mkdir()
            
    def pre_insert(self, digits: array[int]) -> int:
        current_stream_index: int = 0
        for digit in digits:
            current_stream_index = self.insert_digit(current_stream_index, digit)
        return current_stream_index

    def insert_digit(self, stream_index: int, digit: int) -> int:
        return (stream_index + digit) * PIECE_KEY_BASE

    def insert_last_digit(self, current_stream_index: int, last_digit: int) -> Tuple[bool, InsertNode]:
        leaf_index = current_stream_index + last_digit
        if leaf_index in self.leafs:
            self.insert_node.load(leaf_index)
            return False, self.insert_node
        else:
            self.leafs.add(leaf_index)
            self.insert_node.init(leaf_index)
            self.node_counter.increment()
            return True, self.insert_node
        
    def close(self) -> None:
        pass
        
