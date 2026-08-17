class Solution:
    def isHappy(self, n: int,done=None) -> bool:
        if n==1:
            return True
        if done is None:
            done={}
        s=0
        while n>0:
            s+=(n%10)**2
            n//=10
        if done.get(s,False):
            return False
        done[s]=True
        return self.isHappy(s,done)