class MinStack:

    def __init__(self):
        self.stack=[None]*30000
        self.min=[None]*30000
        self.rear=0

    def push(self, value: int) -> None:
        self.stack[self.rear]=value

        if(self.rear==0):
            self.min[self.rear]=value
        else:
            self.min[self.rear]=(min(self.min[self.rear-1],value))
        self.rear+=1

    def pop(self) -> None:
        self.rear-=1

    def top(self) -> int:
        return self.stack[self.rear-1]

    def getMin(self) -> int:
        return self.min[self.rear-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()