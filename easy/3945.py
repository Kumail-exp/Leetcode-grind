class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        if n==0:
            return 0
        return n%10+self.digitFrequencyScore(n//10)