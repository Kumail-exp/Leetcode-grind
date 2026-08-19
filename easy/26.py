class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        till=0
        for i in dict.fromkeys(nums):
            nums[till]=i
            till+=1
        for i in range(len(nums)-till):
            nums.pop()
        return len(nums)