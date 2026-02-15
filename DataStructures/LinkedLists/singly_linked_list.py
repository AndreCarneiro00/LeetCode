class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class SinglyLinkedList:
    def __init__(self, lst: list):
        self.head = None
        self.tail = None
        prev = None

        for val in lst:
            node = Node(val)
            if not self.head:
                self.head = node
            else:
                prev.next = node

            self.tail = node
            prev = node

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node

        curr = self.tail
        while curr.next:
            curr = curr.next
            self.tail = curr

    def pop_left(self):
        if self.head is None:
            return None

        val = self.head.val
        new_head = self.head.next
        self.head.next = None
        self.head = new_head

        if self.head is None:
            self.tail = None

        return val

    def pop(self):
        if self.head is None:
            return None

        val = self.tail.val

        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        if prev:
            prev.next = None
            self.tail = prev
        else:
            self.head = None
            self.tail = None

        return val

    def clear(self):
        self.head = None
        self.tail = None


if __name__ == "__main__":
    linked_list = SinglyLinkedList([1, 2, 3, 4, 5, 6])
    print("debug")
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print("debug")
