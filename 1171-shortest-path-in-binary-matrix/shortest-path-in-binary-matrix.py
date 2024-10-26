class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # N = len(grid)
        # queue = deque([(0, 0, 1)]) #r, c, Length of Step
        # visit = set((0, 0))
        # directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
        #               [1, 1], [-1, -1], [1, -1], [-1, 1]]
        # while queue:

        #     r, c, length = queue.popleft()
        #     if min(r, c) < 0  or max(r, c) == N or grid[r][c]:
        #         continue
            
        #     if r == N - 1 and c == N - 1:
        #         return length
            
        #     for dr, dc in directions:
        #         if(r + dr, c + dc) not in visit:
        #             queue.append((r + dr, c + dc, length + 1))
        #             visit.add((r + dr, c + dc))

        # return -1

        #approach 2
        if grid[0][0] or grid[-1][-1]:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        queue = collections.deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            x, y, path_len = queue.popleft()
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return path_len
            
            for x_inc, y_inc in directions:
                new_x = x + x_inc
                new_y = y + y_inc

                if((0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and not grid[new_x][new_y]):
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y, path_len + 1))
                
        return -1
        

        