class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out=[0]*len(nums)
        for i in range(len(nums)):
            out[i]=nums[nums[i]]
        return out