from typing import List, Tuple
from collections.abc import Callable

# class Trie:
#     def __init__(self, max: List[int]) -> None:
#         self.max = max
#         self.root: List[Any|None]  = [None]*max[0]

#     def insert(self, keys:List[int], last_key: int, next: Callable[[], int]) -> Tuple[bool, int]:
#         current: List[Any|None] = self.root
#         for i, key in enumerate(keys):
#             next_node = current[key]
#             if next_node is None:
#                 next_node = [None]*self.max[i + 1]
#                 current[key] = next_node
#             current = next_node
#         last_node = current[last_key]
#         if last_node is None:
#             next_node = next()
#             current[last_key] = next_node
#             return True, next_node
#         else:
#             return False, last_node

class Trie:
    def __init__(self, max: List[int]) -> None:
        self.max = max
        self.trie_stream: List[int] = [0]*max[0]
        self.length: int = len(self.trie_stream)
        self.zero = 0
     
    def insert(self, keys:List[int], last_key: int, next: Callable[[], int]) -> Tuple[bool, int]:
        return self.insert_last_key(self.pre_insert(keys), last_key, next)
     
    def pre_insert(self, keys: List[int]) -> int:
        current_stream_index: int = 0
        for i, key in enumerate(keys):
            current_stream_index = self.insert_key(current_stream_index, i + 1, key)
        return current_stream_index

    def insert_key(self, stream_index: int, max_index: int, key: int) -> int:
        stream_index += key
        next_node_index: int = self.trie_stream[stream_index]
        if next_node_index == 0:
            next_node_index = self.length
            self.trie_stream[stream_index] = next_node_index
            self.append_zeros(self.max[max_index])
        return next_node_index
    
    def append_zeros(self, count: int) -> None:
        for _ in range(count):
            self.trie_stream.append(self.zero)
        self.length += count
    
    def insert_last_key(self, current_stream_index: int, last_key: int, next: Callable[[], int]) -> Tuple[bool, int]:
        stream_index = current_stream_index + last_key
        insert_index = self.trie_stream[stream_index]
        if insert_index == 0:
            insert_index = next()
            self.trie_stream[stream_index] = insert_index
            return True, insert_index
        return False, insert_index      