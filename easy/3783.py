class Solution:
    def mirrorDistance(self, n: int) -> int:
        if n<10:
            return 0
        return abs(n-self.reverse(n))
    def reverse(self,n):
        rev = 0
        while n:
            rev = rev * 10 + n % 10
            n //= 10
        return rev