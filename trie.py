from typing import List, Tuple, Any
from collections.abc import Callable

class Trie:
    def __init__(self, max: List[int]) -> None:
        self.max = max
        self.root: List[Any|None]  = [None]*max[0]

    def insert(self, keys:List[int], last_key: int, next: Callable[[], int]) -> Tuple[bool, int]:
        current: List[Any|None] = self.root
        for i, key in enumerate(keys):
            next_node = current[key]
            if next_node is None:
                next_node = [None]*self.max[i + 1]
                current[key] = next_node
            current = next_node
        last_node = current[last_key]
        if last_node is None:
            next_node = next()
            current[last_key] = next_node
            return True, next_node
        else:
            return False, last_node
