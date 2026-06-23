# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            new_head = head.next
            new_head.next = head
            head.next = None
            return new_head
        a = head
        b = head.next
        c = head.next.next
        a.next = None
        while c is not None:
            b.next = a
            a = b
            b = c
            c = c.next
        b.next = a
        return b
        
        # First iteration: a= a, b = b, c = c
        # Second iteration: a = b, b = c, c = d
        # Third iteration: a = c, b = d, c = None

# A -> B -> C -> D
# A <- B, C -> D
# A <- B <- C, D
# A <- B <- C <- D