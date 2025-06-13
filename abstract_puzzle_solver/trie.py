from typing import List, Tuple


class TrieNode:
    def __init__(self, max:int, object: List[int]|None = None):
        
        if max == 0 and object is not None:
            self.object: List[int] = object
        else:
            self.childNode: List[TrieNode|None] = [None]*max if max > 0 else LEAF
        
    

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
        next_node.object.append(index)

    return count, next_node.object

def check_key(root:TrieNode, key:List[int]) -> Tuple[bool, TrieNode|None]:

    currentNode:TrieNode = root

    for value in key:
        
        next_node = currentNode.childNode[value]

        if next_node is None:

            return False, None

        currentNode = next_node
    
    return True, currentNode



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

    return count, currentNode.object[0]

   