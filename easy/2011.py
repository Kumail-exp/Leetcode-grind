class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operate= lambda op:-1 if ("--X"==op or op=="X--") else 1
        return sum(operate(i) for i in operations)