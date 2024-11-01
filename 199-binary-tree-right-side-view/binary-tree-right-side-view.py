# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([(root)])
        res = []
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                cur = queue.popleft()
                if i == level_length - 1:
                    res.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
            
        return res