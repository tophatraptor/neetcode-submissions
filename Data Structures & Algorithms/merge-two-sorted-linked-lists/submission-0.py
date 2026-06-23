# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cursor1 = list1
        cursor2 = list2
        dummy_head = ListNode(0, None)
        cur_head = dummy_head

        while cursor1 is not None or cursor2 is not None:
            if cursor1 is None:
                target_node = cursor2
            elif cursor2 is None:
                target_node = cursor1
            else:
                # Both cursor1 and cursor2 exist
                if cursor2.val > cursor1.val:
                    target_node = cursor1
                else:
                    target_node = cursor2
            cur_head.next = target_node
            cur_head = cur_head.next
            if target_node == cursor1:
                cursor1 = cursor1.next
            else:
                cursor2 = cursor2.next
        return dummy_head.next