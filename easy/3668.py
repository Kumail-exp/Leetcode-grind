class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        out=[]
        for i in range(len(order)):
            if order[i] in friends:
                out.append(order[i])
        return out