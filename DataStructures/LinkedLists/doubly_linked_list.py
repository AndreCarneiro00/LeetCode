class Node:
    def __init__(self, val, next_node=None, prev=None):
        self.val = val
        self.next = next_node
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, lst: list):
        self.head = None
        self.tail = None
        prev = None

        for val in lst:
            node = Node(val)
            if not self.head:
                self.head = node
            else:
                node.prev = prev
                prev.next = node

            self.tail = node
            prev = node

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node

        curr = self.tail
        while curr.next:
            curr = curr.next
            self.tail = curr


if __name__ == "__main__":
    linked_list = DoublyLinkedList([1, 2, 3])
    print("debug")
    linked_list.append(7)
    print("debug")