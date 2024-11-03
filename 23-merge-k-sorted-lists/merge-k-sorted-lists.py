# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Method1
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
        
        #Method2
        min_heap = []

        for index, linked_list in enumerate(lists): #[-1, 1], [0, 2]
            if linked_list:
                heapq.heappush(min_heap, (linked_list.val, index, linked_list))
        
        dummy = ListNode(0)
        cur = dummy

        while min_heap:
            val, index, node = heapq.heappop(min_heap)
            cur.next = ListNode(val)
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        return dummy.next