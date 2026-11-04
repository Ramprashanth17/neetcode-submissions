class MinStack:

    def __init__(self):
        self.items = []
        

    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append([val, val])
        else:
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])
        

    def pop(self) -> None:
        if len(self.items) == 0:
            return "Stack is empty, cannot pop"
        else:
            self.items.pop()
        

    def top(self) -> int:
        if len(self.items) == 0:
            return "Stack is empty!"
        else:
            return self.items[-1][0]
        

    def getMin(self) -> int:
        if len(self.items) == 0:
            return 0
        else:
            return self.items[-1][1]
        
