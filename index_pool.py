from array import array

class IndexPool:
    def __init__(self, offset: int) -> None:
        self.offset = offset
        self.zero = 0
        self.last_index = self.zero
        self.indexes: array[int] = array('i', [self.zero])
        self.length = 1

    def get_index(self, index: int) -> int:
        if index < self.length:
            return self.indexes[index]
        else:
            self.last_index += self.offset
            self.indexes.append(self.last_index)
            self.length += 1
            return self.last_index