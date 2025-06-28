from insert_node_value import InsertNodeValue
from pickle import dump, load
from typing import Dict

class InsertNode:
    def __init__(self, file_path: str, leafs: Dict[int, int]) -> None:
        self.positions = leafs
        self.indexes: Dict[int, InsertNodeValue|None]
        self.file_path = file_path
        self.file = open(file_path, 'wb+')
        self.current_position = 0
        self.end_position = 0
        self.last_load_size = 0
        self.empty_size = 0
        
    def init(self, leaf_index: int)-> None:
        self.leaf_index = leaf_index
        self.indexes = {}
        self.last_load_size = 0
        

    def load(self, leaf_index: int) -> None:
        self.leaf_index = leaf_index
        current_position = self.file.seek(self.positions[leaf_index] - self.current_position, 1)
        self.indexes = load(self.file)
        self.current_position = self.file.tell()
        self.last_load_size = self.current_position - current_position
        assert self.last_load_size > 0
        
    def append_index(self, index: int, value: InsertNodeValue|None = None) -> None:
        self.indexes[index] = value
        self.current_position = self.file.seek(self.end_position - self.current_position, 1)
        self.positions[self.leaf_index] = self.current_position
        dump(self.indexes, self.file)
        self.end_position = self.file.tell()
        self.current_position = self.end_position

        self.empty_size += self.last_load_size 
        if self.empty_size * 1.2  > self.end_position:
            assert self.end_position - self.empty_size > 0
            print(f'{self.end_position} > {self.end_position - self.empty_size}')
            self.reposition()
            self.empty_size = 0
    
    def reposition(self) -> None:
        write_position = 0
        self.file.seek(0)
        for leaf_index, position in sorted(self.positions.items(), key=lambda x: x[1]):
            if position > write_position:
                _ = self.file.seek(position - write_position, 1)
                self.indexes = load(self.file)
                load_position = self.file.tell()
                self.positions[leaf_index] = write_position
                _ = self.file.seek(write_position - load_position, 1)
                dump(self.indexes, self.file)
                write_position = self.file.tell()
                assert write_position < load_position
            else:
                assert position == write_position
                _ = load(self.file)
                write_position = self.file.tell()
                
        self.current_position = write_position
        self.end_position = write_position

    def contains_index(self, index: int) -> bool:
        return index in self.indexes
    
    def get_value(self, index: int) -> InsertNodeValue|None:
        return self.indexes[index]
