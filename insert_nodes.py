from piece_key_constants import PIECE_KEY_BASE
from node_counter import NodeCounter
from insert_node import InsertNode
from array import array
from typing import Tuple, Dict

class InsertNodes:
    def __init__(self, node_counter: NodeCounter, depth: int) -> None:
        self.node_counter = node_counter
        self.length = PIECE_KEY_BASE ** depth
        self.leafs: Dict[int, InsertNode] = {} 
       
    def pre_insert(self, digits: array[int]) -> int:
        current_stream_index: int = 0
        for digit in digits:
            current_stream_index = self.insert_digit(current_stream_index, digit)
        return current_stream_index

    @staticmethod
    def insert_digit(stream_index: int, digit: int) -> int:
        return (stream_index + digit) * PIECE_KEY_BASE
          
    def insert_last_digit(self, current_stream_index: int, last_digit: int) -> Tuple[bool, InsertNode]:
        leaf_index = current_stream_index + last_digit
        if leaf_index in self.leafs:
            return False, self.leafs[leaf_index]
        else:
            insert_node = InsertNode()
            self.leafs[leaf_index] = insert_node
            self.node_counter.increment()
            return True, insert_node
    
    def close(self) -> None:
        pass

        
