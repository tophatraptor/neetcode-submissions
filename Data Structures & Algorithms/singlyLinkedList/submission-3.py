class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cursor = self.head
        cur_idx = 0
        while cur_idx < index:
            cursor = cursor.next
            cur_idx += 1
        return cursor.val

    def insertHead(self, val: int) -> None:
        self.length += 1
        if self.head is None:
            # Head, tail are both none
            new_node = Node(val, None)
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            new_head = Node(val, self.head)
            self.head = new_head
        

    def insertTail(self, val: int) -> None:
        if self.tail is None:
            return self.insertHead(val)
        old_tail = self.tail
        new_tail = Node(val, None)
        old_tail.next = new_tail
        self.tail = new_tail
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        self.length -= 1
        if index == 0:
            if self.head.next is None:
                self.head = None
                self.tail = None
                return True
            self.head = self.head.next
            return True
        prev, cur = self.head, self.head.next
        cur_idx = 1
        while cur_idx < index:
            prev = cur
            cur = cur.next
            cur_idx += 1
        # At this juncture, prev points to the index behind i
        if self.tail == cur:
            self.tail = prev
            prev.next = None
        else:
            prev.next = cur.next
        return True

    def getValues(self) -> List[int]:
        values = []
        cursor = self.head
        while cursor is not None:
            values.append(cursor.val)
            cursor = cursor.next
        return values