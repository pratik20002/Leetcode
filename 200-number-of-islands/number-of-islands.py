import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visit = set()
        # islands = 0

        # def bfs(r, c):
        #     q = collections.deque()
        #     visit.add((r, c))
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  

        #         for dr, dc in direction:
        #             new_r = row + dr
        #             new_c = col + dc

        #             if (new_r in range(rows) and new_c in range(cols) 
        #                 and grid[new_r][new_c] == "1" 
        #                 and (new_r, new_c) not in visit):
        #                 q.append((new_r, new_c))
        #                 visit.add((new_r, new_c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visit:
        #             bfs(r, c)
        #             islands += 1
        
        # return islands





















        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))

            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    if (new_r in range(rows) and new_c  in range(cols) and (new_r, new_c) not in visit and grid[new_r][new_c] == "1"):
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands

