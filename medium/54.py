class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        done={}
        out=[]
        up=0
        down=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while up<=down and left<=right:
            for i in range(left,right+1):
                if(done.get(f'{up},{i}',False)):
                    return out
                out.append(matrix[up][i])
                done[f'{up},{i}']=True
            up+=1
            for i in range(up,down+1):
                if(done.get(f'{i},{right}',False)):
                    return out
                out.append(matrix[i][right])
                done[f'{i},{right}']=True
            right-=1
            for i in range(right,left-1,-1):
                if(done.get(f'{down},{i}',False)):
                    return out
                out.append(matrix[down][i])
                done[f'{down},{i}']=True
            down-=1
            for i in range(down,up-1,-1):
                if(done.get(f'{i},{left}',False)):
                    return out
                out.append(matrix[i][left])
                done[f'{i},{left}']=True
            left+=1
        return out