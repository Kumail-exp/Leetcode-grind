class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[]
        def backtrack(a,depth=0):
            if depth==len(nums):
                perms.append(a[:])
                return
            for i in nums:
                if i not in a:
                    a.append(i)
                    backtrack(a,depth+1)
                    a.pop()
        backtrack([])
        return perms
        