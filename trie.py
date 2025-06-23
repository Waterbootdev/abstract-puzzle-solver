from typing import List, Tuple
from collections.abc import Callable

class Trie:
    def __init__(self, max: List[int]) -> None:
        self.max = max
        self.trie_stream: List[int] = [0]*max[0]
        self.length: int = max[0]
        self.zero = 0
     
    def insert(self, keys:List[int], last_key: int, next: Callable[[], int]) -> Tuple[bool, int]:
        return self.insert_last_key(self.pre_insert(keys), last_key, next)
     
    def pre_insert(self, keys: List[int]) -> int:
        current_stream_index: int = 0
        for i, key in enumerate(keys):
            current_stream_index = self.insert_key(current_stream_index, i + 1, key)
        return current_stream_index

    def insert_key(self, stream_index: int, max_index: int, key: int) -> int:
        key_index = stream_index + key
        next_straem_offset: int = self.trie_stream[key_index]
        if next_straem_offset == 0:
            next_straem_offset =  self.length - stream_index
            self.trie_stream[key_index] = next_straem_offset
            self.append_zeros(self.max[max_index])
        return stream_index + next_straem_offset
    
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