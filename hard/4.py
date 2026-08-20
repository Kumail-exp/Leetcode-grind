class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined=sorted(nums1+nums2)
        l, h = 0, len(combined) - 1

        if len(combined) % 2 == 0:
            mid1 = (l + h) // 2
            mid2 = mid1 + 1

            return (combined[mid1] + combined[mid2]) / 2

        else:
            mid = (l + h) // 2
            return combined[mid]
        