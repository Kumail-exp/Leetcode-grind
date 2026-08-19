class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return 
        new=[0]*len(nums)
        for i in range(len(nums)):
            new[(i+k)%len(nums)]=nums[i]
        for i in range(len(nums)):
            nums[i]=new[i]
        