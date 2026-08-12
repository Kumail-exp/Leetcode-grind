class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count={}
        for val in nums:
            count[val]=1+count.get(val,0)
        qouta=(len(nums)//3)+1
        out=[]
        for val in count:
            if(count[val]>=qouta):
                out.append(val)
        return out