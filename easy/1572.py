class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]
            s+=mat[i][len(mat)-i-1]
        if len(mat)%2==1:
            s-=mat[(len(mat))//2][(len(mat))//2]
        return s