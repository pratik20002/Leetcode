# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        total_sum = 0
        if low <= root.val <= high:
            total_sum += root.val
        
        if root.val > low:
            total_sum += self.rangeSumBST(root.left, low, high)
        
        if root.val < high:
            total_sum += self.rangeSumBST(root.right, low, high)
        
        return total_sum