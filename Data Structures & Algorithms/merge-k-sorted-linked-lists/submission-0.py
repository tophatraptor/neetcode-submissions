# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, x in enumerate(lists):
            if x is None:
                continue
            heapq.heappush(heap, (x.val, i, x))
        dummy_head = ListNode(None, None)
        cursor = dummy_head
        while len(heap) > 0:
            value, idx, node = heapq.heappop(heap)
            cursor.next = node
            cursor = node
            if node.next is not None:
                next_value = node.next.val
                next_node = node.next
                heapq.heappush(heap, (next_value, idx, next_node))
        return dummy_head.next