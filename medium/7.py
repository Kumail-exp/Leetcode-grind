class Solution:
    def reverse(self, x: int) -> int:
        negative=x<0
        rev=0
        x=abs(x)
        while x>0:
            rev=rev*10+(x%10)
            x//=10
        if rev >= 2**31 or rev<-2**31:
            return 0
        return rev*(-1 if negative else 1)