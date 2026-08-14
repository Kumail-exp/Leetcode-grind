class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=Counter(nums)
        count=0
        for i in c:
            count+=(c[i]*(c[i]-1))//2
        return count