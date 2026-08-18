class Solution:
    def __init__(self):
        self.done={0:0,1:1,2:2,3:3}
    def climbStairs(self, n: int) -> int:
        val=self.done.get(n,-1)
        if(val!=-1):
            return val
        val=self.climbStairs(n-1)+self.climbStairs(n-2)
        self.done[n]=val
        return val