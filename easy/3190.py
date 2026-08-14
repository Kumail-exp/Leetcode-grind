class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([(0 if i%3==0 else 1) for i in nums])