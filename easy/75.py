class Solution:
    def sortColors(self, nums: List[int],low=0,high=None) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if high is None:
            high=len(nums)-1
        
        if high<=low:
            return 
        
        pivot=nums[high]
        i=low
        for j in range(low,high):
            if nums[j]<=pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i],nums[high]=nums[high],nums[i]
        self.sortColors(nums,low, i-1)
        self.sortColors(nums,i+1,high)