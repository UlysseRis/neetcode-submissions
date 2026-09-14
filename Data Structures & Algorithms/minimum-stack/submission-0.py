class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if not self.stack:
            raise TypeError("Stack is empty")
        self.stack.pop()


    def top(self) -> int:
        if not self.stack:
            raise TypeError("Stack is empty")
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)

        
