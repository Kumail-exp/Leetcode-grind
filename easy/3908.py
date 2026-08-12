class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        ns=f'{n}'
        nx=f'{x}'
        return Counter(ns)[nx]>0 and ns[0]!=nx