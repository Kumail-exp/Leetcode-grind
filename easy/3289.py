class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneaky=[]
        done={}
        for i in nums:
            if(done.get(i,False)):
                sneaky.append(i)
            else:
                done[i]=True
        return sneaky