class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        val=0
        for i in range(n+1):
            val+=i *(1 if i%m else -1)
        return val