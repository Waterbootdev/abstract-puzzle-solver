from piece_key_constants import PIECE_KEY_BASE
from insert_node import InsertNode
from typing import List, Any, Tuple
class SearchTrie:
    def __init__(self) -> None:
        self.children: List[Any] = [None] * PIECE_KEY_BASE

    def insert(self, digits: List[int]) -> Tuple[bool, InsertNode]:
        current = self 
        for digit in digits[:-1]:
            if current.children[digit] is None:
                current.children[digit] = SearchTrie()
            current = current.children[digit]
        last_digit = digits[-1]
        insert_node = current.children[last_digit]
        if insert_node is None:
            insert_node = InsertNode()
            current.children[last_digit] = insert_node
            return True, insert_node
        else: 
            return False, insert_node





    
   





  


            



        



      
