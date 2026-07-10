# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length of list
        if head is None:
            return None
        cur_len = 1
        cur_node = head
        while cur_node.next is not None:
            cur_len += 1
            cur_node = cur_node.next
        # Now we know the length of the array
        # Formula for the index is cur_len - n + 1
        if cur_len == n:
            return head.next
        anchor_idx = cur_len - n - 1
        cur_idx = 0
        cur_node = head
        while cur_idx < anchor_idx:
            cur_idx += 1
            cur_node = cur_node.next
        # Now cur_node pointing at the node *before* the one we want to remove
        cur_node.next = cur_node.next.next
        return head