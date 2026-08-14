class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        out=[]
        ones=[]
        for i in range(len(boxes)):
            if boxes[i]=='1':
                ones.append(i)
        for i in range(len(boxes)):
            val=0
            for j in range(len(ones)):
                val+=abs(i-ones[j])
            out.append(val)
        return out
                