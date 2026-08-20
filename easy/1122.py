class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        set_arr=set(arr2)
        present=[]
        absent=[]
        for i in arr1:
            if i in set_arr:
                present.append(i)
            else:
                absent.append(i)
        return sorted(present,key=lambda x: arr2.index(x)) +sorted(absent)