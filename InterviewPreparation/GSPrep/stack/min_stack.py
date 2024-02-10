class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: 
            self.stack.append([val, val])
        else:
            min_val = val if self.stack[-1][1] > val else self.stack[-1][1]
            self.stack.append([val, min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack != [] else -1

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack != [] else -1
    

if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(-4)
    stack.push(-3)
    stack.pop()
    print(stack.getMin())