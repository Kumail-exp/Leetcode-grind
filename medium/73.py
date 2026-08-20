class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        cols=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    rows.add(j)
                    cols.add(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in rows:
                    matrix[i][j]=0
                if i in cols:
                    matrix[i][j]=0  