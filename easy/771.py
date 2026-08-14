class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        gems=Counter(jewels)
        s=0
        for i in stones:
            s+=gems.get(i,0)
        return s