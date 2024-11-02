class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                     (0, 1), (1, -1), (1, 0), (1, 1)]
                    
        queue = collections.deque([(0, 0, 1)])

        visited = set((0, 0))

        while queue:
            r, c, pathlen = queue.popleft()
            if r == (n - 1) and c == (n - 1):
                return pathlen
            
            for dr, dc in directions:
                n_row = r + dr
                n_col = c + dc

                if 0 <= n_row < n and 0 <= n_col < n and (n_row, n_col) not in visited and grid[n_row][n_col] == 0:
                    visited.add((n_row, n_col))
                    queue.append((n_row, n_col, pathlen + 1))
            
        return -1
                