class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        more=[]
        count=0
        for i in nums:
            if i==pivot:
                count+=1
            elif i<pivot:
                less.append(i)
            else:
                more.append(i)
        return less+[pivot]*count+more