class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num%10!=0 if num>0 else True