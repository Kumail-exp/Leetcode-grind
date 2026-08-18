class Solution:
    def __init__(self):
        self.done={0:0,1:1,2:1}
    def fib(self, n: int) -> int:
        val=self.done.get(n,-1)
        if val!=-1:
            return val
        val=self.fib(n-1)+self.fib(n-2)
        self.done[n]=val
        return val

