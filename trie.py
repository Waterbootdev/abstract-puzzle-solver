from typing import Tuple, Dict
from collections.abc import Callable
from array import array
from itertools import repeat
from trie_helper import leafs_count

class TrieArray:
    def __init__(self, max_values: array[int]) -> None:
        self.max_values = max_values
        self.length: int = leafs_count(max_values)
        self.leafs: array[int] = array('i', repeat(0, self.length))
        self.leafs_count: int = 0
     
    def insert(self, keys: array[int], last_key: int, next_index: Callable[[], int]) -> Tuple[bool, int]:
        return self.insert_last_key(self.pre_insert(keys), last_key, next_index)
     
    def pre_insert(self, keys: array[int]) -> int:
        current_stream_index: int = 0
        for i, key in enumerate(keys):
            current_stream_index = self.insert_key(current_stream_index, i + 1, key)
        return current_stream_index

    def insert_key(self, stream_index: int, max_index: int, key: int) -> int:
         return (stream_index + key) * self.max_values[max_index]
    
    def insert_last_key(self, current_stream_index: int, last_key: int, next_index: Callable[[], int]) -> Tuple[bool, int]:
        leaf_index = current_stream_index + last_key
        leaf = self.leafs[leaf_index]
        if leaf == 0:
            leaf = next_index()
            self.leafs[leaf_index] = leaf
            self.leafs_count += 1
            return True, leaf
        return False, leaf

class TrieDict:
    def __init__(self, max_values: array[int]) -> None:
        self.max_values = max_values
        self.length: int = leafs_count(max_values)
        self.leafs: Dict[int, int] = {} 
        self.leafs_count: int = 0
     
    def insert(self, keys: array[int], last_key: int, next_index: Callable[[], int]) -> Tuple[bool, int]:
        return self.insert_last_key(self.pre_insert(keys), last_key, next_index)
     
    def pre_insert(self, keys: array[int]) -> int:
        current_stream_index: int = 0
        for i, key in enumerate(keys):
            current_stream_index = self.insert_key(current_stream_index, i + 1, key)
        return current_stream_index

    def insert_key(self, stream_index: int, max_index: int, key: int) -> int:
         return (stream_index + key) * self.max_values[max_index]
    
    def insert_last_key(self, current_stream_index: int, last_key: int, next_index: Callable[[], int]) -> Tuple[bool, int]:
        leaf_index = current_stream_index + last_key
        
        if leaf_index not in self.leafs:
            leaf = next_index()
            self.leafs[leaf_index] = leaf
            self.leafs_count += 1
            return True, leaf
        else:
            return False, self.leafs[leaf_index]
        