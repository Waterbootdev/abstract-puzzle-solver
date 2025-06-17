from piece_key_constants import PIECE_KEY_BASE
from insert_node import InsertNode
from typing import List, Any

class SearchTrie:
    def __init__(self) -> None:
        self.children: List[Any] = [None] * PIECE_KEY_BASE

    def insert(self, digits: List[int]) -> InsertNode:
        current = self 
        for digit in digits[:-1]:
            if current.children[digit] is None:
                current.children[digit] = SearchTrie()
            current = current.children[digit]

        last_digit = digits[-1]
        current_children = current.children

        if current_children[last_digit] is None:
            current_children[last_digit] = InsertNode()
    
        return current_children[last_digit]


    
   





  


            



        



      
