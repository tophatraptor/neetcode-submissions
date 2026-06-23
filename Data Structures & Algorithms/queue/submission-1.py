class DLLNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.dummy_head = DLLNode(None, None, None)
        self.dummy_tail = DLLNode(None, self.dummy_head, None)
        self.dummy_head.next = self.dummy_tail
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        if self.length == 0:
            new_node = DLLNode(value, self.dummy_head, self.dummy_tail)
            self.dummy_head.next = new_node
            self.dummy_tail.prev = new_node
            self.length += 1
            return
        old_tail = self.dummy_tail.prev
        new_node = DLLNode(value, old_tail, self.dummy_tail)
        old_tail.next = new_node
        self.dummy_tail.prev = new_node
        self.length += 1

    def appendleft(self, value: int) -> None:
        if self.length == 0:
            return self.append(value)
        old_head = self.dummy_head.next
        new_node = DLLNode(value, self.dummy_head, old_head)
        self.dummy_head.next = new_node
        old_head.prev = new_node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        node_to_pop = self.dummy_tail.prev
        before = node_to_pop.prev
        after = self.dummy_tail
        before.next = after
        after.prev = before
        self.length -= 1
        return node_to_pop.val

    def popleft(self) -> int:
        if self.length == 0:
            return -1
        node_to_pop = self.dummy_head.next
        before = self.dummy_head
        after = node_to_pop.next
        before.next = after
        after.prev = before
        self.length -= 1
        return node_to_pop.val