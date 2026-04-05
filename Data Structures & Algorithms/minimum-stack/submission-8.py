class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        self.len = 0

    def push(self, val: int) -> None:
        if self.min > val:
            self.min = val
        
        self.stack.append((val, self.min))
        self.len += 1

    def pop(self) -> None:
        self.stack.pop()
        self.len -= 1
        if self.len > 0:
            self.min = self.stack[-1][1]
        else:
            self.min = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
