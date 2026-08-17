class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(3):
            if(mat==target):
                return True
            mat=Solution.rot90(mat)
        return False
    @staticmethod
    def rot90(mat):
        n = len(mat)
        rot = []
        for j in range(n):
            a = []
            for i in range(n - 1, -1, -1):
                a.append(mat[i][j])
            rot.append(a)
        return rot