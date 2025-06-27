class InsertNodeValue:
    def __init__(self, first:int , last:int) -> None:
        self.first = first
        self.count = last - first

    def __repr__(self) -> str:
        return f'{self.first}:{self.count}'
    
     
    
