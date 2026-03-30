class MinStack:

    def __init__(self):
        self.stack = []
        self.min_Stack = [] 
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_Stack:
            self.min_Stack.append(val)
        elif val <= self.min_Stack[-1]:
            self.min_Stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_Stack[-1]:
            self.stack.pop()
            self.min_Stack.pop()
        else:
            self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_Stack[-1]
        
