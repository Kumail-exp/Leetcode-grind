class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k%=2 * (n - 1)
        owner=0
        direction=1
        while k>0:
            k-=1
            if(owner==0):
                direction=1
            if(owner==n-1):
                direction=-1
            owner+=direction
        return owner
            
