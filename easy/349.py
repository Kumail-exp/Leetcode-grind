class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        n1=set()
        for i in nums1:
            n1.add(i)
        for i in set(nums2):
            if i in n1:
                inter.append(i)
        return inter