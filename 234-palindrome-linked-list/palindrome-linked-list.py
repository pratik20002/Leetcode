# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        pointer = head
        while pointer is not None:
            vals.append(pointer.val)
            pointer = pointer.next


        return vals == vals[::-1]