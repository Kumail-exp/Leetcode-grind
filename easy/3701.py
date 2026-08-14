class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(nums[i]*(-1 if i%2 else 1) for i in range(len(nums)))