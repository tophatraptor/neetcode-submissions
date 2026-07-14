# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        carryover = 0
        place = 0
        total = 0
        dummy_head = ListNode(None, None)
        cursor = dummy_head
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1val = 0
            else:
                l1val = l1.val
                l1 = l1.next
            if l2 is None:
                l2val = 0
            else:
                l2val = l2.val
                l2 = l2.next
            
            res = l1val + l2val + carryover
            if res >= 10:
                res = res % 10
                carryover = 1
            else:
                carryover = 0
            new_node = ListNode(res, None)
            cursor.next = new_node
            cursor = new_node
        if carryover:
            cursor.next = ListNode(1, None)
        
        return dummy_head.next