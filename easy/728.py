class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out=[]
        for i in range(left,right+1):
            if(Solution.is_sd(i)):
                out.append(i)
        return out
    @staticmethod
    def is_sd(n):
        og=n
        while n>0:
            d=(n%10)
            if d==0:
                return False
            if og%d!=0:
                return False
            n//=10
        return True