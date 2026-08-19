class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        till=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[till]=nums[till],nums[i]
                till+=1