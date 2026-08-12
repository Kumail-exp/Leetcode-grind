class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:    
        r=self.rev(n)
        return self.prime(min(r,n),max(r,n))
    def rev(self, n: int, current: int = 0) -> int:
        if n == 0:
            return current
        return self.rev(n // 10, current * 10 + (n % 10))

    def prime(self,s,e):
        #using sieve or erosthenes

        is_prime = [True] * (e+1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(e**0.5) + 1):
            if is_prime[start]:
                for multiple in range(start * start, e + 1, start):
                    is_prime[multiple] = False
        val=0
        for i in range(s, e + 1):
            if is_prime[i]:
                val += i
        return val
