class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2

        def dfs(r, c, island_id):
            stack = [(r, c)]
            size = 0
            while stack:
                r, c = stack.pop()
                if grid[r][c] != 1:
                    continue
                grid[r][c] = island_id
                size += 1
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        stack.append((nr, nc))
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        max_island_size = max(island_sizes.values(), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    possible_size = 1  
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            island_id = grid[nr][nc]
                            if island_id not in seen:
                                seen.add(island_id)
                                possible_size += island_sizes[island_id]
                    max_island_size = max(max_island_size, possible_size)

        return max_island_size