# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Method 1: Collect all values, sort, and reconstruct the list
        # nodes = []
        # head = point = ListNode(0)
        # for l in lists:
        #     while l:
        #         nodes.append(l.val)
        #         l = l.next
        
        # for x in sorted(nodes):
        #     point.next = ListNode(x)
        #     point = point.next
        
        # return head.next

        # Method 2: Use a Min-Heap to efficiently merge k sorted lists
        min_heap = []

        # Push the head of each linked list into the min-heap
        for index, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(min_heap, (linked_list.val, index, linked_list))
        
        dummy = ListNode(0)  # Dummy node for the resulting linked list
        cur = dummy  # Pointer to construct the new linked list

        while min_heap:
            # Pop the smallest element from the heap
            val, index, node = heapq.heappop(min_heap)
            cur.next = ListNode(val)  # Add the smallest value to the result list
            cur = cur.next  # Move the pointer forward

            # If the extracted node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        return dummy.next  # Return the head of the merged linked list
