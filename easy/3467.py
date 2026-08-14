class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd=0
        for i in nums:
            odd+=i%2
        return [0]*(len(nums)-odd)+[1]*odd