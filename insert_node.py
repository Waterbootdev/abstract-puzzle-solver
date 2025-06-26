
from insert_node_value import InsertNodeValue
from typing import Dict

class InsertNode:
    def __init__(self) -> None:
        self.indexes: Dict[int, InsertNodeValue|None] = dict()

    def append_index(self, index: int, value: InsertNodeValue|None = None) -> None:
        self.indexes[index] = value

    def contains_index(self, index: int) -> bool:
        return index in self.indexes

    def get_value(self, index: int) -> InsertNodeValue|None:
        return self.indexes[index]

