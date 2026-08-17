class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rot=[]
        for i in range(len(matrix)):
            a=[]
            for j in range(len(matrix)-1,-1,-1):
                a.append(matrix[j][i])
            rot.append(a)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=rot[i][j]
        