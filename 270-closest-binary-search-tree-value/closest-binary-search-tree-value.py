# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_value = root.val 
        minimum_difference = float('inf') 
        
        current_node = root
        while current_node:
            difference = abs(current_node.val - target)
            
            if difference < minimum_difference or (difference == minimum_difference and current_node.val < closest_value):
                minimum_difference = difference
                closest_value = current_node.val

            if current_node.val > target:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return closest_value