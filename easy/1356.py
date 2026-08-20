
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x:(x.bit_count(),x)) #tuple prioritizes first and ifs its equal check the other 
        return arr