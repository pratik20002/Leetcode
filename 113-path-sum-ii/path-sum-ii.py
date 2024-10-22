# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []

        def recurse(node, path, curSum):
            if not node:
                return
            
            curSum += node.val
            if not node.left and not node.right:
                if curSum == targetSum:
                    path.append(node.val)
                    ans.append(path[:])
                    path.pop()
                return
            
            path.append(node.val)
            recurse(node.left, path, curSum)
            recurse(node.right, path, curSum)
            path.pop()
        
        recurse(root, [], 0)
        return ans