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
        

        # def dfs(node, depth):
        #     if not node:
        #         return 
            
        #     if depth == len(res):
        #         res.append(node.val)
            
        #     dfs(node.right, depth+1)
        #     dfs(node.left, depth+1)
        
        # res = []
        # dfs(root, 0)
        # return res

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