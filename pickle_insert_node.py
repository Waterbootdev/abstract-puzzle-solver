from os import path
from pickle import dump, load
from typing import BinaryIO, Dict

from insert_node_value import InsertNodeValue


class InsertNode:
    def __init__(self, directory_path: str) -> None:
        self.indexes: Dict[int, InsertNodeValue | None]
        self.directory_path = directory_path
        self.file_name: str
        self.file: BinaryIO

    def init(self, index: int) -> None:
        self.set_file_name(index)
        self.file = open(self.file_name, "wb")
        self.indexes = {}

    def set_file_name(self, index: int) -> None:
        self.file_name = path.join(self.directory_path, f"{index}.pickle")

    def load(self, index: int) -> None:
        self.set_file_name(index)
        self.file = open(self.file_name, "rb+")
        self.indexes = load(self.file)
        self.file.seek(0)

    def append_index(self, index: int, value: InsertNodeValue | None = None) -> None:
        self.indexes[index] = value
        dump(self.indexes, self.file)
        self.file.close()

    def contains_index(self, index: int) -> bool:
        containd = index in self.indexes
        if containd:
            self.file.close()
        return containd

    def get_value(self, index: int) -> InsertNodeValue | None:
        return self.indexes[index]
