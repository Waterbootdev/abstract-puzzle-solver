
from insert_node_value import InsertNodeValue
from typing import Dict

class InsertNode:
    def __init__(self) -> None:
        self.indexes: Dict[str, InsertNodeValue|None] = dict()

    def append_index(self, index: str, value: InsertNodeValue|None = None) -> None:
        self.indexes[index] = value

    def contains_index(self, index: str) -> bool:
        return index in self.indexes

    def get_value(self, index: str) -> InsertNodeValue|None:
        return self.indexes[index]
