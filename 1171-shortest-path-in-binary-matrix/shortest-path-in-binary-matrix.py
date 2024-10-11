class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque([(0, 0, 1)]) #r, c, Length of Step
        visit = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while queue:

            r, c, length = queue.popleft()
            if min(r, c) < 0  or max(r, c) == N or grid[r][c]:
                continue
            
            if r == N - 1 and c == N - 1:
                return length
            
            for dr, dc in directions:
                if(r + dr, c + dc) not in visit:
                    queue.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))

        return -1
