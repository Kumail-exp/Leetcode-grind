class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if(len(nums)==1):
            return nums[0]
        
        def backtrack(index,path):
            if(index==len(nums)):
                x=0
                for i in path:
                    x^=i
                return x
            path.append(nums[index])
            val=backtrack(index+1,path)
            path.pop()
            val+=backtrack(index+1,path)
            return val
        return backtrack(0,[])