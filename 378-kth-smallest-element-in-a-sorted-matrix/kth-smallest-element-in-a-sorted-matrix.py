class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(min_heap)
        for _ in range(k - 1):
            value, row, col = heapq.heappop(min_heap)
            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        return heapq.heappop(min_heap)[0]