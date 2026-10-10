class MinStack:

    def __init__(self):
        self.stack = []
        self.MIN_stack = [float('inf')]

    def push(self, val: int) -> None:
        if val < self.MIN_stack[-1]:
            self.MIN_stack.append(val)
        else:
            self.MIN_stack.append(self.MIN_stack[-1])

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.MIN_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MIN_stack[-1]
