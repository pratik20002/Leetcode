# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
        1
        /\
       2  3
       /\ /\
        5   4
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, depth):
            if not node:
                return 
            if depth == len(res):
                res.append(node.val)

            if node.right:
                dfs(node.right, depth+1)
                
            if node.left:
                dfs(node.left, depth+1)
            
            
        
        res = []
        dfs(root, 0)
        return res