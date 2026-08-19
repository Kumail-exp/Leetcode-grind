class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        done=0
        for i in range(len(nums)):
            total-=nums[i]
            if(done==total):
                return i
            done+=nums[i]
        
        return -1