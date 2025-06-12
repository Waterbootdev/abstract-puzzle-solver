from typing import TypeVar, Generic, List

T = TypeVar("T")

class Ring(Generic[T]):

    class RingNode:
    
        def __init__(self, index: int,  data: List[T]) -> None:    
            self.forward = self
            self.backward = self
            self.index = index
            self.data = data[index]

        def increment(self, data: List[T]):
            if self.forward == self or self.backward == self:
                raise Exception()
            node = Ring.RingNode(self.index + 1, data)
            node.backward = self
            node.forward = self.forward
            self.forward = node
            return node

        @staticmethod
        def twice(data: List[T]):
            first = Ring.RingNode(0, data)
            second = Ring.RingNode(1, data)

            first.forward = second
            second.forward = first

            first.backward = second
            second.backward = first

            return [first, second], second   

    def __init__(self, data: List[T]) -> None:
        self.__data = data
        self.length = len(data)
        
        if self.length < 2:
            raise ValueError()
        
        self.nodes, node = Ring.RingNode.twice(data)

        for _ in range(self.length - 2):
                node = node.increment(data)
                self.nodes.append(node)

        self.current_node = self.nodes[0]

    def get_forward(self) -> T:
        self.forward()
        return self.current_node.data
    
    def forward(self) -> None:
        self.current_node = self.current_node.forward
        
    def backward(self) -> None:
        self.current_node = self.current_node.backward
    
    def get_backward(self) -> T:
        self.backward()
        return self.current_node.data
    
    def current(self) -> T:
        return self.current_node.data
    
    def at_index(self, index: int) -> T:
        return self.__data[index]
    
    def curent_index(self) -> int:
        return self.current_node.index
    
    def backward_index(self) -> int:
        return self.current_node.backward.index
    
    def forward_index(self) -> int:
        return self.current_node.forward.index
    
    def set_to(self,index: int) -> None:
        self.current_node = self.nodes[index]


    


