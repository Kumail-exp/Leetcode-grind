class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return math.comb(k+n-1,n-1) %(10**9+7)