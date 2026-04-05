class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float("inf")
        self.height = 0

    def push(self, val: int) -> None:
        self.mini = min(self.mini, val)
        self.stack.append([val, self.mini])
        self.height += 1

    def pop(self) -> None:
        self.stack.pop()
        self.height -= 1
        if self.height > 0:
            self.mini = self.getMin()
        else:
            self.mini = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
