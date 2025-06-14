from typing import List, Tuple

class TrieNode:
    def __init__(self, max:int, indexes: List[int]|None = None):
        
        if max == 0 and indexes is not None:
            self.indexes: List[int] = indexes
        else:
            self.childNode: List[TrieNode|None] = [None]*max if max > 0 else LEAF

    def append_indexes(self, index: int) -> bool:
        assert self.indexes is not None
    
        if index not in self.indexes:
            self.indexes.append(index)
            return True
        else:
            return False
    
        
        
LEAF: List[TrieNode|None] = []

def insert_key(root:TrieNode, max:int, key:List[int], index: int) -> Tuple[int, List[int]]:

    count = 0

    currentNode:TrieNode = root

    for value in key[:-1]:
        
        next_node = currentNode.childNode[value]

        if next_node is None:
            next_node = TrieNode(max)
            currentNode.childNode[value] = next_node
            count += 1

        currentNode = next_node

    value = key[-1]

    next_node = currentNode.childNode[value]

    if next_node is None:
            next_node = TrieNode(0, [index]) 
            currentNode.childNode[value] = next_node
            count += 1
    else:
        next_node.indexes.append(index) if index not in next_node.indexes else None

    return count, next_node.indexes

def contains_key(root:TrieNode, key:List[int], index: int) -> Tuple[bool, bool]:

    currentNode:TrieNode = root

    for value in key:
        
        next_node = currentNode.childNode[value]

        if next_node is None:

            return False, False

        currentNode = next_node
    
    return True, currentNode.append_indexes(index)

def insert_key_list(root:TrieNode, max_list:List[int], key:List[int], index:int) -> Tuple[int, int]:

    count = 0
    
    currentNode:TrieNode = root
     
    for i, value in enumerate(key):
        
        next_node = currentNode.childNode[value]

        if next_node is None:
            max = max_list[i + 1]
            next_node = TrieNode(max, [index]) if max == 0 else TrieNode(max)
            currentNode.childNode[value] = next_node
            count += 1

        currentNode = next_node

    return count, currentNode.indexes[0]

   