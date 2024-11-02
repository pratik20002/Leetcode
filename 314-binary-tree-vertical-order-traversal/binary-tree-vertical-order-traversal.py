# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        
        # column_items = collections.defaultdict(list)
        # queue = collections.deque([(0, root)])
        # res = []

        # min_x = float("inf")
        # max_x = float("-inf")

        # while queue:
        #     x, node = queue.popleft()

        #     column_items[x].append(node.val)
        #     min_x = min(min_x, x)
        #     max_x = max(max_x, x)

        #     if node.left:
        #         queue.append((x-1, node.left))

        #     if node.right:
        #         queue.append((x+1, node.right))

        
        # for level in range(min_x, max_x + 1):
        #     res.append(column_items[level])
        
        # return res

        if not root:
            return []
        
        column_items = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            column_items[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            
            if node.right:
                queue.append((node.right, col + 1))
            
        res = []

        for column in sorted(column_items.keys()):
            res.append(column_items[column])
        
        return res
        