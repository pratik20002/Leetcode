# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            p1 = l1
            p2 = l2
            carry = 0
            sumlist = ListNode()
            result = sumlist
            
            while p1 is not None or p2 is not None or carry:
                val1 = p1.val if p1 else 0
                val2 = p2.val if p2 else 0
                
                total = val1 + val2 + carry
                carry = total // 10
                
                sumlist.val = total % 10
                if p1:
                    p1 = p1.next
                if p2:
                    p2 = p2.next
                
                if p1 is not None or p2 is not None or carry:
                    sumlist.next = ListNode()
                    sumlist = sumlist.next
            
            return result

        
        
        