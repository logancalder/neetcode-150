class MinStack:

    def __init__(self):
        self.contents = []
        self.mins = []

    def push(self, val: int) -> None:
        self.contents.append(val)
        if not self.mins or self.mins[-1] > val:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.contents.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.contents[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]
        
