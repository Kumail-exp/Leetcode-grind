class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1 or n==2 or n==3 or n==5:
            return True
        
        able=True
        while able:
            able=False
            for i in  [2,3,5]:
                if n%i==0:
                    able=True
                    n//=i
            
        return n==1
        
