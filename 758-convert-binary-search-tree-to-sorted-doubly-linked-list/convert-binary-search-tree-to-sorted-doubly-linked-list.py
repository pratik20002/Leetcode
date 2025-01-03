"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.first = None
        self.last = None

        self.inorder_link(root)

        self.first.left = self.last
        self.last.right = self.first

        return self.first
    
    def inorder_link(self, node):
        if node:
            self.inorder_link(node.left)

            if not self.last:
                self.first = node
            else:
                node.left = self.last
                self.last.right = node
            
            self.last = node
            self.inorder_link(node.right)
    
#T -> O(N)
#S -> O(log N) -> If tree is balanced else O(N)