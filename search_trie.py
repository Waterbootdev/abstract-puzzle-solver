from index_pool import IndexPool
from piece_key_constants import PIECE_KEY_BASE
from insert_node import InsertNode
from typing import List, Tuple

class SearchTrie:
    def __init__(self, trie_index_pool: IndexPool, index_pool: IndexPool) -> None:
        self.index_pool = index_pool
        self.trie_index_pool: IndexPool = trie_index_pool
        self.trie_stream: List[int] = [trie_index_pool.zero]*PIECE_KEY_BASE
        self.next_index: int = 1
        self.insert_nodes: List[InsertNode] = []
        self.insert_nodes_count: int = 0
    
    def pre_insert(self, digits: List[int]) -> int:
        current_stream_index: int = 0
        for digit in digits:
            current_stream_index = self.insert_digit(current_stream_index, digit)
        return current_stream_index

    def insert_digit(self, stream_index: int, digit: int) -> int:
        stream_index += digit
        next_node_index: int = self.trie_stream[stream_index]
        if next_node_index == 0:
            next_node_index = self.trie_index_pool.get_index(self.next_index)
            self.trie_stream[stream_index] = next_node_index
            self.next_index += 1
            self.trie_stream.append(self.trie_index_pool.zero)
            self.trie_stream.append(self.trie_index_pool.zero)
            self.trie_stream.append(self.trie_index_pool.zero)
        return next_node_index
    
    def insert_last_digit(self, current_stream_index: int, last_digit: int) -> Tuple[bool, InsertNode]:
        stream_index = current_stream_index + last_digit
        insert_node_index = self.trie_stream[stream_index]
        if insert_node_index == 0:
            insert_node = InsertNode()
            self.insert_nodes.append(insert_node)
            self.insert_nodes_count = self.index_pool.get_index(self.insert_nodes_count + 1)
            self.trie_stream[stream_index] = self.insert_nodes_count
            return True, insert_node
        else:
            return False, self.insert_nodes[insert_node_index - 1]
     
            
        
        






    
   





  


            



        



      
