class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #approach 1
        # heapq._heapify_max(nums)
        # while k > 1:
        #     heapq._heappop_max(nums)
        #     k -= 1
        # return heapq._heappop_max(nums)

        # #approach 2
        # nums_heap = [-num for num in nums]
        # heapq.heapify(nums_heap)
        # for _ in range(k - 1):
        #     heapq.heappop(nums_heap)
        # return -heapq.heappop(nums_heap)

        #approach 3
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]        