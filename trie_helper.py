from typing import List
from piece_key_constants import PIECE_KEY_BASE
from array import array


def  create_trie_stream_length(max: List[int]) -> List[int]:
    count = 1
    total = 0
    for m in max:
        count *= m
        total += count
    total += count
    
    print(total)
    return list(0 for _ in range(total))


def create_search_trie_stream(depth: int) -> List[int]:
    
    count = 1
    total = 0
    for _ in range(depth):
        count *= PIECE_KEY_BASE
        total += count
    total += count
    
    
    print(f'{total}')
    
    return list(0 for _ in range(total))


def leafs_count(max: array[int]) -> int:
    count = 1
    for m in max:
        count *= m
    return count


if  __name__ == '__main__':
    print(list(0 for _ in range(100)))