class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any((target in m) for m in matrix)