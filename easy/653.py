# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        done={}
        def backtrack(node):
            done[node.val]=True
            if node.left:
                backtrack(node.left)
            if node.right:
                backtrack(node.right)
        backtrack(root)
        for i in done:
            if(done.get(k-i,False) and (k-i!=i)):
                return True
        return False
