# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # if not root:
        #     return []

        # level_items =  collections.defaultdict(list)
        # queue = collections.deque([(root, 0, 0)])
        # min_col = float("inf")
        # max_col = float("-inf")

        # while queue:
        #     node, row, col = queue.popleft()
        #     if col < min_col:
        #         min_col = col
            
        #     if col > max_col:
        #         max_col = col
            
        #     level_items[col].append((node.val, row))

        #     if node.left:
        #         queue.append((node.left, row + 1, col - 1))
            
        #     if node.right:
        #         queue.append((node.right, row + 1, col + 1))
        
        # res = []
        # for level in range(min_col, max_col + 1):
        #     items = level_items[level]
        #     items.sort(key = lambda x:(x[1], x[0]))
        #     items = [val for val, _ in items]
        #     res.append(items)
        
        # return res
        if not root:
            return []
        
        column_items = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])

        while queue:
            node, col, row = queue.popleft()
            if node:
                column_items[col].append((row, node.val))
                queue.append((node.left, col - 1, row + 1))
                queue.append((node.right, col + 1, row + 1))
        
        sorted_columns = sorted(column_items.keys())
        res = []

        for col in sorted_columns:
            column_nodes = sorted(column_items[col], key = lambda x:(x[0], x[1]))
            res.append([val for row, val in column_nodes])
        
        return res