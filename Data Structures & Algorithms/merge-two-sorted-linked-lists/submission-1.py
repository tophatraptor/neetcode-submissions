# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        dummy_head = ListNode(None, None)
        cursor = dummy_head
        while c1 is not None or c2 is not None:
            if c1 is None:
                minnode = c2
            elif c2 is None:
                minnode = c1
            else:
                if c2.val < c1.val:
                    minnode = c2
                else:
                    minnode = c1
                    # If the two ists are equal, take from C1 first
            cursor.next = minnode
            cursor = cursor.next
            if minnode == c2:
                c2 = c2.next
            elif minnode == c1:
                c1 = c1.next
        return dummy_head.next