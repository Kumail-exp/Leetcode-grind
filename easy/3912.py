class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        mx = 0
        valid = []

        for i in range(len(nums)):
            rmx = 0
            for j in range(i + 1, len(nums)):
                rmx = max(rmx, nums[j])

            if nums[i] > mx or nums[i] > rmx:
                valid.append(nums[i])

            mx = max(mx, nums[i])

        return valid