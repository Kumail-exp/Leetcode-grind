class Solution:
    def minElement(self, nums: List[int]) -> int:
        m=10**4
        for i in nums:
            d=0
            while i>0:
                d+=i%10
                i=i//10
            m=d if d<m else m
        return m
