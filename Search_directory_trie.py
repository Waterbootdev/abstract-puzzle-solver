from piece_key_constants import PIECE_KEY_BASE
from typing import List, BinaryIO, Tuple
from insert_node import InsertNode
import random


POSITION_BYTES_LENGTH: int = 8

NONE_POSITION_BYTES : bytes = int.to_bytes(0, length=POSITION_BYTES_LENGTH)

PIECE_KEY_BASE_POSITION_BYTES_LENGTH: int = PIECE_KEY_BASE * POSITION_BYTES_LENGTH

NONE_PIECE_KEY_BASE_POSITION_BYTES : bytes = int.to_bytes(0, length=PIECE_KEY_BASE_POSITION_BYTES_LENGTH)

class SearchTrieFile:
    def __init__(self, path: str) -> None:
        self.file: BinaryIO = open(path, 'bw+')
        self.file.write(NONE_PIECE_KEY_BASE_POSITION_BYTES)
        self.size = PIECE_KEY_BASE_POSITION_BYTES_LENGTH
        self.leafs_count = 0
        self.insert_nodes: List[InsertNode] = []

    def insert(self, digits: List[int]) -> InsertNode:
        self.file.seek(0)
    
        offsets =list(map(lambda x: x * POSITION_BYTES_LENGTH, digits[:-1]))

        legth = len(offsets)

        index = 0
        
        read_position = 0
        position_offset = 0
        go = True

        while go and index < legth:
            read_position, position_offset = self.read(offsets[index])
            if position_offset == 0:
                go = False
            else:
                self.file.seek(position_offset - 1, 1)
                index += 1

        if go:
            self.file.seek(digits[-1] * POSITION_BYTES_LENGTH, 1)
            leaf_index = int.from_bytes(self.file.read(POSITION_BYTES_LENGTH))

            if leaf_index == 0:
                self.file.seek(-POSITION_BYTES_LENGTH, 1)
                self.leafs_count += 1
                self.file.write(self.leafs_count.to_bytes(POSITION_BYTES_LENGTH))
                insert_node = InsertNode()
                self.insert_nodes.append(insert_node)

                return insert_node
            else:
                return self.insert_nodes[leaf_index - 1]  
        else:
            
            position_offset = self.size - (read_position + POSITION_BYTES_LENGTH)
            
            self.file.seek(-POSITION_BYTES_LENGTH, 1)
            self.file.write(int.to_bytes(position_offset + 1, length=POSITION_BYTES_LENGTH))
            self.file.seek(position_offset, 1)

            index += 1

            count = legth - index
            
            while count > 0:
                match digits[index]:
                    case 0:
                        self.write_position_offset(PIECE_KEY_BASE_POSITION_BYTES_LENGTH - POSITION_BYTES_LENGTH)
                        self.write_none_postion()
                        self.write_none_postion()
                    case 1:
                        self.write_none_postion()
                        self.write_position_offset(POSITION_BYTES_LENGTH)
                        self.write_none_postion()
                    case 2:
                        self.write_none_postion()
                        self.write_none_postion()
                        self.write_position_offset(0)
                    case _:
                        raise ValueError()
                index += 1
                count -= 1

            self.leafs_count += 1

            insert_node = InsertNode()

            self.insert_nodes.append(insert_node)

            match digits[-1]:
                    case 0:
                        self.write_leaf()
                        self.write_none_postion()
                        self.write_none_postion()
                    case 1:
                        self.write_none_postion()
                        self.write_leaf()
                        self.write_none_postion()
                    case 2:
                        self.write_none_postion()
                        self.write_none_postion()
                        self.write_leaf()
                    case _:
                        raise ValueError()
                
            return insert_node
             
    def write_position_offset(self, position_offset: int):
        position_offset += 1
        self.file.write(position_offset.to_bytes(POSITION_BYTES_LENGTH))
        self.size += POSITION_BYTES_LENGTH

    def write_leaf(self):
        self.file.write(self.leafs_count.to_bytes(POSITION_BYTES_LENGTH))
        self.size += POSITION_BYTES_LENGTH

    def write_none_postion(self):
        self.file.write(NONE_POSITION_BYTES)
        self.size += POSITION_BYTES_LENGTH

    def read(self, offset: int) -> Tuple[int, int]:
        read_position = self.file.seek(offset, 1)
        return read_position, int.from_bytes(self.file.read(POSITION_BYTES_LENGTH))


if  __name__ == '__main__':

    import time

    l = [random.choices(range(PIECE_KEY_BASE), k = 150) for _ in range(10)]
    indexes: List[InsertNode|None] = [None]*len(l)
    
    s = SearchTrieFile("/mnt/g/test.bytes")
    
    start = time.time()    
    
    for i, ll in enumerate(l):
        indexes[i] = s.insert(ll)
        assert indexes[i] == s.insert(ll)
        #print(i)
    
    print(time.time() - start)


   


        

