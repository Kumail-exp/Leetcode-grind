class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        shaped=[[None]*c for _ in range(r)]
        print(shaped)
        m,n=0,0
        for i in mat:
            for j in i:
                if n>=c:
                    n=0
                    m+=1
                shaped[m][n]=j
                n+=1
        return shaped