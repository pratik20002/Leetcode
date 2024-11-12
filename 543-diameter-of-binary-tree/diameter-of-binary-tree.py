# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            if not node:
                return 0, 0 #height, diameter
            
            left_height, left_diameter = dfs(node.left) #1, 0
            right_height, right_diameter = dfs(node.right) #1, 0

            current_diameter = max(left_diameter, right_diameter, left_height + right_height) #2
            current_height = 1 + max(left_height, right_height) #2

            return current_height, current_diameter #2,2
        
        return dfs(root)[1]

    #[1,2,3,4,5]
    #2 -> 
    #4 -> 1, 0 
    #5 ->