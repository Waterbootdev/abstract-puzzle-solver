from index_pool import IndexPool
from insert_node import InsertNode
from node_counter import NodeCounter
from piece_key_constants import PIECE_KEY_BASE
from array import array
from itertools import repeat
from typing import List, Tuple

class InsertNodesArray:
    def __init__(self, index_pool: IndexPool, node_counter: NodeCounter, depth: int) -> None:
        self.node_counter = node_counter
        self.index_pool = index_pool
        self.length = PIECE_KEY_BASE ** depth
        self.leafs: array[int] = array('i', repeat(0, self.length))
        self.insert_nodes: List[InsertNode] = []
        self.insert_nodes_count: int = 0

    def pre_insert(self, digits: array[int]) -> int:
        current_stream_index: int = 0
        for digit in digits:
            current_stream_index = self.insert_digit(current_stream_index, digit)
        return current_stream_index

    def insert_digit(self, stream_index: int, digit: int) -> int:
        return (stream_index + digit) * PIECE_KEY_BASE


    def insert_last_digit(self, current_stream_index: int, last_digit: int) -> Tuple[bool, InsertNode]:
        leaf_index = current_stream_index + last_digit

        insert_node_index = self.leafs[leaf_index]
        if insert_node_index == 0:
            insert_node = InsertNode()
            self.insert_nodes.append(insert_node)
            self.insert_nodes_count = self.index_pool.get_index(self.insert_nodes_count + 1)
            self.leafs[leaf_index] = self.insert_nodes_count
            self.node_counter.increment()
            return True, insert_node
        else:
            return False, self.insert_nodes[insert_node_index - 1]